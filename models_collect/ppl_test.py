import numpy as np
from collections import defaultdict

class NGramModel:
    def __init__(self, n):
        self.n = n
        self.ngrams = defaultdict(lambda: defaultdict(int))
        self.vocab_size = 0

    def train(self, text):
        words = text.split()
        self.vocab_size = len(set(words))
        for i in range(len(words) - self.n + 1):
            ngram = tuple(words[i:i + self.n])
            prefix = ngram[:-1]
            self.ngrams[prefix][ngram[-1]] += 1

    def get_prob(self, prefix, word):
        if prefix not in self.ngrams:
            return 1 / self.vocab_size
        total = sum(self.ngrams[prefix].values())
        return self.ngrams[prefix][word] / total

    def perplexity(self, text):
        words = text.split()
        N = len(words)
        prob = 1.0
        for i in range(len(words) - self.n + 1):
            ngram = tuple(words[i:i + self.n])
            prefix = ngram[:-1]
            prob *= self.get_prob(prefix, ngram[-1])
        return prob**(-1/N)

# 使用示例
text = "the cat sat on the mat"
model = NGramModel(n=2)
model.train(text)
perplexity = model.perplexity(text)
print(f"困惑度1: {perplexity}")

text = "my name is Jone"
model = NGramModel(n=2)
model.train(text)
perplexity = model.perplexity(text)
print(f"困惑度2: {perplexity}")

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
                       ]
for output_article in output_article_list:
    model = NGramModel(n=2)
    model.train(text)
    perplexity = model.perplexity(text)
    print(f"困惑度: {perplexity} {output_article}")