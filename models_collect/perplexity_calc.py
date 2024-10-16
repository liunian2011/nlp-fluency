import time
import jieba
from models_collect.models import NgramsLanguageModel
from models_collect.models import MaskedBert, MaskedAlbert

model = NgramsLanguageModel.from_pretrained("./models_collect/thucnews_lm_model")
#model = NgramsLanguageModel().from_pretrained("./thucnews_lm_model")

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
            x=" ".join(paragram),   # 每个字空格隔开或者输入一个list
            verbose=False,     # 是否显示详细的probability，default=False
            temperature=1.0,   # softmax的温度调节，default=1
            batch_size=100,    # 推理时的batch size，可根据cpu或gpu而定，default=100
        )
    return ppl

if __name__=='__main__':
    a = "我在游泳池游泳。"
    x = " ".join(a)
    print(x)

    output_article_list = ["""
    ### Sedimentological Evolution and Characteristics of Grainstone and Packstone Units Featuring Subrounded Clasts  Grainstones and packstones represent critical lithological components within the sedimentary record, providing valuable insights into past depositional environments, specifically in carbonate settings. This article seeks to expand the sedimentological understanding of these rock types, emphasizing the evolving nature of their depositional and diagenetic features, including the integration of subrounded clasts, uses of compaction curves, and the interrelationship between grainstone and packstone units. This comprehensive examination not only serves academic purposes but also aids in petroleum geology and reservoir characterization.#### Understanding Grainstone and Packstone  Grainstones are a type of carbonate rock primarily characterized by a granular texture with little to no mud matrix. Grainstones are typically formed in high-energy environments where water agitation is sufficient to winnow finer sediments, leaving behind a coarser framework of carbonate grains. These environments include shoals, beach faces, and channelized areas in reef complexes. The primary composition of grainstones includes ooids, peloids, bioclasts, and intraclasts, each indicating specific energy conditions and biological activities at the time of deposition.  Conversely, packstones are also carbonate rocks but differ from grainstones in that they contain a finer matrix that envelops the larger grains. The matrix in packstones is usually composed of micrite (microcrystalline calcite), which infills the spaces between the larger carbonate grains. This characteristic indicates somewhat lower energy conditions compared to those that form grainstone. Packstone typically forms in settings that are still energetic enough to support grain-supported fabrics but where there is also enough suspension for finer sediments to settle.  The presence of grainstone layers within packstone units is not uncommon and is indicative of fluctuating energy conditions within the depositional environment. These interfaces between grainstone and packstone can tell geoscientists much about the paleoenvironmental evolution of the area, including changes in water energy, sediment supply, and biological activity.  #### Role of Subrounded Clasts  Sediment clast shape, ranging from angular to rounded, reflects the history of physical weathering and transport. Subrounded clasts, which are typically observed in both grainstones and packstones, suggest a moderate degree of transport or abrasion. In carbonate environments, these subrounded clasts can be derived from bioclasts, ooids, or intraclasts, which have undergone some degree of rounding due to transportation by currents or waves before deposition.  The integration of subrounded clasts within grainstone and packstone units can indicate episodic high-energy events that have reworked earlier sediments, leading to partial rounding. These clasts not only contribute to the textural diversity of the deposits but also to the porosity and permeability characteristics of the rock, which are essential properties in hydrocarbon reservoirs.  #### Use of Compaction Curves in Sedimentology  Compaction curves are vital tools in sedimentology for understanding how sediment properties change under various loads. These curves help geoscientists predict the porosity and density of sedimentary rocks through geological time, from initial deposition to deep burial. Compaction affects all sediment types but is particularly critical in understanding carbonate sequences where both chemical and mechanical compaction play roles.  In the case of grainstones and packstones, compaction curves can help elucidate the extent to which original porosities have been reduced. For instance, the presence of grainstone layers within packstone units might suggest areas of reduced compaction relative to surrounding finer sediments due to the coarser, more rigid nature of grain-supported frameworks. Analyzing compaction trends across transitions from grainstone to packstone can, therefore, yield insights into the diagenetic history of the sequence and influence reservoir quality prediction in hydrocarbon basins.  #### Evolutionary Context  The sedimentary fabric of grainstone and packstone units evolves with changing depositional dynamics and subsequent diagenetic processes. These changes are often recorded in the shift from grain-supported to matrix-supported textures and vice versa, reflecting variations in energy levels and sedimentation rates. For example, a transition from packstone to grainstone within a stratigraphic sequence might indicate a shift towards higher energy conditions, potentially associated with a regression that exposes carbonate platforms to increased wave action.  Moreover, the chemical composition of the matrix and cement in these rocks evolves with continued burial and exposure to fluid migrations, which can alter original textures and porosities. Understanding these transformations is crucial for interpreting past environmental conditions and for predicting the behavior of carbonate reservoirs under production.  #### Conclusion  Grainstone and packstone units, with their variable content of subrounded clasts and distinct compaction histories, provide a rich tapestry for interpreting sedimentological histories. The study of these units, particularly the transitions between them, offers insights into past hydrodynamic conditions, sediment supply mechanisms, and diagenetic processes. As these carbonate rocks evolve with the geological and geochemical environments, they continue to serve as significant archives of Earth\u2019s past environments and as crucial reservoirs for hydrocarbon resources. The continuing study of their sedimentology not only enriches our understanding of geological processes but also enhances exploration and production strategies in the energy sector.
    """,
    """my name is Jone.""",
    """good morning to you.""",
    """The primary composition of grainstones includes ooids, peloids, bioclasts, and intraclasts"""

    ]
    for output_article in output_article_list:
        #ppl = ngram_model_perplexity(output_article)
        ppl = bert_model_perplexity(output_article)
        print(f"困惑度: {ppl:.5f}")
