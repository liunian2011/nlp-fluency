import xlwt
import xlrd
import openpyxl

class Xls_resolve(object):
    path = None

    def __init__(self, path):
        self.path = path

    def test(self):
        workbook = openpyxl.load_workbook(self.path)
        sheet = workbook.worksheets[0]

        for i in range( 3):
            print(i)
            print(sheet.cell(row=i+1, column=2).value)

    def save_column_data(self, column_index:int, column_data:list):
        workbook = openpyxl.load_workbook(self.path)
        sheet = workbook.worksheets[0]

        row_number = sheet.max_row
        print(f'table row size:{row_number}')
        print(f'column data size:{len(column_data)}')
        for i in range(len(column_data)):
            sheet.cell(row=i+2, column=column_index+1).value = column_data[i]
        workbook.save(self.path)

    def save_table_data(self, record_list:list):
        workhook = xlrd.open_workbook(self.path)
        sheet = workhook.sheet_by_index(0)

        #knowledge_node, interference_node, output_article, word_entity_class, interference_entity_class, triple_list
        target_list = []
        rows = len(record_list)

        for i in range(rows):
            record = record_list[i]

            record_num = record['record_num']
            knowledge_node = record['knowledge_node']
            word_entity_class = record['word_entity_class'] #分类树
            interference_node = record['interference_node'] #干扰词
            interference_entity_class = record['interference_entity_class'] #干扰词分类树
            triple_list = record['triple_list'] #最短路径
            output_article = record['output_article']

            sheet.write(i+1, 0, record_num)
            sheet.write(i+1, 1, knowledge_node)
            sheet.write(i+1, 2, word_entity_class)
            sheet.write(i+1, 3, interference_node)
            sheet.write(i+1, 4, interference_entity_class)
            sheet.write(i+1, 5, str(triple_list))
            sheet.write(i+1, 6, output_article)

        workhook.save(self.path)

    def read_column_data(self, column_index):
        workbook = openpyxl.load_workbook(self.path)
        sheet = workbook.worksheets[0]

        #rows = sheet.rows
        cols = sheet.columns

        col_data = []
        for cell in list(cols)[column_index]:
            col_data.append(cell.value)
        print(f'col_data size:{len(col_data)}')
        return col_data



if __name__ == '__main__':
    resolver = Xls_resolve("/Users/liunian/Downloads/personal/论文相关/医疗实验/所有组实验结果.xlsx")
    #column_list = resolver.read_column_data(1)
    #print(column_list)
    resolver.test()