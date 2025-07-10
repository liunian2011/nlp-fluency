import json
import ppl
dataset_path = '/Users/liunian/Downloads/personal/之江实验室/DDE/大模型/测评体系/原始语料/v0.9-20250616-43B-2000.jsonl'

def read_dataset(file_path):
    dataset = []
    with open(file_path, 'r') as f:
        for line in f:
            line_s = line.strip()
            item = json.loads(line_s)
            text = item['text']
            dataset.append(text)
    return dataset


def start_ppl_eval():
    dataset = read_dataset(dataset_path)
    for item in dataset:
        score = ppl.cal_ppl_score_1(item)

        print(f'ppl score:{score}')

if __name__ == '__main__':
    start_ppl_eval()