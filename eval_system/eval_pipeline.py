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
    i = 0
    all_ppl_score = {}
    dataset = read_dataset(dataset_path)
    for item in dataset:
        score = ppl.cal_ppl_score_1(item)

        all_ppl_score[i] = score
        print(f'ppl score:{score}')
    return all_ppl_score


def read_ppl_result():
    import pandas as pd
    file_path = '/Users/liunian/Downloads/personal/之江实验室/DDE/大模型/测评体系/log/ppl_result.log'
    #bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 100]
    bins = [0, 10, 20, 30, 40, 50, 60, 70, 100]

    data_list = []
    with open(file_path, 'r') as f:
        for line in f:
            ppl = float(line.strip())
            data_list.append(ppl)

    result = pd.cut(data_list, bins)
    counts = result.value_counts()
    print(counts)


if __name__ == '__main__':
    #all_ppl = start_ppl_eval()
    #print(all_ppl)
    read_ppl_result()