import json
import os

from . import pos_predict
#from models_collect import perplexity_calc

def literal_folder_files(folder_path):
    file_paths = []
    for item in os.scandir(folder_path):
        file_paths.append(item.path)

    file_paths.sort()
    for file_path in file_paths:
        file_name = file_path.split('/')[-1]
        #print('file name:{}'.format(file_name))

    return file_paths

def json_content_reader(file_path):
    with open(file_path, encoding="utf-8") as f:
        content = f.read()

    content_json = json.loads(content)
    knowledge_node = content_json['knowledge_node']
    interference_node = content_json['interference_node']

    word_entity_class = content_json['word_entity_class']
    interference_entity_class = content_json['interference_entity_class']
    path = content_json['path']
    input_prompt = content_json['input_prompt']
    output_article = content_json['output_article']
    relation = content_json['relation']

    paths = path.split('->')
    relations = relation.split('->')

    triple_list = []
    node_count = len(paths)
    for index in range(0, node_count-1):
        head = paths[index].strip()
        tail = paths[index + 1].strip()
        connect = relations[index].strip()

        triple = f"{head} {connect} {tail}"
        triple_list.append(triple)

    node = {}
    node['interference_node'] = interference_node
    node['knowledge_node'] = knowledge_node
    node['input_prompt'] = input_prompt
    node['output_article'] = output_article
    node['word_entity_class'] = word_entity_class
    node['interference_entity_class'] = interference_entity_class
    node['triple_list'] = triple_list
    return node

def file_content_reader(file_path):
    with open(file_path, encoding="utf-8") as f:
        content = f.read()

    #print(content)
    content_json = json.loads(content)
    knowledge_entity = content_json['knowledge_entity']
    word_entity = content_json['word_entity']
    input_prompt = content_json['input_prompt']
    output_article = content_json['output_articles']

    word_entity_set = set()
    knowledge_entity_set = set()
    for word in knowledge_entity:
        word_set = set(word.split())
        word_entity_set = word_entity_set.union(word_set)
    for word in word_entity:
        word_set = set(word.split())
        word_entity_set = word_entity_set.union(word_set)

    return input_prompt, output_article, word_entity_set




if __name__=='__main__':
    path = "/Users/liunian/Downloads/personal/论文相关/实验/with_diversity/GPT4 Result with K 500 lines 0 number 0.json"
    file_content_reader(path)
    folder_path = "/Users/liunian/Downloads/personal/论文相关/实验/with_diversity/"
    #literal_folder_files(folder_path)
