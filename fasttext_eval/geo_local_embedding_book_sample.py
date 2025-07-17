from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# 加载本地模型（中文示例）
model = SentenceTransformer('BAAI/bge-small-en')  # BAAI/bge-m3 / m3e-base 等

geo_examples = []
non_geo_examples = []


with open('./datasource/book_pos_train_data_sample.txt', 'r', encoding='utf-8') as f:
    for line in f:
        pos_text = line.strip().replace('__label__0, ','').replace('__label__1, ','')
        geo_examples.append(pos_text)

with open('./datasource/book_neg_train_data_sample.txt', 'r', encoding='utf-8') as f:
    for line in f:
        neg_text = line.strip().replace('__label__0, ','').replace('__label__1, ','')
        non_geo_examples.append(neg_text)

with open('./datasource/fine_web_pos_train_data_sample.txt', 'r', encoding='utf-8') as f:
    for line in f:
        pos_text = line.strip().replace('__label__0, ','').replace('__label__1, ','')
        geo_examples.append(pos_text)

with open('./datasource/fine_web_neg_train_data_sample.txt', 'r', encoding='utf-8') as f:
    for line in f:
        neg_text = line.strip().replace('__label__0, ','').replace('__label__1, ','')
        non_geo_examples.append(neg_text)

with open('./datasource/web_search_pos_train_data_sample.txt', 'r', encoding='utf-8') as f:
    for line in f:
        pos_text = line.strip().replace('__label__0, ','').replace('__label__1, ','')
        geo_examples.append(pos_text)

with open('./datasource/just_moment_neg_train_data_sample.txt', 'r', encoding='utf-8') as f:
    for line in f:
        neg_text = line.strip().replace('__label__0, ','').replace('__label__1, ','')
        non_geo_examples.append(neg_text)

with open('./datasource/temporary_unavailable_neg_train_data_sample.txt', 'r', encoding='utf-8') as f:
    for line in f:
        neg_text = line.strip().replace('__label__0, ','').replace('__label__1, ','')
        non_geo_examples.append(neg_text)



print(f'geo example len:{len(geo_examples)}')
print(f'non geo example len:{len(non_geo_examples)}')

# 编码示例
geo_vectors = model.encode(geo_examples, normalize_embeddings=True)
non_geo_vectors = model.encode(non_geo_examples, normalize_embeddings=True)
np.save('./emb_data/geo_vectors.npy', geo_vectors)  # 保存单个数组
np.save('./emb_data/non_geo_vectors.npy', non_geo_vectors)  # 保存单个数组

geo_vectors = np.load('./emb_data/geo_vectors.npy')
non_geo_vectors = np.load('./emb_data/non_geo_vectors.npy')

# 维度自动取自向量 shape
dimension = geo_vectors.shape[1]

# 创建向量库
geo_index = faiss.IndexFlatIP(dimension)
non_geo_index = faiss.IndexFlatIP(dimension)

geo_index.add(geo_vectors.astype(np.float32))
non_geo_index.add(non_geo_vectors.astype(np.float32))

to_judge_text_list = [
    "The soil disturbance produced by a range of trenchless drainage tines, working under different soil conditions, is described and the effect of the different types of disturbance on subsequent drainage system performance considered. Few problems are likely to arise with trenchless tines working above critical depth. Below critical depth, impeding layers may develop alongside the pipe, reducing drainage efficiency in groundwater control situations, and lack of crack development above the pipe may impede water flow in top-water problem areas. Soil conditions most susceptible to damage are highlighted and methods suggested for avoiding, alleviating and minimizing potential problems. The study suggests trenchless drainage installation techniques can be used with confidence over a wide range of soil conditions, providing care is taken and in some cases, modifications made to the technique.",
    "The cost functions of water conveyance through lined open canals and underground pipelines have been developed. The cost of water conveyance through open lined canals and underground pipes can be reduced by using these methods in combination. A simple mathematical model has been developed to determine the breakeven point for underground pipelines and open canals which considers the costs of works, materials and a derived relationship between the embankment height and the cost of construction. It was concluded that in the conditions of Northern Nigeria, underground pipelines would be more economical than open lined canals when the embankment heights exceeded certain values. The results of the calculations are presented graphically by way of example.",
    "One option for reducing soil surface compaction resulting from the passage of lightly loaded vehicles is to reduce the inflation pressure of conventional tyres below the minimum currently recommended by tyre manufacturers. This paper describes an investigation of one potential problem, collapse of a tyre when subjected to large side forces, which might result from this approach.",
    "An automated measuring system was developed for monitoring the concentration of individual chemical ions in nutrient film solutions. This used ion-selective electrodes to measure pH, nitrate, potassium, calcium, sodium and chloride in solutions used for growing greenhouse tomatoes. The use of frequent and regular calibrations with two solutions which encompassed the concentrations existing in the nutrient solution enabled both short and long term drift of the electrodes to be accommodated, and electrode life to be extended. The accuracy of pH measurement was shown to be \u00b1 0\u00b74 pH units, while the concentrations of nitrate and potassium could be obtained with uncertainties of \u00b1 10 and \u00b1 20% respectively. The repeatability of measurements made on the same samples were within 10 p.p.m. or 0\u00b705 pH units, with the exception of a value of 27 p.p.m. obtained with calcium. The life of the glass and solid state electrodes used for pH, sodium and chloride exceeded 2 years, but that of the p.v.c. electrodes used for nitrate, potassium and calcium, were typically 4, 2 and less than one month, respectively.",
    "Experiments to investigate how blocking in cage wheels occurs showed three possible mechanisms. It was found that these mechanisms were strong functions of lug slip and lug spacing (the angular spacing between two consecutive lugs), in Bangkok clay soil at 49% (d.b.) moisture content. The blocking process observed at 100% slip was found to be the most likely mechanism by which cage wheels block in wet soil in practice.",
    "Variations in the performance characteristics of propeller fans of a range of sizes and from different manufacturers have been established. Desirable and undesirable features of performance are highlighted. Significant differences in performance have been found even between nominally similar fans. Fans of the same nominal diameter but of different manufacture vary widely in their efficiency and torque. It is concluded that it is not adequate to select a fan either solely on the basis of its nominal diameter or according to manufacturer. The merits of each fan should be evaluated in the proposed application to obtain the best overall performance.",
    "The oil-point is identified as a bulk property of rapeseeds under compression. It is the stage at which compression of the bed has sufficiently squeezed the individual seeds for oil to be forced from their interior to their surfaces. A 10 mm thick bed of rapeseeds was compressed and a method of measuring the oil-point bed strain and pressure is described. Experimental results are given along with correlations which interrelate bed strain (0\u00b7362\u20130\u00b7486), pressure (5\u00b772\u20139\u00b768 MPa), rate of deformation (5\u201319\u00b75 mm/min) and seed moisture content (0\u201312\u00b74% wet basis). Influence of seed moisture content on bed strain and pressure was much stronger than that of the rate of deformation.",
    "The dependence of methylene group deformational coordinates upon the puckering amplitude q has been analyzed for a set of ab initio geometries of the four-membered ring (CH2)3X. For small values of the puckering amplitude, the rocking and twisting deformational coordinates are proportional to q, whereas for q > 0.3 Å, the inclusion of a cubic term in q is necessary in order to describe the dependence of those deformational coordinates with the puckering amplitude. The wagging deformational coordinate shows a linear correlation with the square of q, although the effect is so weak that, for small variations in q, the wagging coordinate can be considered constant",
    "The solution and solid state structures of single stereoisomers of α-adducts of diethyl(1-cyclohexenyl)methyl-phosphonate and three aldehydes were determined by NMR spectroscopy and by X-ray diffraction. In both phases, the molecules exist in virtually the same conformation, involving gauche orientation of the PO3Et2 and the 2-hydroxy groups, and trans orientation of the former group and the R group of the aldehyde molecule. In the crystal, this conformation is retained in spite of the fact that PO⋯HO hydrogen bonding occurs inter- and not intramolecularly",
    "Lisinopril, N-N-[(s-1-carboxy-3-phenylpropyl]-l-lysyl-l-proline) (MK-521), is an inhibitor of angiotensin-converting enzyme and a new drug for the treatment of hypertension. 1H and 13C NMR studies have shown that the s-cis equilibrium about the amide bond is strongly dependent on the configuration of the chiral centres. Vicinal coupling constants of stereochemical significance were obtained in deuterated solvent using NMR techniques. Comparison with values calculated for lisinopril using potential energy calculations and NMR show that lisinopril exists in preferred optimum conformation in solution",

    "Dark-colored material (cryoconite) covering Himalayan glaciers has been reported to greatly accelerate glacier-melting by reducing surface albedo. Structure, formation, and the darkening process of the cryoconite on a Himalayan glacier were analyzed. The cryoconite was revealed to be a stromatolite-like algal mat, a product of microbial activity on the glacier. The granular algal mat contains filamentous blue-green algae (cyanobacteria) and bacteria, and grows on the ice by trapping mineral and organic particles. This structure seems to enable high algal production in nutrient poor glacial meltwater by gathering and keeping nutrient rich particles inside. The dark coloration of the mats promotes melt-hole formation on the ice (cryoconite holes), providing a semistagnant aquatic habitat for various algae and animals in the glacier. Optical and chemical analyses of the cryoconite strongly suggests that their high light- absorbency (dark coloration) is mainly due to dark-colored humic substances, residues from bacterial decomposition of the algal products and other organic matter. Our results strongly suggest that biological activity on the glacier substantially affects the albedo of the glacier surface. The structure of the algal mat seems to be important in the glacier ecosystem and biological process affecting glacier albedo",
    "Between October 1993 and May 1998 we measured snow depth (cm), density (g cm−3), and resistance (kg × cm) adjacent to 53 Peary caribou (Rangifer tarandus pearyi) and 134 muskox (Ovibos moschatus) feeding craters on Banks Island in the Canadian High Arctic. Measurements were taken in early (26 October-18 November), mid- (12 February–1 March), and late-winter (20 April–4 May). Concurrently, we recorded snow depth, density, and resistance along fixed transects in the four habitats used by foraging caribou and muskoxen. Caribou craters were found predominantly (94%) in upland habitats; upland barren (UB), hummock tundra (HT), and stony barren (SB). Caribou abandoned craters in the more rolling UB and HT when snow was shallower, less dense, and less resistant than average snow conditions in these habitats; in most cases the differences were significant (P < 0.01). In SB, the habitat with the shallowest snow, caribou cratered through snow conditions similar to the average found in this habitat. During winter 1994–95, when snow depth, density, and resistance was greatest, we located caribou craters only in SB. Muskox craters were found almost exclusively (96%) in wet sedge meadows (WSM); the habitat with deepest snow. Muskoxen abandoned crater sites when snow depth, density, and resistance was less (P < 0.01) than average conditions in WSM, regardless of animal density. Muskoxen in low density areas were faced with deeper snow, particularly in late- winter, and they abandoned crater sites when snow depth was greater (P < 0.004) than muskoxen in high density areas. During winter 1994–95, muskox cratered through deeper, denser, and more resistant snow than during winter 1997–98 when snow conditions were the least severe of the study. We discuss our results in relation to the population dynamics of Peary caribou and muskoxen on Banks Island.",
    "Dramatic retreat of ice shelves in Antarctica in recent years, linked to climatic warming, is well documented. In contrast, the ice shelves of the Russian Arctic remain largely unstudied. A time-series analysis of the largest ice shelf in the Russian High Arctic, the Matusevich Ice Shelf, Severnaya Zemlya, was undertaken for the period 1931 to 1994 using georeferenced Landsat satellite imagery and published maps. The positions of three major ice margins in 1931, 1955, 1962, 1973, 1985, 1988, and 1994 are compared. The floating margin of the ice shelf underwent at least two cycles of retreat followed by periods of advance between 1931 and 1994. These periodic calving events produce tabular icebergs up to several kilometers in length. This process is typical of floating ice shelves in Antarctica and Greenland, whereas grounded ice margins in, for example, Svalbard, produce smaller icebergs much more frequently. There is little evidence that these calving events are related to climate change.Landsat imagery is also used to track the movement of 50 icebergs identified in 1985 imagery of Matusevich Fjord. Iceberg release from the fjord between 1985 and 1994 was extremely slow, with 48 of the icebergs observed in 1985 still trapped in the fjord in 1994. The icebergs from Matusevich Ice Shelf remain in the fjord for many years, probably due to either grounding on submarine moraines or trapping by shore-fast sea ice. Much of the sediment load of the trapped icebergs may be melted out and deposited beneath the sea-ice cover of Matusevich Fjord, and little iceberg-rafted debris of heterogeneous grain size will be transported to the Laptev Sea.",
    "We here describe glacial geomorphology that sheds light on ice-dynamic conditions during the Noble Inlet advance, a glacial event involving northward ice flow across Hudson Strait and large-magnitude meltwater drainage across Meta Incognita Peninsula at around 8.9 to 8.4 14C kyr BR Through airphoto interpretation and field inspection of key sites we mapped the glacial geomorphology of interior Meta Incognita Peninsula, the postulated terminal zone for northward expansion of ice from Quebec-Labrador during the Noble Inlet advance. A 170-km-long zone of glaciofluvial canyons, washing zones and boulder deltas was traced from Shaftesbury Inlet to Henderson Inlet. This zone reflects initial drainage across Meta Incognita Peninsula at >520 m elevation, followed by ice marginal drainage at progressively lower levels along the southern slope of the peninsula. The ice marginal outline required to explain the glaciofluvial zone is compatible with northward-trending striae previously reported from the southern coast of Meta Incognita Peninsula. A very large flux of meltwater across Meta Incognita Peninsula probably occurred because eastward supraglacial drainage on ice in Hudson Strait was temporarily impeded and steered northward by a raised ice surface level in outer Hudson Strait, induced by an enhanced outflow of ice from Ungava Bay.",
    "AbstractWe used fossil beetles recovered from three peatlands of the James Bay area (Radisson, northern Quebec, Canada), and the mutual climatic range (MCR) method, to produce a quantitative reconstruction of summer temperatures during the last 5000 yr. Our main objective was to test the hypothesis that a significant climatic cooling episode occurred during the late Holocene epoch, leading to the opening up of the boreal forest, and to the progressive replacement of black spruce (Picea mariana) forests by jack pine (Pinus banksiana) stands. Beetle assemblages in the Radisson area were very stable during the late Holocene epoch. We used a total of 22 beetle species to conduct the MCR analyses. Reconstructed mean July temperatures ranged from 14.5 to 17.5°C, which is close to the present-day (A.D. 1977–1996) temperature range found in the Radisson area. The general stability of beetle assemblages, and the MCR analyses, suggest that there was no major change in July temperatures during the last 5000 yr in the Radisson area. This study provides no evidence that the progressive replacement of black spruce forests by jack pine stands in the Radisson area during the last 2700 yr can be explained by a longterm climatic cooling episode affecting the postfire regeneration potential of trees. Consequently, an alternative hypothesis (more frequent fires favoring jack pine) should be seriously considered to explain the late Holocene changes in the forest environment of the Radisson area.",
    "AbstractNumerous cold-induced changes in physiology limit the capacity of northern conifers to photosynthesize during winter. Studies of red spruce (Picea rubens Sarg.) have shown that rates of field photosynthesis (Pfield) and laboratory measurements of photosynthetic capacity (Pmax) generally parallel seasonal ambient temperature trends; carbon exchange decreases in the fall, remains negative or close to zero for much of the winter, and increases in the spring. However, increases in Pfield, Pmax, and foliar carbohydrate concentrations can occur during winter thaws. Thaw-induced increases in photosynthesis are probably not the result of increased stomatal conductance, but may result from other changes in physiology associated with thaw-induced improvements in water relations. In addition to increased photosynthesis, red spruce also decrease in cold hardiness during thaws. The cooccurrence of thaw-induced changes in photosynthesis and cold hardiness raises questions regarding their adaptive significance, particularly in the context of potential climate change. Red spruce may face a tradeoff between potentially beneficial increases in carbon capture and potentially detrimental reductions in cold tolerance. The physiological consequence(s) of this tradeoff may depend on the number and duration of thaws, as well as ambient temperature trends following thaw. Pollution-induced reductions in cold tolerance, and the low genetic variability of red spruce, may also influence the net outcome of thaw-induced changes in physiology.",
    "AbstractLow temperatures and high sunlight, factors that are characteristic of high elevations, may lead to the low-temperature photoinhibition of photosynthesis (LTP). Exposure and photosynthetic responses to low temperature and high sunlight were compared among current-year seedlings of the conifers Abies lasiocarpa and Picea engelmannii, and the snowbank perennials Caltha leptosepala and Erythronium grandiflorum, in the alpine treeline ecotone. The ratio of silhouette (sunlit) to total leaf area of whole plants was greatest in A. lasiocarpa (0.33), 25% lower in P. engelmannii (0.25), and at least 36% lower in the snowbank perennials than for A. lasiocarpa. This indicated less structural avoidance of high sunlight in the conifer seedlings, particularly A. lasiocarpa. CO2 assimilation (Asat) in A. lasiocarpa was reduced 40% due to frosts, high sunlight (22%), and their combination (90%). Asat was much less affected by frosts and high sunlight in P. engelmannii and especially the perennials. Following frost and high sunlight exposure, diurnal reductions in maximum photosynthetic efficiency, indicated by the chlorophyll fluorescence ratio Fv/Fm, corresponded to species differences in Asat. A substantially greater degree of slowly-reversible, or irreversible LTP (44% reduction in predawn Fv/Fm) occurred in the microclimate above snow for A. lasiocarpa compared to the other species. It appears that a higher resistance to LTP in the perennials may contribute to their greater occurrence in microsites with lower temperatures and higher sunlight compared to the conifer seedlings.",
    "AbstractPinus albicaulis (whitebark pine) is an important tree species in subalpine forests of the Northern Rocky Mountains. Populations have been declining at unprecedented rates due to the introduction of an exotic pathogen and fire suppression. We initiated this study to evaluate historical trends in Pinus albicaulis abundance along with associated subalpine conifers within a small biogeographically disjunct mountain range. The central objective was to estimate historic trends in subalpine forest composition and structure at the species and community scales. Reconstruction of forest stands reveals an 85% increase in tree volume among all species since the 1870s. Pinus albicaulis has historically dominated most stands associated with Abies bifolia (subalpine fir) and Picea engelmannii (Engelmann spruce) but dominance has shifted to these late-seral species for most of the study area since the early 1900s. We estimate, that since 1753, nearly 50% of the study area has shifted to later successional stages while only 3% has receded to earlier stages. We discuss the implications for Pinus albicaulis and suggest that careful reintroduction of fire can aid in the maintenance of ecological integrity at the community and landscape scales.",
    "In the forest-alpine ecotone at Stillberg (Dischmatal/Switzerland) the morphology of humus forms and the spatial variability of organic layer properties were investigated. At northeast-exposed gully sites mulls with high acidity in the A-horizon occur. They were classified after the Canadian classification of humus forms as Rhizomulls. Mors occur on ridges and on their east- and north-exposed aspects. They can be differentiated by the ratio between the thickness of the F-horizon and the combined thickness of the F- and H-horizon. The relative thickness of the F-horizon increases significantly in the order: east aspects < ridges < north aspect. The humus forms of the east aspects and the ridges were classified as Humimors and those of the north aspects as Hemimors. The Canadian classification was suitable to describe the properties of the horizons and to classify the humus forms. The results of a grid sampling at the study sites and the computation of nonergodic correlograms show that the spatial variability of organic-layer thickness, bulk density, and moisture is high (CV around 50%), with a pronounced small-scale heterogeneity (range usually below 2 m and more than 50% variability occurs within 0.3 m). Only 33% of the variance of organic-layer thickness were explained by site and vegetation structure, but in spite of the low percentage both proved to be a significant factor. In the forest-alpine tundra ecotone about 30 to 35 soil samples per site are needed for a reliable estimation of the mean of the organic-layer thickness.",
    "AbstractIn the antarctic summer of 1996, permafrost-affected cold soils close to the Australian Casey Station in the Windmill Islands region (Wilkes Land) were investigated to determine in what way the thermal and nutrient regimes in the antarctic soils are related to microbial biomass and vegetation patterns. The soils are characterized by a high content of coarse mineral particles and total organic carbon (TOC) and a low C/N ratio (mean 11). Despite the low pH values (mean 4.0) the soils are rich in nutrients due to an input from seabirds (existing or abandoned nesting sites) and an eolian distribution of fine-grained soil material in the landscape. Vegetation influences TOC storage and the cation exchange capacity in the uppermost soil horizons, whereas total N and most nutrient levels are not affected by the vegetation, but by seabird droppings. The present nutrient level does not affect plant adaptation, because the K, Mg, and P contents are often extraordinarily high. This suggests that nutrient supply is not a limiting factor, whereas microclimate effects, such as moisture availability and ground-level wind speed, have a primary influence on plant growth. Soil-surface temperature measurements indicate a strong variability in microclimate due to small-scale variations in geomorphological surface features. Bacteria are found in all soil horizons, but not algae and yeast. Soil microbial counts are weakly correlated to the C/N ratios and soil surface temperatures. High TOC and clay contents probably improve the soil water-holding capacity and TOC contributes to the microbial food supply. The investigated microbial parameters are weakly correlated to the present vegetation carpet, the lowest counts are found in the soils with scattered or no vegetation cover.",

]

with open('./test_data_sample/fine_web_pos_train_data_sample.txt', 'r', encoding='utf-8') as f:
    for line in f:
        text = line.strip().replace('__label__0, ', '').replace('__label__1, ', '')
        to_judge_text_list.append(text)

with open('./test_data_sample/fine_web_neg_train_data_sample.txt', 'r', encoding='utf-8') as f:
    for line in f:
        text = line.strip().replace('__label__0, ', '').replace('__label__1, ', '')
        to_judge_text_list.append(text)

with open('./test_data_sample/web_search_pos_test_data_sample.txt', 'r', encoding='utf-8') as f:
    for line in f:
        text = line.strip().replace('__label__0, ', '').replace('__label__1, ', '')
        to_judge_text_list.append(text)

with open('./test_data_sample/temporary_unavailable_neg_test_data_sample.txt', 'r', encoding='utf-8') as f:
    for line in f:
        text = line.strip().replace('__label__0, ', '').replace('__label__1, ', '')
        to_judge_text_list.append(text)

with open('./test_data_sample/just_moment_neg_test_data_sample.txt', 'r', encoding='utf-8') as f:
    for line in f:
        text = line.strip().replace('__label__0, ', '').replace('__label__1, ', '')
        to_judge_text_list.append(text)

i = 1
for text in to_judge_text_list:
    # 编码并归一化
    text_vector = model.encode([text], normalize_embeddings=True).astype(np.float32)

    # 相似度搜索
    _, geo_sim = geo_index.search(text_vector, 1)
    _, non_geo_sim = non_geo_index.search(text_vector, 1)

    if geo_sim[0][0] > non_geo_sim[0][0]:
        print(f"{i}: 判断结果：地学. Geo similarity: {geo_sim[0][0]:.4f}, Non-geo similarity: {non_geo_sim[0][0]:.4f}")
    else:
        print(f"{i}: 判断结果：非地学. Geo similarity: {geo_sim[0][0]:.4f}, Non-geo similarity: {non_geo_sim[0][0]:.4f}")

    i += 1
