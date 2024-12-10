import json
import os

triple_file_path = '/Users/liunian/Downloads/personal/论文相关/实验/医疗数据/正式数据.txt'


with open(triple_file_path, encoding="utf-8") as f:
    content = f.read()


lines = content.split('\n')

noun_set = set()
for line in lines:
    entities = line.split('|')
    head = entities[0]
    if entities[-1]=='':
        tail = entities[-2]
    else:
        tail = entities[-1]

    head_words_len = len(head.split(' '))
    tail_words_len = len(tail.split(' '))
    if head_words_len==1 and not head.__contains__('_'):
        noun_set.add(head)
    if tail_words_len ==1 and not tail.__contains__('_'):
        noun_set.add(tail)

print(len(noun_set))
print(noun_set)

for noun in noun_set:
    print(noun)