import json


def get_file_list(file_path):
    md_file_list = []

    with open(file_path, "r") as fp:
        for line in fp.readlines():
            line = line.strip()
            data_json = json.loads(line)
            md_file_dir = data_json['md_file_dir']
            question = data_json['question']
            title = data_json['title']
            url_source = data_json['url_source']
            processed_md_file_dir = data_json['processed_md_file_dir']

            md_file_list.append(md_file_dir)

        fp.close()
    return md_file_list

def read_file_content(file_path):
    file_content = ''
    with open(file_path, "r", encoding="utf-8") as fp:
        #file_content = fp.readlines()
        file_content = fp.read()
        fp.close()
    return file_content


def read_all_files(json_path):
    all_file_paths = get_file_list(json_path)
    content_list = []
    count = 0
    for file in all_file_paths:
        content = read_file_content(file)
        content_list.append(content)
        count += 1
        if count > 100:
            break

    return content_list


if __name__ == '__main__':
    file_path = '/Users/liunian/Downloads/personal/之江实验室/DDE/大模型/问答语料增强/final_data.json'
    all_file_contents = read_all_files(file_path)
    print(len(all_file_contents))


