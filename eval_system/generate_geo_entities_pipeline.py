import geo_entities_util
import os
import json

#geo_corpus_file_path = '/Users/liunian/Downloads/personal/之江实验室/DDE/大模型/测评体系/原始语料/geo-oa-paper-2000.jsonl'
geo_corpus_file_path = '/Users/liunian/Downloads/personal/之江实验室/DDE/大模型/测评体系/原始语料/v0.9-20250616-43B-2000.jsonl'

def read_dataset(file_path):
    dataset = []
    with open(file_path, 'r') as f:
        for line in f:
            line_s = line.strip()
            item = json.loads(line_s)
            dataset.append(item)
    return dataset


def start_generate_geo_entities(input_file, eval_count=10):
    corpus_list = read_dataset(input_file)

    already_eval_count = 0
    with open("generated_geo_entities/wiki_claud_geo_entities.jsonl", "a", encoding="utf-8") as f:
        for single_corpus in corpus_list:
            if already_eval_count == eval_count:
                break
            already_eval_count += 1
            corpus_text = single_corpus['text']
            geo_entities = geo_entities_util.get_geo_entities(corpus_text)

            single_corpus.pop('text')
            if len(geo_entities):
                single_corpus['geo_entities'] = geo_entities['geoscience_terms']
                single_corpus['geo_enti_count'] = len(single_corpus['geo_entities'])
                print(f'{single_corpus}')
                f.write(json.dumps(single_corpus) + ' \n')
            else:
                print(f"get geo entities failed. idx:{single_corpus['idx']}")


if __name__ == '__main__':
    start_generate_geo_entities(geo_corpus_file_path, eval_count=20)