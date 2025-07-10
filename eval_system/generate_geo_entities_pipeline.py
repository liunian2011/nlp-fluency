import geo_entities_util
import os
import json

geo_corpus_file_path = '/Users/liunian/Downloads/personal/之江实验室/DDE/大模型/测评体系/原始语料/geo-oa-paper-2000.jsonl'

def read_dataset(file_path):
    dataset = []
    with open(file_path, 'r') as f:
        for line in f:
            line_s = line.strip()
            item = json.loads(line_s)
            dataset.append(item)
    return dataset


def start_generate_geo_entities(input_file):
    corpus_list = read_dataset(geo_corpus_file_path)
    with open("generated_geo_entities/geo_entities.jsonl", "a", encoding="utf-8") as f:
        for single_corpus in corpus_list:
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
    start_generate_geo_entities(geo_corpus_file_path)