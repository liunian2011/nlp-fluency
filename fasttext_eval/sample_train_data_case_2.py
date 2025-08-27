import random


"""
oa_pos_train_data.txt  271821

scihub_pos_train_data.txt  500000
scihub_neg_train_data.txt  27927

book_pos_train_data.txt  8163
book_neg_train_data.txt  30868

just_moment_neg_train_data.txt  5000
temporary_unavailable_neg_train_data.txt  5000  

wiki_neg_train_data.txt 300000

pos_total:      779984
neg_total:      368795
"""


def split_train_valid(all_data, split_rate=0.1):
    d_length = len(all_data)
    
    random.shuffle(all_data)
    eval_num = int(d_length * split_rate)
    
    eval_data = all_data[:eval_num]
    train_data = all_data[eval_num:]
    
    return train_data, eval_data


def get_file_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        all_lines = [line.strip() for line in f]
    return all_lines


"""
=====方案1：=======
neg: book + scihub + [just_moment 和 temporary采样] + wiki 
pos: book + scihub + oa 

正负比约 
再各取出 1% 作为验证集
"""

# 反例
neg_lines = []
book_neg_lines = get_file_lines('book_neg_train_data.txt')
scihub_neg_lines = get_file_lines('scihub_neg_train_data.txt')
just_moment_neg_lines = get_file_lines('just_moment_neg_train_data.txt')
temporary_neg_lines = get_file_lines('temporary_unavailable_neg_train_data.txt')
wiki_neg_lines = get_file_lines('wiki_neg_train_data.txt')

neg_lines.extend(book_neg_lines)
neg_lines.extend(scihub_neg_lines)
neg_lines.extend(just_moment_neg_lines)
neg_lines.extend(temporary_neg_lines)
neg_lines.extend(wiki_neg_lines)

train_neg_lines, eval_neg_lines = split_train_valid(neg_lines)
print(f'反例数据: 训练集{len(train_neg_lines)}条; 验证集{len(eval_neg_lines)}条')

# 正例
pos_lines = []

book_pos_lines = get_file_lines('book_pos_train_data.txt')
oa_pos_lines = get_file_lines('oa_pos_train_data.txt')
scihub_pos_lines = get_file_lines('scihub_pos_train_data.txt')

pos_lines.extend(book_pos_lines)
pos_lines.extend(oa_pos_lines)
pos_lines.extend(scihub_pos_lines)

train_pos_lines, eval_pos_lines = split_train_valid(pos_lines)
print(f'正例数据: 训练集{len(train_pos_lines)}条; 验证集{len(eval_pos_lines)}条')

train_lines = train_pos_lines + train_neg_lines
eval_lines = eval_pos_lines + eval_neg_lines

with open('train_data_case_1.txt', 'w', encoding='utf-8') as f:
    for line in train_lines:
        f.write(line + '\n')

with open('eval_data_case_1.txt', 'w', encoding='utf-8') as f:
    for line in eval_lines:
        f.write(line + '\n')

