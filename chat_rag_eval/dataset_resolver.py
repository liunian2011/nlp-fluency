import json

class dataset_resolver(object):
    path = None

    def __init__(self, json_path):
        self.path = json_path

    def read_json_file(self):
        dataset_list = []
        with open(self.path, "r") as f:
            for line in f:
                orig_dataset = json.loads(line)
                #print(orig_dataset['idx'])
                dataset_list.append(orig_dataset)

        return dataset_list

    def save_dataset(self, json_list, new_file_path):
        with open(new_file_path, 'w') as f:
            for dataset in json_list:
                json_s = json.dumps(dataset)
                f.write(json_s)
                f.write('\n')








if __name__ == '__main__':
    path = "/Users/liunian/Downloads/personal/之江实验室/DDE/大模型/语料增强/oa_synthetic_lqa_clean.jsonl"
    resolver = dataset_resolver(path)
    all_dataset = resolver.read_json_file()
    print(all_dataset.__sizeof__())

    new_path = "/Users/liunian/Downloads/personal/之江实验室/DDE/大模型/语料增强/rewrite/oa_rewrite.jsonl"
    resolver.save_dataset(all_dataset, new_path)
