import fasttext
import re
import os

label_1 = '__label__1,'
label_0 = '__label__0,'


# 正则表达式
md_pattern = re.compile(r'Markdown Content:')
url_pattern = re.compile(
    r'(https?|ftp)://(www\.)?[-a-zA-Z0-9@:%._+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_+.~#?&/=]*)')
def get_all_file(root_dir):
    print("开始遍历文件夹")
    file_paths = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.strip().endswith('.md'):
                file_paths.append(os.path.join(root, file))
    return file_paths


def parse_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        # 将换行替换为空格
        content = ' '.join([line.strip() for line in f.readlines()])

    # 取 Markdown Content:之后的内容
    match = md_pattern.search(content)
    start, end = match.span()
    content = content[end:]
    # 去除链接
    content = url_pattern.sub(' ', content)

    return content

def predict_file(model_path, input_file):
    model = fasttext.load_model(model_path)

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    results = []
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        labels, probabilities = model.predict(line, k=1)  # 只取最可能的标签
        results.append((line, labels[0], probabilities[0]))

        if labels[0] == label_0:
            print(f'predict not right: {labels[0]}, {probabilities[0]}, line: {line}')

    return results

def predict_md_files():
    model_path = "/mnt/geogpt/duyuxuan/train_fasttext/liunian/second_train/output/geo_fasttext_model_1.bin"
    root_folder = "/mnt/geogpt/duyuxuan/train_fasttext/websearch_neg_20250714/"
    model = fasttext.load_model(model_path)

    file_paths = get_all_file(root_folder)
    for file_path in file_paths:
        content = parse_file(file_path)
        labels, probabilities = model.predict(content, k=1)  # 只取最可能的标签
        print(f'label:{labels[0]}, probabilities:{probabilities[0]}, {content}')

def predict_test_data_file():
    model_path = "/mnt/geogpt/duyuxuan/train_fasttext/liunian/second_train/output/geo_fasttext_model_1.bin"
    #input_file = "/mnt/geogpt/duyuxuan/train_fasttext/liunian/fasttext_train/fasttext_test_data_combined.txt"
    input_file = "/mnt/geogpt/duyuxuan/train_fasttext/liunian/second_train/web_search_pos_sample_data.txt"

    results = predict_file(model_path, input_file)

    pos_result_list = []
    neg_result_list = []
    for line, label, prob in results:
        print(f"{label} ({prob:.4f})")
        label = label.strip()
        if line.startswith(label_1):
            pos_is_correct = 1 if label == label_1 else 0
            pos_result_list.append(pos_is_correct)
        elif line.startswith(label_0):
            neg_is_correct = 1 if label == label_0 else 0
            neg_result_list.append(neg_is_correct)

    pos_correct_count = pos_result_list.count(1)
    neg_correct_count = neg_result_list.count(1)
    if len(pos_result_list) > 0:
        print(f'pos right count:{pos_correct_count}, pos precision:{pos_correct_count/len(pos_result_list)}')
    if len(neg_result_list) > 0:
        print(f'neg right count:{neg_correct_count}, neg precision:{neg_correct_count/len(neg_result_list)}')


if __name__ == "__main__":
    #predict_md_files()
    predict_test_data_file()






