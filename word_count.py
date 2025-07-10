
from collections import Counter
#import jieba

def main():
    with open('/Users/liunian/Downloads/personal/论文相关/实验/abstract.txt', encoding="utf-8") as f:
        lines = f.readlines()

    word_dict = {}
    all_words = []

    for line in lines:
        words = line.split()  # 将行按空格分割成单词列表
        for word in words:
            length = len(word)  # 获取单词长度
            all_words.append(word)
            if length not in word_dict:
                word_dict[length] = []  # 如果长度不在字典中，则创建一个空列表
            word_dict[length].append(word)  # 将单词添加到对应长度的列表中

    for length, words in word_dict.items():
        print("单词长度为 {} 的单词有：{}个".format(length, len(words)))

    wordcount = Counter(all_words)
    print('词频前10位单词:{}'.format(wordcount.most_common(10)))

if __name__=='__main__':
    main()
