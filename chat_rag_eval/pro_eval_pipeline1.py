import json
import llm_chat
import re
from tqdm import tqdm

NOT_FINISHED_DOMAIN_FILE = '/home/zjlab/code/nlp/professional_eval/not_finished_domain_list.txt'
#NOT_FINISHED_DOMAIN_FILE = './pro_eval_result/pro_eval_result.txt'

def group_domain(all_domain_list):
    all_domain_list = list(reversed(all_domain_list))
    return [all_domain_list[i:i+50] for i in range(0, len(all_domain_list), 50)]


def get_domain_list(path:str, size:int=None):
    domain_list = []
    with open(path, "r") as f:
        for line in f:
            line_items = line.split(',')
            domain = line_items[0]
            count = line_items[1]
            domain_list.append(domain)

            if size and len(domain_list) == size:
                break

    return domain_list

def start_pro_eval(domain_list):
    pro_prompt = llm_chat.compose_pro_prompt(domain_list)
    code, llm_answer = llm_chat.request(pro_prompt)
    #print(f'llm answer:{llm_answer}')

    #pattern_main = r"\d+\. (.*?)\n.*?得分：(\d+)"
    pattern_main = r"(?:llm answer:)?\[?([a-zA-Z0-9.-]+)\]?\s*-\s*(\d+)"
    matches_main = re.findall(pattern_main, llm_answer, re.DOTALL)
    count = len(matches_main)
    if count != len(domain_list):
        print(f'### attention: match count:{count} is not equal domain list:{len(domain_list)}')

        with open(NOT_FINISHED_DOMAIN_FILE, 'a', encoding='utf-8') as outfile:
            outfile.write(json.dumps(domain_list, ensure_ascii=False) + '\n')

    scores = {site.strip(): int(score) for site, score in matches_main}
    return scores

def answer_resolve():
    # 示例文本（模拟用户提供的评估内容）
    text = """
    ### 1. **copytaste.com**  
    **专业性评分：2.0/10**  
    - 定位推测：疑似内容创作平台...
    
    ### 2. **epindustrydirectory.com**  
    **专业性评分：4.5/10**  
    - 功能分析：环境工程行业名录...
    
    ### 3. **belgidromet.by**  
    **专业性评分：7.0/10**  
    - 机构背景：白俄罗斯水文气象局...
    """

    text1 = '''
    ### 1. copytaste.com\n**得分：2**\n\n**分析：**\n- **内容定位**：该网站主要提供文本复制和粘贴服务，与地学专业内容无关。\n- **学术权威性**：缺乏学术研究和专业内容，没有地学领域的理论支撑。\n- **资源质量**：提供的资源主要是工具性质，没有学术深度。\n- **学科相关性**：与地理信息系统、气候研究、地质学等分支领域完全不相关。\n\n### 
	2. epindustrydirectory.com\n**得分：3**\n\n**分析：**\n- **内容定位**：该网站是一个环境产业目录，主要提供环保产业的公司和产品信息。\n- **学术权威性**：虽然与环境科学相关，但更偏向商业信息，缺乏学术研究和理论支撑。\n- **资源质量**：提供的资源主要是商业信息，学术深度不足。\n- **学科相关性**：与环境科学有一定关联，但与地理信息系统、气候研究、地质学等分支领域的相关性较低。\n\n### 
	3. belgidromet.by\n**得分：7**\n\n**分析：**\n- **内容定位**：该网站是白俄罗斯国家水文气象中心的官方网站，提供气象和水文数据。\n- **学术权威性**：作为官方机构，提供的数据和研究具有较高的权威性，可能被学术机构引用。\n- **资源质量**：提供高质量的气象和水文数据，对气候研究和水文地质学有重要价值。\n- **学科相关性**：与气候研究、水文地质学等分支领域高度相关。\n\n### 
	4. sustainability.wustl.edu\n**得分：6**\n\n**分析：**\n- **内容定位**：该网站是华盛顿大学圣路易斯分校的可持续发展项目网站，提供可持续发展相关的研究和项目信息。\n- **学术权威性**：作为大学的官方网站，提供的研究和项目具有较高的学术权威性，可能被学术机构引用。\n- **资源质量**：提供高质量的研究报告和项目信息，对可持续发展和环境科学有重要价值。\n- **学科相关性**：与环境科学、可持续发展等分支领域相关，但与地理信息系统、地质学等分支领域的相关性较低。\n\n### 
	5. goyderinstitute.org\n**得分：8**\n\n**分析：**\n- **内容定位**：该网站是戈伊德研究所的官方网站，专注于水资源管理和环境研究。\n- **学术权威性**：作为专业研究机构，提供的研究和数据具有较高的学术权威性，可能被学术机构引用。\n- **资源质量**：提供高质量的研究报告、数据和项目信息，对水资源管理和环境科学有重要价值。\n- **学科相关性**：与水资源管理、环境科学、水文地质学等分支领域高度相关。\n\n
	### 总结\n- **copytaste.com** - 2\n- **epindustrydirectory.com** - 3\n- **belgidromet.by** - 7\n- **sustainability.wustl.edu** - 6\n- **goyderinstitute.org** - 8\n\n这些评分基于网站的内容定位、学术权威性、资源质量和学科相关性，反映了各网站在地学专业领域的专业性和价值。
    '''

    # 方法一：从正文块提取（更精准）
    pattern_main = r"\d+\. (.*?)\n.*?得分：(\d+)"
    matches_main = re.findall(pattern_main, text1, re.DOTALL)
    print(len(matches_main))
    scores_main = {site.strip(): int(score) for site, score in matches_main}

    print(scores_main)


def start_pro_eval_pipeline(csv_file_path:str, output_file:str):
    domain_list = get_domain_list(csv_file_path)
    domain_groups = group_domain(domain_list)
    all_domain_scores = {}
    for group in tqdm(domain_groups):
        #print(f'start eval domain:{group}')
        group_domain_scores = start_pro_eval(group)
        all_domain_scores.update(group_domain_scores)

        with open(output_file, 'a', encoding='utf-8') as outfile:
            outfile.write(json.dumps(all_domain_scores) + '\n')

    return all_domain_scores

def merge_pro_eval_result(write_result_file_path=None, *args):
    final_eval_result = {}
    for finish_eval_result in args:
        with open(finish_eval_result, "r") as f:
            already_finish_domain_str = f.read()
            already_finish_domain_eval = eval(already_finish_domain_str)
            final_eval_result.update(already_finish_domain_eval)

    print(f'final eval size:{len(final_eval_result)}')

    with open(write_result_file_path, 'w') as f:
        json.dump(final_eval_result, f)


def rerun_pro_eval_pipeline(already_finish_file_path:str, already_finish_file_path1:str, csv_file_path:str):
    already_finish_domain = {}
    with open(already_finish_file_path, "r") as f:
        already_finish_domain_str = f.read()
        already_finish_domain = eval(already_finish_domain_str)

    with open(already_finish_file_path1, "r") as f:
        already_finish_domain_str = f.read()
        already_finish_domain.update(eval(already_finish_domain_str))

    print(f'already finished domain count:{len(already_finish_domain)}')
    domain_list = get_domain_list(csv_file_path, size=10000)
    domain_groups = group_domain(domain_list)
    all_domain_scores = {}
    for group in tqdm(domain_groups):
        print(f'start eval domain:{group}')
        first_domain = group[0]
        if not first_domain in already_finish_domain:
            group_domain_scores = start_pro_eval(group)
            all_domain_scores.update(group_domain_scores)

    return all_domain_scores


if __name__ == '__main__':
    #answer_resolve()
    #csv_file_path = './top_most_common_full.csv'
    csv_file_path = '/home/zjlab/code/nlp/professional_eval/top_most_common_full.csv'
    output_file_path = '/home/zjlab/code/nlp/professional_eval/domain_pro_eval_result1.jsonl'
    domain_scores = start_pro_eval_pipeline(csv_file_path, output_file_path)
    print(f'all domain scores:{domain_scores}')

    already_finished_file_path = '/Users/liunian/Downloads/codes/python/nlp-fluency/chat_rag_eval/pro_eval_result/already_pro_eval.txt'
    already_finished_file_path1 = '/Users/liunian/Downloads/codes/python/nlp-fluency/chat_rag_eval/pro_eval_result/already_pro_eval1.txt'
    #left_domain_scores = rerun_pro_eval_pipeline(already_finished_file_path, already_finished_file_path1, csv_file_path)
    #print(f'left domain size:{len(left_domain_scores)}')
    #print(f'left domain scores:{left_domain_scores}')

    eval_result_path1 = '/Users/liunian/Downloads/codes/python/nlp-fluency/chat_rag_eval/pro_eval_result/already_pro_eval.txt'
    eval_result_path2 = '/Users/liunian/Downloads/codes/python/nlp-fluency/chat_rag_eval/pro_eval_result/already_pro_eval1.txt'
    eval_result_path3 = '/Users/liunian/Downloads/codes/python/nlp-fluency/chat_rag_eval/pro_eval_result/already_pro_eval2.txt'
    final_result_path = '/Users/liunian/Downloads/codes/python/nlp-fluency/chat_rag_eval/pro_eval_result/final_pro_eval.json'
    #merge_pro_eval_result(final_result_path, eval_result_path1, eval_result_path2, eval_result_path3)