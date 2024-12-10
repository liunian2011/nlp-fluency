import time
import jieba
from models import NgramsLanguageModel
from models import MaskedBert, MaskedAlbert
from models import GPT
#model = NgramsLanguageModel.from_pretrained("./models_collect/thucnews_lm_model")
model = NgramsLanguageModel.from_pretrained("./thucnews_lm_model")

def ngram_model_perplexity(paragram):
    ppl = model.perplexity(
            x=jieba.lcut(paragram),   # 经过切词的句子或段落
            verbose=False,     # 是否显示详细的probability，default=False
        )

    return ppl


def bert_model_perplexity(paragram):
    model = MaskedBert.from_pretrained(
        path="./chinese_bert_wwm_ext_pytorch",
        device="cpu",  # 使用cpu或者cuda:0，default=cpu
        sentence_length=500,  # 长句做切句处理，段落会被切成最大不超过该变量的句子集，default=50
    )

    ppl = model.perplexity(
            x=jieba.lcut(paragram),   # 每个字空格隔开或者输入一个list
            verbose=False,     # 是否显示详细的probability，default=False
            temperature=1.0,   # softmax的温度调节，default=1
            batch_size=100,    # 推理时的batch size，可根据cpu或gpu而定，default=100
        )
    return ppl


def gpt_model_perplexity(paragram):
    model = GPT.from_pretrained(
        path="./chinese_gpt2_pytorch",
        device="cpu",
        sentence_length=500
    )

    ppl = model.perplexity(
            x=jieba.lcut(paragram),   # 每个字空格隔开或者输入一个list
            verbose=False,     # 是否显示详细的probability，default=False
            temperature=1.0,   # softmax的温度调节，default=1
            batch_size=100,    # 推理时的batch size，可根据cpu或gpu而定，default=100
    )
    return ppl



if __name__=='__main__':
    s = "The primary composition of grainstones includes ooids, peloids, bioclasts, and intraclasts"

    output_article_list = [
    """Title: Integrative Roles of Fish Social Behavior and Clinical Attributes in Understanding Cellular Functions\n\nAbstract: \nThis article explores the intricate relationship between unique social behaviors exhibited by fish, their consequential clinical attributes, and the specific cellular functions they influence. The study analyzes various social interactions among fish species and their implications on health and disease at the cellular level. The review aims to elucidate potential benefits and mechanisms through which understanding fish behavior can contribute toward medical science, particularly in terms of cellular processes like cell communication, immunity, and regeneration.\n\nIntroduction:\nFish are a diverse group of organisms that exhibit a wide range of social behaviors, from solitary existences to complex interactions within shoals and schools. These behaviors are not only fundamental for their survival but also have profound implications on their physiological health and overall wellbeing. The social structure can influence clinical attributes which, in turn, affect cellular functions crucial for health and disease. Understanding these interactions opens up novel approaches to human medical research, especially in terms of preventive and therapeutic strategies derived from bio-inspiration and comparative medicine.\n\nFish Social Behavior and its Impact:\nFish, as social animals, communicate and interact within their environments in ways that are critical for their survival, such as foraging, predator avoidance, and reproduction. Social hierarchies and behaviors such as aggression, schooling, and mating rituals can affect their stress levels, immune responses, and other physiological aspects. Studies have shown that social isolation or overcrowded environments can lead to higher cortisol levels, indicative of stress, which directly impacts fish immune systems at the cellular level.\n\nLink Between Clinical Attributes and Cell Function:\nClinical attributes in fish, such as stress responses, growth rates, and susceptibility to diseases, are deeply intertwined with cellular functionality. For instance, long periods of stress not only affect the neuroendocrine system but also impact cellular immunity. Lymphocytes and macrophages show altered activities under stress, leading to modified responses to pathogens and diseases. Additionally, fish schooling behavior has been linked with synchronized cell processes, including metabolism and gene expression, due to the need for homogeneity within groups.\n\nCellular Functions Influenced by Fish Behavior:\nOne of the key cellular functions influenced by fish behavior is cell communication, essential for maintaining homeostasis and responding to environmental stimuli. The neuro-immunological interface in fish showcases how stress and social interactions can modulate neurotransmitter levels and cytokine production, thereby influencing cellular communication pathways. Moreover, the phenomenon of cellular regeneration in fish, especially noticeable in species like zebrafish which can regenerate their hearts, is highly influenced by both intrinsic (genetic) and extrinsic (environmental) factors, including social interactions.\n\nNovel Medical Insights Gained from Fish Studies:\nUnderstanding fish social behavior and its impacts on cell function has myriad applications in medical science. For instance, by studying the mechanisms of cellular regeneration in zebrafish, researchers can explore new avenues for tissue regeneration in humans. The social dependency of certain metabolic processes in fish can also enlighten pathways to investigate metabolic disorders in humans. Furthermore, the stress and immune responses modulated by social interactions in fish provide a comparative basis to study similar phenomena in human psycho-neuroimmunology.\n\nConclusion:\nIn conclusion, fish and their complex social behaviors offer a unique window into the interconnected relationship between behavior, clinical attributes, and cellular function. By exploring these links, medical researchers can not only gain deeper insights into cellular processes but also explore potential therapeutic and preventive measures derived from these studies. Future research should focus on more in-depth molecular mechanisms and potential applications of these discoveries in human health sciences, paving the way for innovative cross-disciplinary medical advancements. The study of fish, therefore, becomes not just an exploration of ecological interest but a promising frontier in medical science.\n\nReferences:\n[1] Scholarly articles and research studies on fish behavior and its physiological impacts.\n[2] Clinical studies on stress, immunity, and cellular functions in marine organisms.\n[3] Reviews on comparative medicine and bio-inspired medical approaches.""",
    "Title: Integrative Roles of Fish Social Behavior and Clinical Attributes in Understanding Cellular Functions",
        """Abstract:\nThis article explores the intricate relationship between unique social behaviors exhibited by fish, their consequential clinical attributes, and the specific cellular functions they influence. The study analyzes various social interactions among fish species and their implications on health and disease at the cellular level. The review aims to elucidate potential benefits and mechanisms through which understanding fish behavior can contribute toward medical science, particularly in terms of cellular processes like cell communication, immunity, and regeneration.""",
        """Introduction:\nFish are a diverse group of organisms that exhibit a wide range of social behaviors, from solitary existences to complex interactions within shoals and schools. These behaviors are not only fundamental for their survival but also have profound implications on their physiological health and overall wellbeing. The social structure can influence clinical attributes which, in turn, affect cellular functions crucial for health and disease. Understanding these interactions opens up novel approaches to human medical research, especially in terms of preventive and therapeutic strategies derived from bio-inspiration and comparative medicine.""",
        """Fish Social Behavior and its Impact:\nFish, as social animals, communicate and interact within their environments in ways that are critical for their survival, such as foraging, predator avoidance, and reproduction. Social hierarchies and behaviors such as aggression, schooling, and mating rituals can affect their stress levels, immune responses, and other physiological aspects. Studies have shown that social isolation or overcrowded environments can lead to higher cortisol levels, indicative of stress, which directly impacts fish immune systems at the cellular level.""",
        """Link Between Clinical Attributes and Cell Function:\nClinical attributes in fish, such as stress responses, growth rates, and susceptibility to diseases, are deeply intertwined with cellular functionality. For instance, long periods of stress not only affect the neuroendocrine system but also impact cellular immunity. Lymphocytes and macrophages show altered activities under stress, leading to modified responses to pathogens and diseases. Additionally, fish schooling behavior has been linked with synchronized cell processes, including metabolism and gene expression, due to the need for homogeneity within groups.""",
        """Cellular Functions Influenced by Fish Behavior:\nOne of the key cellular functions influenced by fish behavior is cell communication, essential for maintaining homeostasis and responding to environmental stimuli. The neuro-immunological interface in fish showcases how stress and social interactions can modulate neurotransmitter levels and cytokine production, thereby influencing cellular communication pathways. Moreover, the phenomenon of cellular regeneration in fish, especially noticeable in species like zebrafish which can regenerate their hearts, is highly influenced by both intrinsic (genetic) and extrinsic (environmental) factors, including social interactions.""",
        """Novel Medical Insights Gained from Fish Studies:\nUnderstanding fish social behavior and its impacts on cell function has myriad applications in medical science. For instance, by studying the mechanisms of cellular regeneration in zebrafish, researchers can explore new avenues for tissue regeneration in humans. The social dependency of certain metabolic processes in fish can also enlighten pathways to investigate metabolic disorders in humans. Furthermore, the stress and immune responses modulated by social interactions in fish provide a comparative basis to study similar phenomena in human psycho-neuroimmunology.""",
        """Conclusion:\nIn conclusion, fish and their complex social behaviors offer a unique window into the interconnected relationship between behavior, clinical attributes, and cellular function. By exploring these links, medical researchers can not only gain deeper insights into cellular processes but also explore potential therapeutic and preventive measures derived from these studies. Future research should focus on more in-depth molecular mechanisms and potential applications of these discoveries in human health sciences, paving the way for innovative cross-disciplinary medical advancements. The study of fish, therefore, becomes not just an exploration of ecological interest but a promising frontier in medical science.""",
        """References:
\n[1] Scholarly articles and research studies on fish behavior and its physiological impacts.
\n[2] Clinical studies on stress, immunity, and cellular functions in marine organisms.
\n[3] Reviews on comparative medicine and bio-inspired medical approaches.""",
    ]
    for output_article in output_article_list:
        ppl1 = ngram_model_perplexity(output_article)
        print(f"第一种模型困惑度: {ppl1:.5f},  {output_article}")

    for output_article in output_article_list:
        ppl2 = bert_model_perplexity(output_article)
        print(f"第二种模型困惑度: {ppl2:.5f},  {output_article}")

    for output_article in output_article_list:
        ppl3 = gpt_model_perplexity(output_article)
        print(f"第三种模型困惑度: {ppl3:.5f},  {output_article}")