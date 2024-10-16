from ner_predict import file_resolve, rouge_cal

#no_diver_folder_path = "/Users/liunian/Downloads/personal/论文相关/实验/no diversity/"
#no_diver_file_paths = file_resolve.literal_folder_files(no_diver_folder_path)



diver_folder_path = "/Users/liunian/Downloads/personal/论文相关/实验/baseline1/"
diver_file_paths = file_resolve.literal_folder_files(diver_folder_path)

for index in range(0, 10):
    print('=='*20)
    print(f'index:{index}')
    #no_diver_file = no_diver_file_paths[index]
    diver_file = diver_file_paths[index]

    #file_name = no_diver_file.split('/')[-1]
    #print('no diver file name:{}'.format(file_name))
    diver_file_name = diver_file.split('/')[-1]
    print('diver file name:{}'.format(diver_file_name))

    #no_diver_output_article = file_resolve.file_content_reader(no_diver_file)
    #print('****区别于有扩展后的结果*****')
    input_prompt, diver_output_article = file_resolve.file_content_reader(diver_file)
    rouge_scores = rouge_cal.cal(input_prompt, diver_output_article)
    print(f'rouge scores:{rouge_scores}')



