import json
from qa_generate import generate_qa_pairs

geo_oa_pdf_content_file_path = '/Users/liunian/Downloads/personal/之江实验室/DDE/大模型/测评体系/原始语料/geo-oa-paper-2000.jsonl'

def read_dataset(file_path):
    dataset = []
    with open(file_path, 'r') as f:
        for line in f:
            line_s = line.strip()
            item = json.loads(line_s)
            text = item['text']
            dataset.append(text)
    return dataset

def start_generate_qa(orig_oa_count=10):
    all_dataset = read_dataset(geo_oa_pdf_content_file_path)
    part_dataset = all_dataset[:orig_oa_count]

    all_qas = []
    for oa_pdf in part_dataset:
        oa_pdf_qas = generate_qa_pairs(oa_pdf)
        all_qas.extend(oa_pdf_qas)

    # Step 5: 可选：把结果写到本地
    with open("generated_qa/generated_geo_qas.jsonl", "a", encoding="utf-8") as f:
        for qa in all_qas:
            f.write(json.dumps(qa) + ' \n')


if __name__=='__main__':
    start_generate_qa(orig_oa_count=100)