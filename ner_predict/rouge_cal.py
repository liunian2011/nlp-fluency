from rouge import Rouge

def cal(paragram1, paragram2):
    rouge = Rouge()

    # 计算分数
    scores = rouge.get_scores(paragram1, paragram2)
    return scores