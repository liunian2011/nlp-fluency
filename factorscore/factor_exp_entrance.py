import os.path

from ner_predict import file_resolve
from .Xls_resolve import Xls_resolve
from .fact_gen import generate_fact

factscore_folder = "/Users/liunian/Downloads/personal/论文相关/医疗实验/GPT4_generation_experiment_select_long_path/"
factscore_json_file_paths = file_resolve.literal_folder_files(factscore_folder)

test_file_path = "/Users/liunian/Downloads/personal/论文相关/医疗实验/GPT4_generation_experiment_new/GPT4 Generate Result from amphibian to cell function path number 0 experiment number 0.json"
file_resolve.json_content_reader(test_file_path)

excel_file_path = "/Users/liunian/Downloads/personal/论文相关/医疗实验/factscore_ln.xlsx"

def resolve_json_files():
    all_target_list = []
    for index in range(len(factscore_json_file_paths)):
        file_path = factscore_json_file_paths[index]
        node = file_resolve.json_content_reader(file_path)
        #node['record_num'] = index+1

        all_target_list.append(node)

    resolver = Xls_resolve(excel_file_path)
    resolver.append_table_data(all_target_list)

def add_input_prompt_data():
    input_list = []
    for index in range(len(factscore_json_file_paths)):
        file_path = factscore_json_file_paths[index]
        node = file_resolve.json_content_reader(file_path)
        input_list.append(node['input_prompt'])

    resolver = Xls_resolve(excel_file_path)
    input_prompt_index = 9
    resolver.save_column_data(input_prompt_index, input_list)

def generate_fact_flow():
    resolver = Xls_resolve(excel_file_path)
    output_article_index = 8
    output_article_list = resolver.read_column_data(output_article_index, start_row_index=1031)

    facts_array = []
    i = 0
    for article in output_article_list:
        facts = generate_fact(article)
        facts_array.append(facts)
        i += 1
    resolver.save_column_data(9, facts_array, start_row_index=1031)


def generate_cell_fact_flow():
    resolver = Xls_resolve(excel_file_path)
    #row_list = [166, 200, 202, 226, 258, 259, 291, 300, 322, 323, 354, 355, 358, 390, 391, 422, 425, 451, 461]
    #row_list = [134]
    #row_list = [103,106,133,136,163,169,194,197,225,227,262,264,292,294,326,329,887,898,903,904,936,940,967,972,999,1000,993,994,996,997,998,1001,1015,1023,1025,1029]
    #row_list = [879, 888, 892, 893, 894, 895, 896, 897, 900,907, 912,918,919,929,933,934,935,949,954,960,963,965,966,968,992,  360,361,392,418,419,460,464,488,498,522,523,548,582,589,617,645,678,679,708,709,715,724,744,775,777,817,844,849,871]
    #row_list = [865,868,869,870,873,877,885,890,901,902,905,906,930,932,948,951,957,962,964,981,982,987,991,995,1024,1028]
    row_list = [63,68,98,102,130,139,170,196,198,230,268,269,324,327,356,359,386,410,420,423,452,454,483,507,872,943,944,971,974,1005,1006]
    for row_index in row_list:
        print(f'row index:{row_index}')
        output_article = resolver.read_cell_data(8, row_index)
        facts = generate_fact(output_article)
        if facts:
            resolver.write_cell_data(9, row_index, facts)
        else:
            print(f'row_index :{row_index} generate fact failed.')


def generate_all_fact_flow():
    resolver = Xls_resolve(excel_file_path)
    facts_index = 9
    facts_column_data = resolver.read_column_data(facts_index)
    print(f'facts count:{len(facts_column_data)}')
    empty_fact_index_list = []
    for fact_index in range(len(facts_column_data)):
        fact = facts_column_data[fact_index]
        if not fact:
            empty_fact_index_list.append(fact_index)

    print(empty_fact_index_list)

    for row_index in empty_fact_index_list:
        row_index += 1
        print(f'row index:{row_index}')
        output_article = resolver.read_cell_data(8, row_index)
        facts = generate_fact(output_article)
        if facts:
            resolver.write_cell_data(9, row_index, facts)
        else:
            print(f'row_index :{row_index} generate fact failed.')

def copy_file_result_flow():
    left_file_path = "/Users/liunian/Downloads/personal/论文相关/医疗实验/factscore_jx_null_update.xlsx"
    right_file_path = "/Users/liunian/Downloads/personal/论文相关/医疗实验/factscore_ln.xlsx"
    left_resolver = Xls_resolve(left_file_path)
    right_resolver = Xls_resolve(right_file_path)

    left_parent_folder = "/Users/liunian/Downloads/personal/论文相关/医疗实验/factscore/12.19_jx/"
    left_sub_folders = file_resolve.literal_folder(left_parent_folder)
    id_list = []
    for index in range(len(left_sub_folders)):
        sub_folder = left_sub_folders[index]
        folder_name = sub_folder.split('/')[-1]
        id = folder_name.split('-')[0]
        id_list.append(id)

    print(id_list)

    left_result = left_resolver.get_left_result(id_list)
    right_resolver.write_right_result(id_list, left_result)


def find_not_consistent_flow():
    right_file_path = "/Users/liunian/Downloads/personal/论文相关/医疗实验/factscore_ln.xlsx"
    right_resolver = Xls_resolve(right_file_path)
    excel_ids = right_resolver.get_all_id_value()
    excel_id_set = set(excel_ids)
    print(f'excel id len:{len(excel_id_set)}')

    all_ids = []
    left_parent_folder = "/Users/liunian/Downloads/personal/论文相关/医疗实验/factscore/"
    left_sub_folders = file_resolve.literal_folder(left_parent_folder)
    for sub_folder in left_sub_folders:
        sub_sub_folders = file_resolve.literal_folder(sub_folder)
        for sub_sub_folder in sub_sub_folders:
            id = int(sub_sub_folder.split('/')[-1].split('-')[0])
            all_ids.append(id)
    all_ids.sort()

    all_id_set = set(all_ids)
    print(f'all id len:{len(all_id_set)}')
    print(all_id_set)
    left_ids = all_id_set - excel_id_set
    print('left ids:')
    print(left_ids)


def collect_all_top3_top1_flow():
    all_top_files = []

    left_parent_folder = "/Users/liunian/Downloads/personal/论文相关/医疗实验/factscore/"
    left_sub_folders = file_resolve.literal_folder(left_parent_folder)
    for sub_folder in left_sub_folders:
        sub_sub_folders = file_resolve.literal_folder(sub_folder)
        for sub_sub_folder in sub_sub_folders:
            sub_sub_sub_files = file_resolve.literal_folder_files(sub_sub_folder)
            top_file_paths = [file for file in sub_sub_sub_files if file.__contains__('top3') or file.__contains__('_top1')]
            all_top_files.extend(top_file_paths)

    import shutil

    target_folder = "/Users/liunian/Downloads/personal/论文相关/医疗实验/all_500_top_files/"
    for top_file_path in all_top_files:
        file_name = top_file_path.split('/')[-1]
        try:
            f_dst = os.path.join(target_folder, file_name)
            shutil.move(top_file_path, f_dst)
        except Exception as e:
            print(f'move file error:{e}')


def generate_all_fact_flow():
    resolver = Xls_resolve(excel_file_path)
    facts_index = 9

def split_list_by_n(list_collection, n):
    for i in range(0, len(list_collection), n):
        yield list_collection[i:i+n]

def divide_facts_flow():
    resolver = Xls_resolve(excel_file_path)
    facts_index = 10
    facts_list = resolver.read_column_data(facts_index)

    factscore_prompt_template = """**Factuality Assessment Task**
Based on the information provided in attached documents, evaluate the factuality of the following statements, DO NOT refer to any external knowledge or information beyond the provided attachments.
Respond with "Supported", or "Not-supported" or "Not-mentioned" , provide explanatory reasons in the following format:
Statement [Number] | [Your Answer] | [Explanatory Reasoning] 

**Additional Guidance:**
Supported: The statement is accurate based on available evidence.
Not-mentioned: Lack of credible evidence to determine accuracy.
Not-supported: The statement is inaccurate or contradicts established facts.

**examples**
Supported: "The company's revenue increased by 10% in 2020 compared to 2019." (If the attachment files contain a financial report showing the company's revenue in 2019 as $100,000 and in 2020 as $110,000, this statement would be supported because the numbers can be used to calculate the 10% increase.)
Not-Supported: "The company's revenue increased by 20% in 2020 compared to 2019." (If the attachment files contain the same financial report, this statement would not be supported because the numbers do not support a 20% increase.)
Not-mentioned: "The company's CEO is planning to retire in 2023." (If the attachment files do not mention the CEO's retirement plans or any information about the CEO's future plans, this statement would be Not-mentioned.)

**Your Task:**
Please evaluate the factual accuracy of the following statements:
{facts}
"""

    threshold = 8

    all_facts_prompts = []
    for fact in facts_list:
        prompt_list = []
        if not fact:
            continue
        lines = fact.split('\n')
        sub_lists = split_list_by_n(lines, threshold)
        for sub_fact in sub_lists:
            sub_fact_prompt = factscore_prompt_template.format(facts=str(sub_fact))
            prompt_list.append(sub_fact_prompt)
            #prompt_list.append('\n\n********\n\n')
        all_facts_prompts.append(str(prompt_list))
        all_facts_prompts.append('\n\n********\n\n')

    print(f'all_facts_prompts len:{len(all_facts_prompts)}')
    resolver.save_column_data(11, all_facts_prompts)




