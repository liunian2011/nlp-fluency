# ------------------------------
# NgramsLanguageModel
# ------------------------------
import time
import jieba
from models_collect.models import NgramsLanguageModel

sentences = [
    "中国人的性情是总喜欢调和折中的，譬如你说，这屋子太暗，须在这里开一个窗，大家一定不允许的。但如果你主张拆掉屋顶他们就来调和，愿意开窗了。",
    "惟将终夜长开眼，报答平生未展眉",
    "我原以为，你身为汉朝老臣，来到阵前，面对两军将士，必有高论。没想到，竟说出如此粗鄙之语！",
    "人生当中成功只是一时的，失败却是主旋律，但是如何面对失败，却把人分成不同的样子，有的人会被失败击垮，有的人能够不断的爬起来继续向前，我想真正的成熟，应该不是追求完美，而是直面自己的缺憾，这才是生活的本质，罗曼罗兰说过，这个世界上只有一种真正的英雄主义，那就是认清生活的真相，并且仍然热爱它。难道向上攀爬的那条路不是比站在顶峰更让人热血澎湃吗？",
    "通过此次比赛不仅展示了室友们拼搏实干、奋勇争先、突破自我的“弄潮儿”风采，更加深了内部团队的凝聚力和集体荣誉感。未来，他们将继续努力，积极参与更多类似的体育赛事，为推动实验室体育文化的建设贡献力量。",
    "由各球类运动协会承办，开展篮球、足球、乒乓球、网球等项目的实验室内部联赛，以体育竞技形式促进实验室各中心间的交流联动，增强室友团队归属感、荣誉感。",
    "我在树上游泳。",
    "我在游泳池游泳。",
    "我游泳在游泳池。",
    "尤是为了,更佳大的,念,念,李是彼,更伟大的多,你只会用这种方法解决问题吗!",
    "当沉积学家研究湖泊沉积物的成分时，他们经常检查的一个关键方面是碳酸盐含量。碳酸盐主要以方解石和文石的形式存在，它们可以为了解湖泊的古环境条件提供有价值的见解。湖泊沉积物中碳酸盐含量的增加可以归因于各种因素，包括生物生产力、水化学和气候变化。\n\n在生物生产力增加的时期，藻类和水生植物等生物可以通过生物矿化过程促进碳酸盐含量的提高。该过程涉及生物从水中提取溶解的无机碳并将其转化为碳酸盐矿物，这是其生物功能的一部分。\n\n湖泊的水化学也在碳酸盐沉积中起着重要作用。溶解离子（如钙和碳酸氢盐）浓度较高的湖泊更有利于碳酸盐矿物的沉淀。这种沉淀可能进一步受到 pH 值和水温等因素的影响。\n\n气候条件也会影响湖泊沉积物的碳酸盐含量。例如，温度升高会加快湖泊流域岩石的化学风化速度，导致水中离子浓度增加，进而促进碳酸盐沉淀。相反，温度降低会减缓这些过程。\n\n总体而言，对湖泊沉积物中碳酸盐含量的研究为沉积学家提供了有关湖泊环境历史状况的重要信息，有助于重建过去的气候和生态情景。",
    "在沉积学中，湖泊沉积物的研究为了解过去的气候和环境条件提供了重要的见解。这项研究的一个关键方面是观察这些沉积物中的碳酸盐含量。有充分的证据表明，某些湖泊沉积物中的碳酸盐含量随着时间的推移而增加，了解推动这种增加的因素对于重建历史环境变化至关重要。\n\n碳酸盐含量的增加可能受到各种因素的影响，例如湖泊的水化学、生物活动和水动力条件。例如，在潮流强劲的湖泊中，水的搅动可以促进碳酸盐矿物的沉淀。此外，某些微生物群落的存在也在碳酸盐矿物的沉积中起着重要作用。这些群落可以形成层状凝块石结构，这些结构是有机沉积物，通常存在于具有中度至高度水搅动的浅水环境中。\n\n这些层状凝块石结构的形成是一个复杂的过程，包括微生物（如蓝藻）与周围沉积物和水化学的相互作用。微生物活动嵌入在沉积记录中，随着这些微生物的光合作用和代谢，它们会引起水化学变化，从而促进碳酸盐的沉淀。随着时间的推移，随着一层又一层的微生物垫和被捕获的沉积物积累，湖泊沉积物中的碳酸盐含量会增加。\n\n在沉积学研究中，检查湖泊沉积物的成分和结构（包括碳酸盐含量的变化）为湖泊的历史条件提供了宝贵的线索。通过研究模式和过程，例如层状凝块石的形成和潮汐流的影响，科学家可以更好地了解地质时间尺度上发生的环境动态。这些知识对于预测未来的环境变化和有效管理水资源至关重要。"
]

sentences = [
    """
    ## Unveiling the Complex Dynamics of Carbonate Sedimentation and Diagenesis: Insights and Implications\n\n### Introduction\n\nCarbonate sedimentology forms a crucial branch of geological sciences, focusing on the processes of formation, transport, alteration, and deposition of carbonate minerals. These processes play pivotal roles in shaping the Earth's surface and subsurface environments, influencing not only geomorphological formations but also the geochemical cycles. This article explores several facets of carbonate sedimentology, from the intricacies of carbonate detrital inputs in turbidite layers to the significance of caliche in shales, delivering a comprehensive overview of current understanding and emerging discoveries in the field. \n\n### Carbonate Detrital Input in Turbidite Layers\n\nTurbidite systems in marine settings often receive inputs of carbonate detrital materials sourced from nearby continental shelves or slopes. These carbonate particles are typically entrained in gravity-driven flows that deposit them in deep-water environments. The settling behavior of these particles can significantly influence the textural and compositional stratigraphy of turbidite deposits, where faster-settling coarse materials lead the flow, followed by finer carbonates, creating a graded bedding pattern essential in interpreting depositional environments.\n\n### Carbonate Dissolution and Re-precipitation in Calcrete Profiles\n\nA fascinating aspect of carbonate geochemistry occurs in calcrete profiles, where environmental conditions promote dissolution and re-precipitation of carbonates. In these profiles, carbonate materials originally deposited via detrital processes or direct precipitation undergo dissolution due to changes in pH, temperature, or ionic strength of percolating waters. This dissolved carbonate can later re-precipitate, forming discrete horizons of calcrete, a process that encapsulates vital information on past climatic conditions and hydrological dynamics.\n\n### Clasts Contacts with Carbonate Structures\n\nIn sedimentary environments, clasts (rock fragments) within a carbonate matrix often interact dynamically with surrounding carbonate structures. These contacts can influence the mechanical properties of the rock, where carbonate cementation around clast boundaries plays a critical role in enhancing rock durability and porosity, factors that are significantly important in reservoir rocks and aquifer systems.\n\n### Compaction Process in Carbonate Oozes\n\nDeep under the ocean, the accumulation of carbonate oozes is subject to increasing pressures and temperatures, leading to compaction. This compaction process reduces pore spaces, increases density, and eventually transforms the ooze into a more lithified state, influencing the acoustic properties and mechanical behavior of the resulting sedimentary rock, which are crucial for seismic exploration and geological modeling.\n\n### Carbonates Affected by Intense Compaction\n\nIntense compaction in carbonate sediments can lead to deformational features such as stylolites and pressure solution seams. These features not only record the stress history but also influence fluid flow through the carbonate sequences, impacting both diagenetic pathways and reservoir qualities.\n\n### Carbonates Affect Content of Phosphorus in Clays\n\nCarbonate interactions within clay matrices can significantly affect the geochemical environment, notably in the cycling of nutrients like phosphorus. Carbonates can bind with phosphate ions, thereby influencing the availability of phosphorus in marine sediments, which has implications for biogeochemical cycles and marine productivity.\n\n### Dissolution Affected Carbonate Allochems\n\nThe dissolution processes targeting carbonate allochems (grain constituents of carbonate rocks) can lead to enhanced secondary porosity, critical in petroleum geology for improving reservoir quality. The various types of allochems, including ooids, bioclasts, and peloids, each respond differently to dissolution processes depending on their chemical and physical properties.\n\n### Cementation Typical Temperatures Carbonate Diagenesis\n\nCementation in carbonate sediments, a key diagenetic pathway, occurs over a range of temperatures. Typically, carbonate cementation initiates at moderate temperatures (from about 30 to 50 degrees Celsius) encountered at shallow burial depths, progressively increasing with deeper burial and thermal maturity. Understanding these temperature regimes is essential for predicting carbonate rock properties and their evolution.\n\n### Caliche Increases Thickness Impregnated Shales\n\nCaliche development in shales can lead to an increase in thickness and density of these sedimentary layers. The carbonate content derived from caliche impregnation enhances the mechanical strength and reduces the permeability of the shale, which has significant implications for both conventional and unconventional hydrocarbon systems.\n\n### Conclusion\n\nThe multidimensional role of carbonates in sedimentological processes highlights their vast influence on Earth's systems, from surface dynamics to deep-sea deposits. Through understanding these processes, geoscientists can better predict the behavior of carbonates in geological time frames and their impact on ecological and economic systems. Continued research in carbonate sedimentology is essential in unravelling these complex interactions and fostering a deeper understanding of our planet's dynamic systems.
    """,
    """
    **Compaction and Diagenetic Processes in Carbonate Sedimentology: Insights into Structure Changes and Geochemical Influences**\n\nIn the expansive field of sedimentology, the study of carbonate sediments offers intriguing insights into the diagenetic processes that modify original depositional characteristics. From the intricate details of compaction fabric to the dynamics at the edges of intraclasts, carbonate systems reveal the complexities involved in sediment transformation from deposition through to lithification.\n\n**Carbonate Detrital Input in Turbidite Layers**\n\nCarbonates often contribute significantly to turbidite systems, where gravity-driven flows deposit sediments along slopes into deeper marine environments. The detrital carbonate material, primarily derived from shallow marine carbonate platforms, is transported into deeper zones. This results in layered deposits that occasionally exhibit preserved structures such as folded and crenulated layers, indicating post-depositional tectonic activity or slumping processes before final lithification.\n\n**Carbonate Dissolution and Re-precipitation in Calcrete Profiles**\n\nIn terrestrial settings, carbonate dissolution followed by re-precipitation often leads to the formation of calcrete profiles. These profiles typically evolve through leaching of carbonates by acidic soil waters combined with subsequent precipitation from carbonate-saturated solutions, resulting in a distinctive horizon that can significantly affect the soil fabric and hydrology. The process often results in a hardened layer which can be conducive to the preservation of underlying soft sediments.\n\n**Clasts Contacts with Carbonate Structures**\n\nThe contacts between clasts in carbonate sediments, such as those seen in conglomerates or breccias, often show evidences of diagenetic alterations. The edges of intraclasts might be smoothed or chemically welded to adjacent grains by microspar or spar cement, pointing towards a diagenetic history involving dissolution and precipitation of carbonate minerals.\n\n**Compaction Process in Carbonate Oozes**\n\nIn deep marine settings, the compaction of carbonate oozes is a prevalent process where the weight of overlying sediments compresses the underlying sediments. This results in a compaction fabric that's typically characterized by the alignment of platy minerals and deformation of more ductile components. Through this process, porosity is significantly reduced as the grain contacts increase and the matrix becomes denser.\n\n**Carbonates Affected by Intense Compaction**\n\nWhen subjected to intense compaction, carbonates may develop stylolites and other pressure-solution features. These features often run parallel to the maximum stress direction and can result in significant porosity reduction and formation of secondary voids filled later by blocky cement.\n\n**Carbonate Affect Content of Phosphorus in Clays**\n\nCarbonate presence in clay sediments can influence the geochemistry, notably the phosphorus content. Calcite, for example, can bind with phosphate ions, reducing their mobility and availability, which is a crucial aspect for nutrient cycling in both marine and lacustrine systems.\n\n**Dissolution Affected Carbonate Allochems**\n\nDissolution processes specifically affect carbonate allochems - fragments of pre-existing carbonate rocks - often leading to the development of secondary porosity which then becomes sites for further mineral precipitation during later diagenetic stages.\n\n**Cementation Typical Temperatures Carbonate Diagenesis**\n\nCementation in carbonate systems generally occurs at relatively low temperatures, typically around 30\u00b0C to 80\u00b0C. During this stage, calcium carbonate is precipitated into the pore spaces, often from marine or meteoric waters that become heated due to burial or hydrothermal activity, thus binding the sediment into rock.\n\n**Caliche Increases Thickness Impregnated Shales**\n\nIn arid and semi-arid regions, caliche formation can notably impact impregnated shales by increasing their thickness. This process typically happens when carbonate-rich waters infiltrate shale layers, depositing calcite and thus increasing the volume and reducing the permeability of these strata.\n\nIn summary, the study of carbonate sediments offers a window into the past geodynamic and geochemical conditions from which these rocks formed. Understanding these processes provides not only academic insights but also crucial information for industries such as hydrocarbon exploration where predicting porosity and permeability distributions is essential. Through examining structures such as compaction fabric and folded and crenulated layers, geoscientists continue to unravel the complex history recorded in carbonate rock formations.
    """
]

def ngram_model_test():
    print('=========ngram model===========')
    start_time = time.time()
    model = NgramsLanguageModel.from_pretrained("models_collect/thucnews_lm_model")
    print(f"Loading ngrams model cost {time.time() - start_time:.3f} seconds.")

    for s in sentences:
        ppl = model.perplexity(
            x=jieba.lcut(s),   # 经过切词的句子或段落
            verbose=False,     # 是否显示详细的probability，default=False
        )
        print(f"ppl: {ppl:.5f} # {s}")

    print(model.perplexity(jieba.lcut(sentences[-4]), verbose=True))


def bert_model_test():
    print('=========bert model===========')
    # bert or albert
    from models_collect.models import MaskedBert, MaskedAlbert
    start_time = time.time()
    #model = MaskedAlbert.from_pretrained("./models/albert_base_zh")
    model = MaskedBert.from_pretrained(
         path="models_collect/chinese_bert_wwm_ext_pytorch",
         device="cpu",  # 使用cpu或者cuda:0，default=cpu
         sentence_length=50,  # 长句做切句处理，段落会被切成最大不超过该变量的句子集，default=50
     )
    print(f"Loading bert model cost {time.time() - start_time:.3f} seconds.")

    for s in sentences:
         ppl = model.perplexity(
             x=" ".join(s),   # 每个字空格隔开或者输入一个list
             verbose=False,     # 是否显示详细的probability，default=False
             temperature=1.0,   # softmax的温度调节，default=1
             batch_size=100,    # 推理时的batch size，可根据cpu或gpu而定，default=100
         )
         print(f"ppl: {ppl:.5f} # {s}")

    print(model.perplexity(sentences[-4], verbose=True))


def gpt_model_test():
    print('=========gpt model===========')
    from models_collect.models import GPT
    start_time = time.time()
    model = GPT.from_pretrained(
         path="models_collect/chinese_gpt2_pytorch",
         device="cpu",
         sentence_length=50
     )
    print(f"Loading gpt model cost {time.time() - start_time:.3f} seconds.")

    for s in sentences:
         ppl = model.perplexity(
             x=" ".join(s),   # 每个字空格隔开或者输入一个list
             verbose=False,     # 是否显示详细的probability，default=False
             temperature=1.0,   # softmax的温度调节，default=1
             batch_size=100,    # 推理时的batch size，可根据cpu或gpu而定，default=100
         )
         print(f"ppl: {ppl:.5f} # {s}")

    print(model.perplexity(sentences[-4], verbose=True))


if __name__ == '__main__':
    ngram_model_test()
    bert_model_test()
    gpt_model_test()
    exit()