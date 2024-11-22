import time
import jieba
from models import NgramsLanguageModel
from models import MaskedBert, MaskedAlbert

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
        sentence_length=100,  # 长句做切句处理，段落会被切成最大不超过该变量的句子集，default=50
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

    output_article_list = ["""
    ## Understanding the Relationship between Grainstone and Packstone in Sedimentary Layers\n\nIn the discipline of sedimentology, unraveling the intricacies of rock formation and layering provides invaluable insights into past depositional environments and geological processes. Among the different types of carbonate rocks, grainstone and packstone stand out due to their distinctive characteristics and the unique insights they offer into sedimentological and diagenetic histories. This article delves into the relationship between these two rock types, with a focus on the occurrence of grainstone within packstone units and the alternation of packstone with grainstone layers.""",
    """## The Relationship between Grainstone and Packstone Units in Sedimentology\n\nAs a geoscientist, understanding and characterizing distinctive rock formations is critical to properly unraveling the geological history of an area. This article aims to discuss two particular types of rock units in the discipline of sedimentology: grainstone and packstone, also highlighting the fact that grainstone is encountered within packstone units.\n\nSedimentologists often use the Dunham texture classification system to categorize carbonate sediments such as grainstone using factors like grain texture and the amount of interstitial material. Grainstone is defined by Robert L. Folk, a renowned sedimentologist, as a carbonate rock solely made of grains and is devoid of any mud. """,
    """my name is Jone.""",
    """good morning to you.""",
    """The primary composition of grainstones includes ooids, peloids, bioclasts, and intraclasts""",
    """SpaCy makes it extremely straightforward to build an NER system.""",
    """new to Medium, create a new account ,story available, account.""",
    """ times, quantities, monetary values, percentages, etc. In this blog.""",
    "通过此次比赛不仅展示了室友们拼搏实干、奋勇争先、突破自我的“弄潮儿”风采，更加深了内部团队的凝聚力和集体荣誉感。未来，他们将继续努力，积极参与更多类似的体育赛事，为推动实验室体育文化的建设贡献力量。",
    "由各球类运动协会承办，开展篮球、足球、乒乓球、网球等项目的实验室内部联赛，以体育竞技形式促进实验室各中心间的交流联动，增强室友团队归属感、荣誉感。",
    "我在树上游泳。",
    "尤是为了,更佳大的,念,念,李是彼,更伟大的多,你只会用这种方法解决问题吗!",
    "Understanding the Relationship between Grainstone and Packstone in Sedimentary Layers.",
    "In the discipline of sedimentology, unraveling the intricacies of rock formation and layering provides invaluable insights into past depositional environments and geological processes. ",
    "Among the different types of carbonate rocks, grainstone and packstone stand out due to their distinctive characteristics and the unique insights they offer into sedimentological and diagenetic histories. ",
    "This article delves into the relationship between these two rock types, with a focus on the occurrence of grainstone within packstone units and the alternation of packstone with grainstone layers.",
    "The Relationship between Grainstone and Packstone Units in Sedimentology.",
    "As a geoscientist, understanding and characterizing distinctive rock formations is critical to properly unraveling the geological history of an area. ",
    "This article aims to discuss two particular types of rock units in the discipline of sedimentology: grainstone and packstone, also highlighting the fact that grainstone is encountered within packstone units.",
    "Sedimentologists often use the Dunham texture classification system to categorize carbonate sediments such as grainstone using factors like grain texture and the amount of interstitial material.",
    "Grainstone is defined by Robert L. Folk, a renowned sedimentologist, as a carbonate rock solely made of grains and is devoid of any mud. ",
    "Under the Dunham classification (Dunham, 1962) system of limestones, a packstone is defined as a grain-supported carbonate rock that contains 1% or more mud-grade fraction. This definition has been clarified by Lokier and Al Junaibi (2016) as a carbonate-dominated lithology containing carbonate mud (<63 μm) in a fabric supported by a sand grade (63 μm to 2 mm) grain-size fraction and where less than 10% of the volume consists of grains >2 mm.",
    ]
    for output_article in output_article_list:
        ppl1 = ngram_model_perplexity(output_article)
        print(f"第一种模型困惑度: {ppl1:.5f},  {output_article}")

    for output_article in output_article_list:
        ppl2 = bert_model_perplexity(output_article)
        print(f"第二种模型困惑度: {ppl2:.5f},  {output_article}")