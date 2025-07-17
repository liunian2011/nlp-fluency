import random


"""
book_neg	    27927
book_pos	    2602338
oa_pos	        271821
fineweb_neg	    245075
fineweb_pos	    382354
just_moment_neg	679176
temporary_neg	55375
web_search_pos	45906

pos_total:      3302419
neg_total:      1007553
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
neg: book + fineweb  (273002) + [just_moment 和 temporary采样(30000)]
pos: web_search所有(45906) + 其他pos采样(660000)

正负比约 7：3
再各取出 1% 作为验证集
"""

# 反例
neg_lines = []
book_neg_lines = get_file_lines('book_neg_train_data.txt')
fineweb_neg_lines = get_file_lines('fine_web_neg_train_data.txt')
just_moment_neg_lines = get_file_lines('just_moment_neg_train_data.txt')
temporary_neg_lines = get_file_lines('temporary_unavailable_neg_train_data.txt')

web_search_neg_lines = just_moment_neg_lines + temporary_neg_lines
web_search_neg_sample_lines = random.sample(web_search_neg_lines, k=30000)

neg_lines.extend(book_neg_lines)
neg_lines.extend(fineweb_neg_lines)
neg_lines.extend(web_search_neg_sample_lines)

train_neg_lines, eval_neg_lines = split_train_valid(neg_lines)
print(f'反例数据: 训练集{len(train_neg_lines)}条; 验证集{len(eval_neg_lines)}条')

# 正例
pos_lines = []
web_search_pos = get_file_lines('web_search_pos_train_data.txt')

book_pos_lines = get_file_lines('book_pos_train_data.txt')
oa_pos_lines = get_file_lines('oa_pos_train_data.txt')
fineweb_pos_lines = get_file_lines('fine_web_pos_train_data.txt')

other_pos_lines = book_pos_lines + oa_pos_lines + fineweb_pos_lines
other_pos_sample_lines = random.sample(other_pos_lines, k=660000)

pos_lines.extend(web_search_pos)
pos_lines.extend(other_pos_sample_lines)

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

