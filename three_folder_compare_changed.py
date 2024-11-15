from ner_predict import file_resolve, rouge_cal
from functools import cmp_to_key

no_diver_folder_path = "/Users/liunian/Downloads/personal/论文相关/实验/clean_kg_multiple_times/baseline1/"
no_diver_file_paths = file_resolve.literal_folder_files(no_diver_folder_path)
group0_no_diver_file_paths = no_diver_file_paths[:10]
group1_no_diver_file_paths = no_diver_file_paths[10:20]

farthest_folder_path = "/Users/liunian/Downloads/personal/论文相关/实验/clean_kg_multiple_times/ours/"
farthest_file_paths = file_resolve.literal_folder_files(farthest_folder_path)
group0_farthest_file_paths = farthest_file_paths[:10]
group1_farthest_file_paths = farthest_file_paths[10:20]

neareast_folder_path = "/Users/liunian/Downloads/personal/论文相关/实验/clean_kg_multiple_times/baseline2/"
neareast_file_paths = file_resolve.literal_folder_files(neareast_folder_path)
group0_neareast_file_paths = neareast_file_paths[:10]
group1_neareast_file_paths = neareast_file_paths[10:20]


def func(file_path1, file_path2):
    input_prompt1, output1, word_entity_set1 = file_resolve.file_content_reader(file_path1)
    input_prompt2, output2, word_entity_set2 = file_resolve.file_content_reader(file_path2)
    len1 = len(output1.split())
    len2 = len(output2.split())

    return len1 - len2

group0_no_diver_file_paths = sorted(group0_no_diver_file_paths, key=cmp_to_key(func))
group0_farthest_file_paths = sorted(group0_farthest_file_paths, key=cmp_to_key(func))
group0_neareast_file_paths = sorted(group0_neareast_file_paths, key=cmp_to_key(func))
group1_no_diver_file_paths = sorted(group1_no_diver_file_paths, key=cmp_to_key(func))
group1_farthest_file_paths = sorted(group1_farthest_file_paths, key=cmp_to_key(func))
group1_neareast_file_paths = sorted(group1_neareast_file_paths, key=cmp_to_key(func))
no_diver_file_paths = group0_no_diver_file_paths + group1_no_diver_file_paths
farthest_file_paths = group0_farthest_file_paths + group1_farthest_file_paths
neareast_file_paths = group0_neareast_file_paths + group1_neareast_file_paths

print('no diver sorted:{}'.format(no_diver_file_paths))
print('farthest sorted:{}'.format(farthest_file_paths))
print('nearest sorted:{}'.format(neareast_file_paths))


result_collect = {}

no_diver_total_words_set = set()
no_diver_expected_nount_set = set()
farthest_total_words_set = set()
farthest_expected_nount_set = set()
nearest_total_words_set = set()
nearest_expected_nount_set = set()

for index in range(0, 10):
    print('=='*20)
    print(f'index:{index}')
    result = {}

    no_diver_file = no_diver_file_paths[index]
    farthest_file = farthest_file_paths[index]
    nearest_file = neareast_file_paths[index]

    file_name = no_diver_file.split('/')[-1]
    print('no diver file name:{}'.format(file_name))
    diver_file_name = farthest_file.split('/')[-1]
    print('farthest diver file name:{}'.format(diver_file_name))
    nearest_file_name = nearest_file.split('/')[-1]
    print('neareast file name:{}'.format(nearest_file_name))

    from models_collect import perplexity_calc
    from ner_predict import pos_predict
    
    print('****没有拓展的结果*****')
    input_no_diver_prompt, no_diver_output_article, word_entity_set = file_resolve.file_content_reader(no_diver_file)
    percent1, total_words_set1, expected_nount_set1 = pos_predict.nount_statis(no_diver_output_article, word_entity_set)
    #ppl1 = perplexity_calc.ngram_model_perplexity(no_diver_output_article) #困惑度
    #print(f"困惑度: {ppl1:.5f}")
    #result['percent1'] = percent1
    #result['ppl1'] = ppl1
    no_diver_total_words_set = no_diver_total_words_set.union(total_words_set1)
    no_diver_expected_nount_set = no_diver_expected_nount_set.union(expected_nount_set1)
    print('no diver total len:{}'.format(len(no_diver_total_words_set)))
    print('no diver noun len:{}'.format(len(no_diver_expected_nount_set)))

    print('****拓展后最远端的结果*****')
    input_diver_prompt, diver_output_article, word_entity_set = file_resolve.file_content_reader(farthest_file)
    percent2,total_words_set2, expected_nount_set2 = pos_predict.nount_statis(diver_output_article, word_entity_set)
    #ppl2 = perplexity_calc.ngram_model_perplexity(diver_output_article) #困惑度
    #print(f"困惑度: {ppl2:.5f}")
    #result['percent2'] = percent2
    #result['ppl2'] = ppl2
    farthest_total_words_set = farthest_total_words_set.union(total_words_set2)
    farthest_expected_nount_set = farthest_expected_nount_set.union(expected_nount_set2)

    print('****拓展后最近邻的结果*****')
    nearest_input_prompt, nearest_output_article, word_entity_set = file_resolve.file_content_reader(nearest_file)
    percent3, total_words_set3, expected_nount_set3 = pos_predict.nount_statis(nearest_output_article, word_entity_set)
    #ppl3 = perplexity_calc.ngram_model_perplexity(nearest_output_article) #困惑度
    #print(f"困惑度: {ppl3:.5f}")
    #result['percent3'] = percent3
    #result['ppl3'] = ppl3
    nearest_total_words_set = nearest_total_words_set.union(total_words_set3)
    nearest_expected_nount_set = nearest_expected_nount_set.union(expected_nount_set3)

    rouge_scores = rouge_cal.cal(diver_output_article, no_diver_output_article)
    print(f'没有拓展与最远端的rouge-l scores:{rouge_scores}')
    result['rouge1'] = rouge_scores

    rouge_scores2 = rouge_cal.cal(nearest_output_article, no_diver_output_article)
    print(f'没有拓展与最近邻的rouge-l scores:{rouge_scores2}')
    result['rouge2'] = rouge_scores2

    rouge_scores3 = rouge_cal.cal(diver_output_article, nearest_output_article)
    print(f'最近邻到最远端的rouge-l scores:{rouge_scores3}')
    result['rouge3'] = rouge_scores3

    result_collect[index] = result



print('\n=======扩展平均值=========')
print('base 全部union单词数：{}'.format(len(no_diver_total_words_set)))
print('base 全部union名词数：{}'.format(len(no_diver_expected_nount_set)))
print('base 名词比例:{}'.format(len(no_diver_expected_nount_set) * 100/len(no_diver_total_words_set)))
print('farthest 全部union单词数：{}'.format(len(farthest_total_words_set)))
print('farthest 全部union名词数：{}'.format(len(farthest_expected_nount_set)))
print('farthest 名词比例:{}'.format(len(farthest_expected_nount_set) * 100/len(farthest_total_words_set)))
print('nearest 全部union单词数：{}'.format(len(nearest_total_words_set)))
print('nearest 全部union名词数：{}'.format(len(nearest_expected_nount_set)))
print('nearest 名词比例:{}'.format(len(nearest_expected_nount_set) * 100/len(nearest_total_words_set)))


group0_percent1_list = []
group0_percent2_list = []
group0_percent3_list = []
group0_ppl1_list = []
group0_ppl2_list = []
group0_ppl3_list = []
group0_rouge1_list = []
group0_rouge2_list = []
group0_rouge3_list = []
group1_percent1_list = []
group1_percent2_list = []
group1_percent3_list = []
group1_ppl1_list = []
group1_ppl2_list = []
group1_ppl3_list = []
group1_rouge1_list = []
group1_rouge2_list = []
group1_rouge3_list = []

for index, result in result_collect.items():
    if index//10 == 0:
        group0_percent1_list.append(result['percent1'])
        group0_percent2_list.append(result['percent2'])
        group0_percent3_list.append(result['percent3'])
        group0_ppl1_list.append(result['ppl1'])
        group0_ppl2_list.append(result['ppl2'])
        group0_ppl3_list.append(result['ppl3'])
        group0_rouge1_list.append(result['rouge1'])
        group0_rouge2_list.append(result['rouge2'])
        group0_rouge3_list.append(result['rouge3'])

    if index//10 == 1:
        group1_percent1_list.append(result['percent1'])
        group1_percent2_list.append(result['percent2'])
        group1_percent3_list.append(result['percent3'])
        group1_ppl1_list.append(result['ppl1'])
        group1_ppl2_list.append(result['ppl2'])
        group1_ppl3_list.append(result['ppl3'])
        group1_rouge1_list.append(result['rouge1'])
        group1_rouge2_list.append(result['rouge2'])
        group1_rouge3_list.append(result['rouge3'])


print('=======1-10组的平均值========')
print('****没有拓展的结果平均值****')
print('排除word entity后名词数比例:{}'.format(sum(group0_percent1_list)/len(group0_percent1_list)))
print('困惑度:{}'.format(sum(group0_ppl1_list)/len(group0_ppl1_list)))

print('****拓展后最远端的结果*****')
print('排除word entity后名词数比例:{}'.format(sum(group0_percent2_list)/len(group0_percent2_list)))
print('困惑度:{}'.format(sum(group0_ppl2_list)/len(group0_ppl2_list)))

print('****拓展后最近邻的结果*****')
print('排除word entity后名词数比例:{}'.format(sum(group0_percent3_list)/len(group0_percent3_list)))
print('困惑度:{}'.format(sum(group0_ppl3_list)/len(group0_ppl3_list)))

group0_rouge1_r_list = []
group0_rouge1_p_list = []
group0_rouge1_f_list = []
for rouge_l in group0_rouge1_list:
    group0_rouge1_r_list.append(rouge_l['r'])
    group0_rouge1_p_list.append(rouge_l['p'])
    group0_rouge1_f_list.append(rouge_l['f'])
print('*****没有拓展与最远端的rouge-l平均值，r:{}, p:{}, f:{}'.format(sum(group0_rouge1_r_list)/len(group0_rouge1_r_list),
                                                                     sum(group0_rouge1_p_list)/len(group0_rouge1_p_list),
                                                                     sum(group0_rouge1_f_list)/len(group0_rouge1_f_list)))

group0_rouge2_r_list = []
group0_rouge2_p_list = []
group0_rouge2_f_list = []
for rouge_l in group0_rouge2_list:
    group0_rouge2_r_list.append(rouge_l['r'])
    group0_rouge2_p_list.append(rouge_l['p'])
    group0_rouge2_f_list.append(rouge_l['f'])
print('*****没有拓展与最近邻的rouge-l平均值，r:{}, p:{}, f:{}'.format(sum(group0_rouge2_r_list)/len(group0_rouge2_r_list),
                                                                     sum(group0_rouge2_p_list)/len(group0_rouge2_p_list),
                                                                     sum(group0_rouge2_f_list)/len(group0_rouge2_f_list)))

group0_rouge3_r_list = []
group0_rouge3_p_list = []
group0_rouge3_f_list = []
for rouge_l in group0_rouge3_list:
    group0_rouge3_r_list.append(rouge_l['r'])
    group0_rouge3_p_list.append(rouge_l['p'])
    group0_rouge3_f_list.append(rouge_l['f'])
print('*****最近邻到最远端的rouge-l平均值，r:{}, p:{}, f:{}'.format(sum(group0_rouge3_r_list)/len(group0_rouge3_r_list),
                                                                   sum(group0_rouge3_p_list)/len(group0_rouge3_p_list),
                                                                   sum(group0_rouge3_f_list)/len(group0_rouge3_f_list)))


print('\n\n=======11-20组的平均值========')
print('****没有拓展的结果平均值****')
print('排除word entity后名词数比例:{}'.format(sum(group1_percent1_list)/len(group1_percent1_list)))
print('困惑度:{}'.format(sum(group1_ppl1_list)/len(group1_ppl1_list)))

print('****拓展后最远端的结果*****')
print('排除word entity后名词数比例:{}'.format(sum(group1_percent2_list)/len(group1_percent2_list)))
print('困惑度:{}'.format(sum(group1_ppl2_list)/len(group1_ppl2_list)))

print('****拓展后最近邻的结果*****')
print('排除word entity后名词数比例:{}'.format(sum(group1_percent3_list)/len(group1_percent3_list)))
print('困惑度:{}'.format(sum(group1_ppl3_list)/len(group1_ppl3_list)))


group1_rouge1_r_list = []
group1_rouge1_p_list = []
group1_rouge1_f_list = []
for rouge_l in group1_rouge1_list:
    group1_rouge1_r_list.append(rouge_l['r'])
    group1_rouge1_p_list.append(rouge_l['p'])
    group1_rouge1_f_list.append(rouge_l['f'])
print('*****没有拓展与最远端的rouge-l平均值，r:{}, p:{}, f:{}'.format(sum(group1_rouge1_r_list)/len(group1_rouge1_r_list),
                                                                     sum(group1_rouge1_p_list)/len(group1_rouge1_p_list),
                                                                     sum(group1_rouge1_f_list)/len(group1_rouge1_f_list)))

group1_rouge2_r_list = []
group1_rouge2_p_list = []
group1_rouge2_f_list = []
for rouge_l in group1_rouge2_list:
    group1_rouge2_r_list.append(rouge_l['r'])
    group1_rouge2_p_list.append(rouge_l['p'])
    group1_rouge2_f_list.append(rouge_l['f'])
print('*****没有拓展与最近邻的rouge-l平均值，r:{}, p:{}, f:{}'.format(sum(group1_rouge2_r_list)/len(group1_rouge2_r_list),
                                                                     sum(group1_rouge2_p_list)/len(group1_rouge2_p_list),
                                                                     sum(group1_rouge2_f_list)/len(group1_rouge2_f_list)))

group1_rouge3_r_list = []
group1_rouge3_p_list = []
group1_rouge3_f_list = []
for rouge_l in group1_rouge3_list:
    group1_rouge3_r_list.append(rouge_l['r'])
    group1_rouge3_p_list.append(rouge_l['p'])
    group1_rouge3_f_list.append(rouge_l['f'])
print('*****最近邻到最远端的rouge-l平均值，r:{}, p:{}, f:{}'.format(sum(group1_rouge3_r_list)/len(group1_rouge3_r_list),
                                                                   sum(group1_rouge3_p_list)/len(group1_rouge3_p_list),
                                                                   sum(group1_rouge3_f_list)/len(group1_rouge3_f_list)))
