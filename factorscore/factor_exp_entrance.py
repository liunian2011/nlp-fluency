from ner_predict import file_resolve
from .Xls_resolve import Xls_resolve
from .fact_gen import generate_fact

factscore_folder = "/Users/liunian/Downloads/personal/论文相关/医疗实验/GPT4_generation_experiment_new/"
factscore_json_file_paths = file_resolve.literal_folder_files(factscore_folder)

test_file_path = "/Users/liunian/Downloads/personal/论文相关/医疗实验/GPT4_generation_experiment_new/GPT4 Generate Result from amphibian to cell function path number 0 experiment number 0.json"
file_resolve.json_content_reader(test_file_path)

excel_file_path = "/Users/liunian/Downloads/personal/论文相关/医疗实验/所有组实验结果.xlsx"

def resolve_json_files():
    all_target_list = []
    for index in range(len(factscore_json_file_paths)):
        file_path = factscore_json_file_paths[index]
        node = file_resolve.json_content_reader(file_path)
        node['record_num'] = index+1

        all_target_list.append(node)

    resolver = Xls_resolve(excel_file_path)
    resolver.save_table_data(all_target_list)

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
    output_article_index = 9
    output_article_list = resolver.read_column_data(output_article_index)
    facts_array = []
    i = 0
    for article in output_article_list:
        i += 1
        if i == 10:
            break
        facts = generate_fact(article)
        facts_array.append(facts)
    resolver.save_column_data(10, facts_array)





