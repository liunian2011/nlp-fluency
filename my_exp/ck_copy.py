import collections
import datetime
import functools
import logging
import time

from clickhouse_driver import Client

source_conn = Client(host='source-host', user='user', password='password')
target_conn = Client(host='target-host', user='user', password='password')


def format_partition_expr(p):
    if isinstance(p, int):
        return p
    return f"'{p}'"


def execute_queries(conn, queries):
    if isinstance(queries, str):
        queries = queries.split(';')
    for q in queries:
        conn.execute(q.strip())


class Table(object):
    def __init__(self, database, name, ddl, partition_key, is_view):
        self.database = database
        self.name = name
        self.ddl = ddl.replace('CREATE TABLE', 'CREATE TABLE IF NOT EXISTS')
        self.partition_key = partition_key
        self.is_view = is_view

    def exists(self, conn):
        q = f"SELECT name FROM system.tables WHERE database = '{self.database}' AND name = '{self.name}'"
        return len(conn.execute(q)) > 0

    def get_partitions(self, conn):
        partitions = []
        q = f'SELECT {self.partition_key}, count() FROM {self.identity} GROUP BY {self.partition_key} ORDER BY {self.partition_key}'
        partitions = collections.OrderedDict(conn.execute(q))
        return partitions

    def get_total_count(self, conn):
        q = f'SELECT COUNT() FROM {self.identity}'
        return conn.execute(q)[0][0]

    def check_consistency(self):
        if not self.exists(target_conn):
            return False, None

        source_ttl_count = self.get_total_count(source_conn)
        target_ttl_count = self.get_total_count(target_conn)
        if source_ttl_count == target_ttl_count:
            return True, None

        if not self.partition_key:
            return False, None

        source_partitions = self.get_partitions(source_conn)
        target_partitions = self.get_partitions(target_conn)
        bug_partitions = []
        for p, c in source_partitions.items():
            if p not in target_partitions or c != target_partitions[p]:
                bug_partitions.append(p)
        return False, bug_partitions

    def create(self, replace=False):
        target_conn.execute(f'CREATE DATABASE IF NOT EXISTS {self.database}')
        if self.is_view:
            replace = True
        if replace:
            target_conn.execute(f'DROP TABLE IF EXISTS {self.identity}')
        target_conn.execute(self.ddl)

    def copy_data_from_remote(self, by_partition=True):
        self.create()
        if self.is_view:
            logging.info('ignore view %s', self.identity)
            return

        is_identical, bug_partitions = self.check_consistency()
        if is_identical:
            logging.info('table %s has the same number of rows, skip', self.identity)
            return

        if self.partition_key and by_partition:
            for p in bug_partitions:
                logging.info('copy partition %s=%s', self.partition_key, p)
                self._copy_partition_from_remote(p)
        else:
            self._copy_table_from_remote()

    def _copy_table_from_remote(self):
        queries = f'''
        DROP TABLE {self.identity};
        {self.ddl};
        INSERT INTO {self.identity}
        SELECT * FROM remote('{source_conn.host}', {self.identity}, '{source_conn.user}', '{source_conn.password}')
        '''
        execute_queries(target_conn, queries)

    def _copy_partition_from_remote(self, partition):
        partition = format_partition_expr(partition)
        queries = f'''
        ALTER TABLE {self.identity} DROP PARTITION {partition};
        INSERT INTO {self.identity}
        SELECT * FROM remote('{source_conn.host}', {self.identity}, '{source_conn.user}', '{source_conn.password}')
        WHERE {self.partition_key} = {partition}
        '''
        execute_queries(target_conn, queries)

    def copy_to_another_table(self, database, name=None):
        if not name:
            name = self.name
        assert not (self.database == database and self.name == name)
        if self.partition_key:
            partitions = self.get_partitions(target_conn)
            queries = [f'CREATE TABLE IF NOT EXISTS {database}.{name} AS {self.identity}']
            for p in partitions.keys():
                expr = format_partition_expr(p)
                queries.append(f'ALTER TABLE {database}.{name} DROP PARTITION {expr}')
                queries.append(f'ALTER TABLE {database}.{name} ATTACH PARTITION {expr} FROM {self.identity}')
            execute_queries(target_conn, queries)
        else:
            queries = f'''
            DROP TABLE IF EXISTS {database}.{name};
            CREATE TABLE {database}.{name} AS {self.identity};
            INSERT INTO {database}.{name} SELECT * FROM {self.identity};
            '''
            execute_queries(target_conn, queries)

    @property
    def identity(self):
        return f'{self.database}.{self.name}'

    def __str__(self):
        return self.identity

    __repr__ = __str__


def get_all_tables() -> [Table]:

    q = '''
    SELECT database, name, create_table_query, partition_key, engine = 'View' AS is_view
    FROM system.tables
    WHERE database NOT IN ('system')
    ORDER BY if(engine = 'View', 999, 0), database, name
    '''
    rows = source_conn.execute(q)
    tables = [Table(*values) for values in rows]
    return tables


def copy_remote_tables(tables):
    for idx, t in enumerate(tables):
        start_time = datetime.datetime.now()
        logging.info('>>>> start to migrate table %s, progress %s/%s', t.identity, idx+1, len(tables))
        t.copy_data_from_remote()
        logging.info('<<<< migrated table %s in %s', t.identity, datetime.datetime.now() - start_time)


def with_retry(max_attempts=5, backoff=120):
    def decorator(f):
        @functools.wraps(f)
        def inner(*args, **kwargs):
            attempts = 0
            while True:
                attempts += 1
                logging.info('start attempt #%s', attempts)
                try:
                    f(*args, **kwargs)
                except Exception as e:
                    if attempts >= max_attempts:
                        raise e
                    logging.exception('caught exception')
                    time.sleep(backoff)
                else:
                    break
        return inner
    return decorator


@with_retry(max_attempts=10, backoff=60)
def main():
    tables = get_all_tables()
    logging.info('got %d tables: %s', len(tables), tables)
    copy_remote_tables(tables)


if __name__ == '__main__':
    main()