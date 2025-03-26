import json
import llm_chat
import rag_retrievel
from dataset_resolver import dataset_resolver

oa_dataset_path = "/Users/liunian/Downloads/personal/之江实验室/DDE/大模型/语料增强/oa_synthetic_lqa_clean.jsonl"
agu_dataset_path = "/Users/liunian/Downloads/personal/之江实验室/DDE/大模型/语料增强/agu_synthetic_lqa_clean.jsonl"
lqa_dataset_path = "/Users/liunian/Downloads/personal/之江实验室/DDE/大模型/语料增强/lqa_176_with_statements_clean.jsonl"

new_oa_path = "/Users/liunian/Downloads/personal/之江实验室/DDE/大模型/语料增强/rewrite/oa_synthetic_lqa_clean.jsonl"
new_agu_path = "/Users/liunian/Downloads/personal/之江实验室/DDE/大模型/语料增强/rewrite/agu_synthetic_lqa_clean.jsonl"
new_lqa_path = "/Users/liunian/Downloads/personal/之江实验室/DDE/大模型/语料增强/rewrite/lqa_176_with_statements_clean.jsonl"

def start_eval_process():
    resolver = dataset_resolver(oa_dataset_path)
    dataset_list = resolver.read_json_file()
    for dataset in dataset_list:
        idx = dataset['idx']
        print(idx)
        question = dataset['question']
        #请求rag获取retrievel结果
        rag_retrievel_result = rag_retrievel.retrive(question)
        llm_prompt = llm_chat.compose_prompt(question, rag_retrievel_result)
        code, question_llm_answer = llm_chat.request(llm_prompt)
        dataset['answer'] = question_llm_answer

    resolver.save_dataset(dataset_list,new_oa_path)

if __name__ == '__main__':
    start_eval_process()