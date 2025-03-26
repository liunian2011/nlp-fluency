import fasttext

def train(): # 训练模型
    model = fasttext.train_supervised(input="./train/train.data", lr=0.1, dim=100,
                                      epoch=5, word_ngrams=2, loss='softmax')
    model.save_model("model_file.bin")

def model_test(): # 预测
    classifier = fasttext.load_model("model_file.bin")
    result = classifier.test("./train/train.data")
    print("准确率:", result)
    with open('./train/test.data', encoding='utf-8') as fp:
        for line in fp.readlines():
            line = line.strip()
            if line == '':
                continue
            print(line, classifier.predict([line])[0][0][0])


def skipgram_test():
    # Skipgram model
    model = fasttext.train_unsupervised(input='./train/train.data', model='skipgram')
    print(model.words)

    # CBOW model
    model = fasttext.train_unsupervised('./train/train.data', model='cbow')
    print(model.words)

if __name__ == '__main__':
    #train()
    #model_test()
    skipgram_test()