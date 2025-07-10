import json
import ast
import os
import file_interact
import redis_db_manager

def find_next_step_domain(match_pattern:str, source_data_file_path):
    matched_result = file_interact.grep_match_result(match_pattern, source_data_file_path)
    next_domain_list = []
    if len(matched_result) > 0:
        for pre_domain_index, next_domain_index in matched_result:
            next_domain_name = redis_db_manager.get_domain(next_domain_index)
            next_domain_list.append(next_domain_name)
    return next_domain_list

def find_pre_step_domain(match_pattern:str, source_data_file_path):
    matched_result = file_interact.grep_match_result(match_pattern, source_data_file_path)
    pre_domain_list = []
    if len(matched_result) > 0:
        for pre_domain_index, next_domain_index in matched_result:
            pre_domain_name = redis_db_manager.get_domain(pre_domain_index)
            pre_domain_list.append(pre_domain_name)
    return pre_domain_list

def get_all_next_domains(domain:str, source_data_file_path):
    domain_index = redis_db_manager.get_index(domain)
    match_pattern = '^{0}\s'.format(domain_index)
    all_next_domains = find_next_step_domain(match_pattern, source_data_file_path)
    return all_next_domains

def get_all_pre_domains(domain:str, source_data_file_path):
    domain_index = redis_db_manager.get_index(domain)
    match_pattern = '\s{0}$'.format(domain_index)
    all_pre_domains = find_pre_step_domain(match_pattern, source_data_file_path)
    return all_pre_domains


def start_ana_batch_domain_pipeline(input_file_path:str, source_data_file_path:str):
    with open(input_file_path, 'r') as f:
        for line in f:
            domain = line.split(',')[0].strip()
            url_count = line.split(',')[1].strip()
            next_step_domains = get_all_next_domains(domain, source_data_file_path)
            pre_step_domains = get_all_pre_domains(domain, source_data_file_path)
            domain_info = {'domain': domain, 'url_count': url_count, 'in_degree': len(pre_step_domains), 'out_degree': len(next_step_domains), 'next_domains': next_step_domains, 'pre_domains': pre_step_domains}
            yield domain_info


def record_ana_result():
    source_data_file_path = '/mnt/geogpt/liunian/domain_analysis/data/pld-arc'
    input_file = '/mnt/geogpt/liunian/domain_analysis/websearch/top_domain_10000.csv'
    metadata_file = '/mnt/geogpt/liunian/domain_analysis/websearch/metadata_top_10000.jsonl'
    out_degree_output_folder = '/mnt/geogpt/liunian/domain_analysis/websearch/out_degree_output/'
    in_degree_output_folder = '/mnt/geogpt/liunian/domain_analysis/websearch/in_degree_output/'
    for domain_info in start_ana_batch_domain_pipeline(input_file, source_data_file_path):
        print(f'domain finished matched :' + domain_info['domain'])
        out_degree_output_file_path = out_degree_output_folder + domain_info['domain'] + '.json'
        in_degree_output_file_path = in_degree_output_folder + domain_info['domain'] + '.json'
        with open(out_degree_output_file_path, 'w', encoding='utf-8') as f:
            out_domain_info = {'domain': domain_info['domain'],
                               'out_degree': domain_info['out_degree'],
                               'next_domains': domain_info['next_domains']
                               }
            f.write(json.dumps(out_domain_info) + '\n')
        with open(in_degree_output_file_path, 'w', encoding='utf-8') as f:
            in_domain_info = {'domain': domain_info['domain'],
                              'in_degree': domain_info['in_degree'],
                              'pre_domains': domain_info['pre_domains']
                              }
            f.write(json.dumps(in_domain_info) + '\n')
        with open(metadata_file, 'a', encoding='utf-8') as f:
            meta_info = {'domain': domain_info['domain'],
                         'url_count': domain_info['url_count'],
                         'out_degree': domain_info['out_degree'],
                         'in_degree': domain_info['in_degree']
                         }
            f.write(json.dumps(meta_info) + '\n')


def find_most_central_domains(metadata_file_path:str):
    domain_meta_list = []
    with open(metadata_file_path, 'r') as f:
        for line in f:
            file_meta = json.loads(line)
            domain_meta_list.append(file_meta)

    domain_meta_list.sort(key= lambda m:(m['out_degree']), reverse=True)
    print(f'after sorted: {domain_meta_list}')

def find_next_domains(pre_domain_list:list):
    next_domain_folder = '/mnt/geogpt/liunian/domain_analysis/fineweb/out_degree_output/'
    all_next_domain_set = set()
    for pre_domain in pre_domain_list:
        domain_file_path = os.path.join(next_domain_folder, '{0}.json'.format(pre_domain))
        with open(domain_file_path, 'r') as f:
            domain_info = json.load(f)
            next_domains = domain_info['next_domains']
            all_next_domain_set.update(next_domains)

    print(f'all next domain set len:{len(all_next_domain_set)}')
    print(f'all next domains:{all_next_domain_set}')

def find_domain_not_include(next_domain_file_path:str, all_domain_file_path:str):
    with open(next_domain_file_path, 'r') as f:
        content = f.read()
        next_domains = ast.literal_eval(content)

    all_domain_set = set()
    with open(all_domain_file_path, 'r') as f:
        for line in f:
            domain = line.split(',')[0].strip()
            url_count = line.split(',')[1].strip()
            all_domain_set.add(domain)

    not_include_domains = next_domains - all_domain_set
    print(f'not include domain len:{len(not_include_domains)}')
    print(f'not include domains:{not_include_domains}')


if __name__ == "__main__":
    #metadata_file_path = '/mnt/geogpt/liunian/domain_analysis/websearch/metadata_top_10000.jsonl'
    metadata_file_path  = '/mnt/geogpt/liunian/domain_analysis/fineweb/metadata_top_10000_1.jsonl'
    #find_most_central_domains(metadata_file_path)

    pre_domain_list = [
                       'harvard.edu',
                       'sciencedirect.com',
                       'researchgate.net',
                       'wiley.com',
                       'nih.gov',
                       'mdpi.com',
                       'copernicus.org',
                       'springer.com',
                       'nature.com',
                       'acs.org','arxiv.org','psu.edu','geoscienceworld.org'
                       ] #'wikipedia.org',
    #find_next_domains(pre_domain_list)
    next_domain_file_path = '/mnt/geogpt/liunian/domain_analysis/websearch/sort_result/next_domains_3.txt'
    all_domain_file_path = '/mnt/geogpt/liunian/domain_analysis/websearch/top_domain.csv'
    #find_domain_not_include(next_domain_file_path, all_domain_file_path)

    fineweb_pre_domain_list = [
        'geoscienceworld.org',
        'usgs.gov',
        'usda.gov',
        'climate.gov',
        'noaa.gov',
        'environmental-expert.com',
        'searchanddiscovery.com',
        'epa.gov',
        'nih.gov',
        'datadryad.org'
    ]
    #find_next_domains(fineweb_pre_domain_list)

    next_domain_file_path = '/mnt/geogpt/liunian/domain_analysis/fineweb/sort_result/next_domains.txt'
    all_domain_file_path = '/mnt/geogpt/liunian/domain_analysis/fineweb/top_most_common_full.csv'
    find_domain_not_include(next_domain_file_path, all_domain_file_path)

