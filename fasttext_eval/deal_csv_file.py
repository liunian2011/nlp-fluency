import csv

file_path = '/Users/liunian/Downloads/文档/临时文档/wiki_neg_train_data.csv'
med_file = '/Users/liunian/Downloads/文档/临时文档/PubMedQA.csv'
computer_file = '/Users/liunian/Downloads/文档/临时文档/computer_science_wikipedia_articles.csv'
med_file_2 = '/Users/liunian/Downloads/文档/临时文档/medical_cases_train.csv'


def write_med_neg_data():
    with open(med_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        with open('second_train_data/med_and_computer_neg_train_data.txt', 'a', encoding='utf-8') as f:
            for row in reader:
                #print(row[''], row['text'])  # 通过列名访问
                wiki_text = row['input']

                wiki_text_format = ' '.join([line.strip() for line in wiki_text.split('\n') if not line.__contains__('Options: No, Maybe, Yes')])
                f.write('__label__0, ' + wiki_text_format + '\n')


def write_med_file2_neg_data():
    with open(med_file_2, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        with open('second_train_data/med_and_computer_neg_train_data.txt', 'a', encoding='utf-8') as f:
            for row in reader:
                #print(row[''], row['text'])  # 通过列名访问
                wiki_text = row['transcription']

                wiki_text_format = ' '.join([line.strip() for line in wiki_text.split('\n')])
                f.write('__label__0, ' + wiki_text_format + '\n')


def write_computer_neg_data():
    with open(computer_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        with open('second_train_data/med_and_computer_neg_train_data.txt', 'a', encoding='utf-8') as f:
            for row in reader:
                #print(row[''], row['text'])  # 通过列名访问
                wiki_text = row['text']

                wiki_text_format = ' '.join([line.strip() for line in wiki_text.split('\n')])
                f.write('__label__0, ' + wiki_text_format + '\n')




def main():
    #write_med_neg_data()
    #write_computer_neg_data()
    write_med_file2_neg_data()

if __name__ == "__main__":
    main()