from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = 'sk-Avu1NSpZvuMReDJJ27BcC6Ff4b024e1c83Ef4cBa52D69e80'
os.environ["OPENAI_BASE_URL"] = "https://openai.sohoyo.io/v1"

# 你的大段文本
big_text = """
# HEALTH PROMOTION AND AGING NUTRITION 

Nancy Chapman, R.D., M.P.H.. N. Chapman Associates, Inc.. Ann Sorenson, M.S., Ph.D.. Health Scientist Administrator, NIA \*The trick is to live to be loo. Very few people die after that." 

George Burns 

Aging is inevitable. Health promotion, including good nutrition, can slow the rate ot degeneration. and foster the independence and well-being of older individuals. For years, health promotion Health professionals and adults over 65 simply accepted. activities targeted only younger adults.. the high rate of chronic disease and the concomitant physical and mental impairments.. Health-promoting dietary recommendations were generally viewed as useless.. However, a preponderance of evidence now suggests many potential benefits of good nutrition for older persons: 

Life expectancy after age 65 has increased in part because of an abundant tood suppiy, wnic   
1) has eliminated most nutritional deficiencies (l). Reducing body weight and excess intakes of sodium, sugars, fats, and cholesterol can lower the.   
2) risk of developing hypertension, diabetes, and heart disease for many individuals and improve. the management of these diseases for older as well as younger individuals (2). Nutritious diets that protect physical and mental health help older people to work longer and.   
3) lead independent lives (1). Maintaining a reasonable weight, exercising regularly, and selecting a proper diet may retard.   
4) the aging process and delay certain debilitating conditions common in old age (i.e., osterporosis, hypertension, dementia, and diabetes) (3). Preventing malnutrition can reduce the need for recurrent hospitalizations and prevent the   
5) occurrence of complicating conditions, thereby, lowering medical costs (3). Selecting the best, most economical foods to meet nutritional needs and using appropriate   
6) nutrition programs can maximize limited financial resources and permit independent living for. the older population. Correcting poor diets for healthy older persons eliminates the need for and avoids the hazards   
7 ) of hish doses of expensive dietary supplements (4).   
To design appropriate nutrition strategies for those over 65, decision-makers need to 1) consiaer   
the heterogeneous characteristics of the elderly population, 2) differentiate age-related changes   
from effects of degenerative diseases, and 3) recognize the limitations of the current research. This paper discusses these factors as well as other related areas -- problems in determining.   
nutritional status and nutrient requirements of older persons, emerging research issues, and the Several links between nutrition and other health.   
effectiveness of current nutrition interventions..   
promotion areas are identified. The issues identified in this paper, though not exhaustive,.   
provide a starting point for developing the strategies that will address nutrition concerns in the   
radidly srowing, aging population in the U.s.. 

## CHARACTERISTICS OF OLDER PERSONS 

Older persons, generally defined as individuals over the age of 65, represent a very diverse group The sex and racial composition of specific cohorts change as the subgroup ages beyond 80 years. The physical and mental capabilities of elders within and among older subgroups also vary widely: thus the potential benefits of nutrition therapies are not uniform. Attempting to foster independence and well-being in this heterogeneous population will require that policy makers and health care professionals examine the distinct characteristics of two to three age strata over 65 hofore develonins broad interventions or formulating policies. 

The varlations in physiological, physical, and mental functions are greater among older persons. than among any younger cohort. This heterogeneity reflects, in part, the diversity in lifestyles, economic and social conditions, food supply, culture, education, and exposure to other. environmental factors experienced daring their growing and maturing years. Genetics, of course, also plays a major role in the rate of functional loss in various organs and one's susceptibility. to chronic diseases (such as cancer, coronary heart disease, diabetes, and osteoporosis). A later section describes more fully the differences in age-related functional changes and occurrence of chronic diseases. 

Many psychosocial factors affect the food habits and nutritional status of the old. Depression, loss of self-esteem, loss of spouse, inability to live independently, and loss of a sense of.   
purpose and motivation adversely affect nutritional status' by decreasing appetite and Interest in.   
eating and food preparation (5). Place of residence and economic status can determine access to.   
food sources and health care services.. 

In 198s, the majority of those over 65 were white, non-institutionalized women, either living in a family setting (67x) or living alone (30x). Few (5x) lived in nursing homes, and most of these were over 85. After age 80 to 85, males and blacks are more likely to survive. Although many. older persons maintain households, many need help with personal care and food purchasing and preparation. Older persons tend to reside more frequently in central cities, small towns, and rural areas where access to social and health services, nutrition programs, and food stores may be. Iimited. Because older residents in urban and rural areas are often less educated and poorer than suburban residents, their risk of nutritional problems increases (6). The dietary patterns of. these rural residents include large amounts of salty snacks, heavy sweets-sugar desserts, and high fat meat (7). 

Older persons are more likely than younger adults to be poor or live on fixed incomes. Federal. programs (Medicare, Medicaid, Social Security) have slowed the onset of poverty for some, but more than two out of every five of those over 65 are poor or economically vulnerable (8). Those over 85, nonwhites, women, and persons living alone experience the highest rates of poverty (8, 9, 10). As inflation increases, those living on fixed or low incomes find that a larger portion of their income is spent for food. Ihe recent low inflation rate has partly eased this burden. Participation in the food stamp program, the nutrition program for seniors, and the commodity supplemental food program has also Improved older persons access to food: but these safety-net programs provide protection for only a small proportion of poor older persons (8). 

The cultural and social influences on food habits are also important to consider in planning. nutrltion strategies (10, 11, 12, 13). Davis and Randall (14) described trends in family structures and gender roles, in social integration, in employment opportunities, in education and in economic stability that affected the food habits and food choices of three subgroups of the. population who would be over 65 by the year 2000. For example, individuals born between 1910-1930. experienced food shortages: often lived close to their food supply: and were less educated. They may require different food offerings and educational tools than persons born between 1940-1950. Nutritional problems of the older cohort who ate more complex carbohydrates and less fat may differ from the younger cohort who were exposed to more processed foods with more fats and simple sugars. A lower fertility.rate among those born in l910-30 could limit family support as they age compared to those born ten to twenty years later. 

## Nutritional status 

The nutritional status of the older persons often reflects lifetime nutrient intakes and food behaviors, as well as age-related conditions and socioeconomic determinants.. Experlence with chronic degenerative diseases and conditions, drug regimens, drug and diet interactions, and. should be taken not to confuse functional status also influences cross-sectional data showing secular trends in dietary patterns with. heal th. To interpret the nutrition data from surveys, caution longitudinal data showing within person changes over time (15, 16, 17).. 

The most recent survey data from NhAnes II showed older adults selecting most frequently the followipg foods from each specific group: whole and low fat milk and cheese (milk group), grapefruits and melon (fruit group), potatoes and tomatoes (vegetables), bread, biscuits, and muffins (breads and cereals group). and ground beef (meat group) (18). The 1977-78 National Food Consumption Survey data showed that one-third of older adults used whole grain breads and that older persons were the highest users of eggs, skim milk, vegetables, fruits, soups and lowest users of soft drinks (19). 

National survey data (20) also show that estimated food energy intakes decline with age; the lowest mean intakes are for those 75 years and over (about 1850 kcal for males and 1400 kcal for females)..   
Adults generally gain weight until age 50: then, relative weights decline. The variance for energy.   
Intakes of those over 65 years of age is great, due to the small numbers in this subset..   
Assessments of caloric intake adequacy require data on body size and physical activiry. 

For some older persons, having been obese and consuming inappropriate levels of sodium and perhaps, calcium, protein, and fat earlier in life may have raised their chances of developing hypertension, cardiovascular disease (cvp), diabetes, and cancer. Dietary cholesterol Intakes for many over 65 (means are 461 mg for males, 316 mg for females) remain above recommended levels for lowering the risk of cvD. 

Intakes of most nutrients except vitamin C and vitamin A also appear to decrease with age. consumed by most older adults provided adequate levels of protein, preformed niacin, vitamin C,. Intakes of calcium iron, vitamin A, thiamin, riboflavin, and potassium for. folate, and phosphorus.   
most adults either approached or failed to meet the RDAs. In general, biochemical or clinical markers of deficiency were rarely found (<5x on average) in the older persons (21). 0f concern are older women who have high rates of bone fractures and related lower intakes of calcium and vitamin n-rich milk products (22, 23). 

Usaee of dietary supplements,  drugs, and alcohol 

An appropriate assessment of nutritional status cannot overlook the population's use or aietaly   
supplements, drugs, and alcohol. In turn, additional data on the nutritional status and supplement use by older persons. [The   
requirements may stimulate promotion of more dietary   
1da1 tareets of health fraud are discussed later.] 

Usage of supplements by older persons has increased from an estimated 1 percent in 19/s (z4) tu estimates of 40 percent natlonwide in 1980 (25). Analysis of national survey results suggests that those who use supplements may not be the Individuals most in need of them (4, 22, 26, 27).. Approximately half of those who use supplemental vitamins take multivitamins, in particular vitamin C and E (22, 28, 29). Dietary supplementation does not appear to routinely Improve nutritional It may even lead to nutrient imbalances, toxicities and/or interactions. status for older persons.. ...+h druos. esneciaily if megadoses (10 times the RDAs) are taken (4, 22, 30).. 

Although older Americans constitute about 10 percent of the population, they use apout z> pete.   
of all prescription drugs. This is not surprising since many chronic diseases are managed with.   
prescription drugs. Over half of older people take at least one medication daily and many take six The drug-drug and drug-nutrient interactions may affect body.   
or more a day for multiple diseases..   
camnnsirion. nutrient balance, or appetite, as discussed later (31).. 

Excessive alcohol intakes may also advance nutrient deficiencies (i.e., thiamin, niacin and otner water soluble nutrients), may damage organs and tissues important to nutrient utilization, and may depress appetite and the desire and ability to eat. The result can be poor nutritional status. Older persons have a lower tolerance for alcohol which becomes more concentrated as body water declines with age. Approximately 30% percent of those 65 and over consume alcohol on a regular basis (at least one time/week). About 15% of this cohort are considered light drinkers, 11% moderate drinkers, and 6% heavy (32). If the older persons' drinking habits are reflective of the adult population, then the 5 percent of the population which drinks most heavily, accounts for about 50 percent of the total alcohol consumption. Since alcohol is a risk factor for diabetes, rtoncinn. cancer. and liver disease, moderation of intake is advisable at any age. 

FFFECTS OF AGING AND CHRONIC DEGENERATIVE DISEASES 

Normal aging changes body composition, physical performance, organ system function and conuitsou occur at different rates in different.   
all individuals if they live long enough; however, changes. Even within the same individual, degeneration of various tissues and organs occurs at   
people. There are some 60- or 70-year-olds with organ function tests equivalent to   
different rates (33). Conversely, there are some younger individuals with physiological.   
someone 30 or 40 years younger.. narities in the range of an average elder (34).. 

## Age-related changes 

Physiological changes in many organ systems naturally accompany the aging process. Examples or. various age-related conditions that can affect the nutritional status of older persons include. sensory impairments, altered endocrine, gastrointestinal, and cardiovascular functions, and changes + h o renal and musculo-skeletal systems . ( 35) . 

During the aging process, changes in dentation and in the oral cavity (recession ot gums ana decreased salivary flow) can occur. Ihese conditions are exacerbated by some medications. Dental caries, periodontal disease, and trauma have led to the loss of natural teeth in approximately 29%. of those over 65 and 50z of individuals over 80. Being toothless or having ill-fitting dentures. can reduce chewing ability and raise the risk of choking. Well-fitting dentures are essential for. chewing high fiber, nutritionally-rich foods, such as raw fruits and vegetables, whole grain products, and nuts. The use of fluoridated water, fluoride treatments, regular dental care, and improved diet may decrease dental problems for the next generation of older persons. Less is known. 2bout prevention of periodontal disease, especially the potential role of nutrients (e.g., sucrose, fluoride, and calcium). (These issues will be considered in background papers prepared for other workins groups.} 

Decreased organ or tissue function can be accelerated by anorexia or autrient imbalances or deficiencies related to chronic illness, use of therapeutic regimens, or lack of proper medical Manv age-related conditions affect the older person's ability to ingest, absorb and utilize discussed under ntial nu emerging research issues. el1 as obtain and prepare food. Additional age-related changes are 

Chronic disease-related changes 

The prevalence of hypertension, diabetes, Cvd, cancer, osteoporosis, and arthritis increases with age. Four out of five older persons have at least one chronic condition and many have multiple problems. diseases. Many of these conditions require special diets, drugs, or other therapeutic regimens. Obesity, affecting approximately 28x of older persons, is also related to many chronic. that could further compromise nutritional status.. 

Mortality and morbidity rates for diseases differ by gender and race.   
This may reflect genetic differences, lifestyle habits, or differences in access to health care.   
nutrition strategies, special diet-related problems should be considered by race and sex. Briefly. Therefore, when planning 1982-84 data (36, 37) show that reported rates of cvD, stroke, and cancer are higher for males than females, with the highest incidence among black males. Hypertension and arthritis rates are highest among females, especially blacks. The prevalence of diabetes is comparable for white males and females, but about 50x higher for black females than for white females (36, 38). This may be due to the high prevalence of obesity among older black females (37). 

Usteoporosis. generally affects more women than men, measured by the higher proportion (four to one) of bone fractures in women than men, and more whites than blacks (36) and Mexican Americans (39) . Higher bone density initially explains part of these differences; but the potential for. obesity may explain the racial difference and should also be explored. Associated immobility. handicaps an older person's ability to purchase and prepare food and thus limits food selections. and independent living. Similarly, resorption of the residual alveolar ridge (bony ridge in which. teeth are positioned) reduces the retention of dentures (40, 41) and mav limi+ fas? ..l..... 

## MAJOR POLICY ISSUES 

Ine previous descriptions of the socioeconomic factors, nutritional status, usage of drugs, alcohol and dietary supplements, and specific health problems, serve as background to the major policy This section highlights the following areas to explore in developing nutrition policies for the aging: 

1) Nutrition surveillance and monitorlng   
2) Emerging research issues.   
3) Nutrition services for older persons.   
4) Technology advances.   
5) Food assistance and nutrition programs   
6) Nutrition education and information 

inis listing does not order the importance of these issues, but rather the logical progression from information gathering to dissemination. For the public, the value of research is best realized when people learn the programs. consensus on the findings through the mass media or nutrition education 

## Nutriticn surveillance 

severai national and state surveys have been conducted on, or include, the older population.. surveys are designed to determine the amounts and types of foods consumed, the nutrient content of intakes, the existence of clinical signs of nutritional problems, and the hematological or. biochemical evidence of sub- clinical nutritional deficiencies. A limited number of. cross-sectional population studies supplement these national data; however, there is almost as much variability between individuals within an age group as between group averages of age decade groups (42).. The NIA Baltimore Longitudinal Study of Aging provides the only data to assess individual variations in intake, biochemical, anthropometric, and functional parameters.. 

many surveys lack documentation of dietary supplement usage. There has aiso been minimal nutrition surveillance and monitoring among institutionalized elders (those in ambulatory care centers and Iong-term care facilities), homebound, or homeless older persons. Likewise, little is known about older persons in defined ethnic groups such as Asian Americans, native Americans, and, until recently, Hispanics. Nutritional data on subgroups of older persons, such as those over 80 years of age, in whom malnutrition may be more common, are also missing.   
It is often difficult to compare nutritional surveys which include or focus on older persons because of differences in dietary methodology and standards (43). to aate, the nutrition surveys of older persons in the U.s. have been very limited in scope, have.   
frequently excluded the oldest old age groups, and have used varying standards of comparison in.   
presenting the frequencies of nutrient deficiencies (33). In the NHAnEs I and NhANEs II, adults.   
ages 65-74 years comprised approximately 6-8x of the sample. The UsDA Nationwide Food Consumption.   
Surveys (NFcs) also collects data on the food intakes of individuals ages 65-74. renreeonr.   
approximately 10x of the 1977-78 NFcs. No information on individuals older than 75 was gathered   
from either survey. rsons Comparisons of independently-living and institutionalized older persons.   
The nutritional status of long-term institutionalized and independently living older persors needs   
to be compared., Older persons in institutions are usually subject to fixed meals which.may not.   
accommodate their individual food preferences, though they often adhere to specified dietary Often, individuals in these settings lose interest in foods and eat sparingly:d.A..   
national survey of geriatric patients in institutions in the U.s. and of homebound individuals. .1h Instructive. Major areas to research include (44):   
WouL Food-energy and nutrient needs of sedentary and bedridden patients:   
1. The means.to best carry out nutritional screening and assessment of geriatric patients in   
2. The interpretation of clinical. anthropometric, hematological, and biochemical indices of   
3. nutritional status in chronically sick older patients, with or without age-related conditions (i.e., skin disease, renal dysfunction, anemia, and muscle wasting): The responsiveness of patients showing one or more indices of malnutrition to nutrient 4. Acceptable values for nutritional status indicators in nursing home patlents. 5 Methods of nutritional assessmeu..   
Dietary intakes documented later in life may not correlate with anthropometric, biochemical   
measurements, or clinical evaluations taken at the same time.   
closely describe a myriad of historical experlences and long-term food intakes. Longitudinal   
studies provide information that begins to explain possible relationships of intakes to other To standardize the results of geriatric nutritional studies, a core set of   
assessment tools needs to be identified and then used routinely (as a minimum) for all studies or   
surveys. ards. food frequencies 

Nutrient and energy intakes are determined using 24-hour recalls, food records, tooa lieyu and dietary histories. Interpretation of the histories requires standards. Appropriate standards for various age-subgroups of older persons do not exist. Comparisons are made to nutritional data from NHanes I and II and the 1977-78 NFcs despite limitations identlfied earlier. Reliability of Information in these dietary histories has also been questioned. Memory, vision, and hearing may decline with age, making it more difficult to recall accurately foods previously eaten. -+hriris may impede record keeping. nd hv aeing. For 

aItnI rements (e.g., height, weight, and skinfolds) are aftectea oy example, height decreases over time due to changes in the integrity of the skeletal system.. Measurements are often hard to obtain because of poor posture, or the inability of the older persons to stand erect unassisted. For these individuals, recumbent length, total arm length, knee height and arm span have been proposed as alternative methods to estimate stature (45, 46). More. research on the reliability of these measurements is needed before they can be recommended as. rautine clinical practice. calibrated 

Actual weight is less difficult to measure than height. For ambulatory people, a caliviac. For the non-ambulatory, wheel chair or bed balance beam scales are   
balance beam scale is used. J. Befory weighing, the patient's hydration state should be noted, as severe edema or   
dehydration can distort actual weight and anthropometric measurements (47). Skinfold measurements   
are also affected by the age-related decrease in lean body mass that results in a larger proportion Fat stores are also redistributed truncally. Changes in skin   
Af hndv weight as fat.. In+ernretation of skinfold measurements (33)..   
compressibility ana e.   
Biochemical parameters may be affected by an age-related decline in renal function, by shifts in   
fluid balance, by drug-drug or drug-nutrient interactions, by the long-term effects of chronic or For example, low serum albumin levels often indicate poor.   
nutritional status; however, kidney and liver disease, cancer, congestive heart failure, and other   
diseases (common among older persons) cause marked reductions in serum albumin (37)..   
these conditions must be done before low serum albumin concentration is associated with. For accurate results, biochemical analysis should use several blood and void.   
malnutrition alone.   
camnles (48, 49, 50). .hueical examinations The most effective clinical methods of nutritional assessment are based on pnysica.   
and observation, and reflect long-term nutritional status. Clinical evaluations must be highly scrutinized because of the potential for human error, especially when large numbers are evaluated. For example, several age-related changes in clinical appearance--dry skin, sensory loss, and sparse. hair -- may appear to be representative of one or more nutrient deficiencies (47). Other   
discussed later.   
limitations in assessment methodology are 

Nutrition and aging research focuses on two general areas: issues related to interaction of diet and aging functions (i.e., physiological, psychological, sociological) and dietary relationships with pathological conditions common to old age. More specifically, much of the current research is directed toward the following topics: 

1) Ihe effects of aging on nutrient digestion, absorption and utilization and the relationship between these effects and nutrient requirements..   
2) The role of dietary restriction in modifying age-related physiological changes or the role of diet in treating conditions associated with changes in immune and endocrine functions and changes in body composition..   
3) The influence or effects of neurological, environmental, and dietary factors on senile dementia or sensory deficits in older persons..   
4 ) The influence of physiological, behavioral, and environmental factors (e.g., sensory function, dental status, culture, cognition, and economics) on the quality and quantity of food eaten by older individuals, and on the relationship between various patterns of dietary intake and nutritional and health status.   
5) The nutritional changes including changes in food intake which accompany chronic diseases common in the older person..   
6) The role of nutrition and nutritional status during adult years in the etiology and pathogenesis of diseases and problems of older persons..   
7) The effect of therapeutic regimens (i.e., drugs, surgery) on nutritional status and the effects of nutritional status on the efficacy of therapeutic agents.   
8) The association between nutritional status and morbidity and mortality -- examining patterns of dietary intake and mortality.   
9 ) Valid methodologies for use in assessing nutritional status in older persons and in establishing age-appropriate norms. 

Although recent estimates suggest that 20x of the population in the year 201o will be over 60, and that one half of those will be at least 75 years of age, much of the research base on nutrition, aging, and health is quite immature. An increase in the understanding of these dynamic. interrelationships can improve the quality of life of the aged, provide more effective health care,. and lessen the impact of aging on the health of older persons.. 

A balance of animal experiments, epidemiologic research, and clinical trials is needed to study the nutritional status and requirements of geriatrics. To assess nutritional status ideally requires 1) determining daily consumption of energy and nutrients, 2) measuring tissue levels of nutrients, 3) clinical examinations including anthropometric measurements, and 4) evaluating physical and mentalfunction. Current assessments of older persons are handicapped by a lack of appropriate age-related biomarkers and valid standards for intake and biochemical and anthropometric values to which survey results can be compared. The related limitation in methodology and gaps in research knowledge were discussed under the nutrition surveillance section. 

Many of the gaps in our knowledge about nutrition and aging are being investigated by NIA-supportec researchers and by researchers at the NIA, the usDA Human Nutrition Research Center on Aging, and other government and private research centers around the country. 

Effects of aging on dietary intakes and eating patterns 

The need for research on socioeconomic influences on eating behaviors of older persons and the biopsychosocial antecedents of age-related changes in eating habits will be discussed in this section. There is a need to clearly differentiate generational patterns in selection and eating of foods from changes in eating habits which are age-specific. Since previous educational, social, economic, and cultural experlences vary widely among various cohorts individuals over age 65 years, these influences on food use and preparation patterns need to separated from late life modifications in eating habits that result from age-related physical changes, chronic diseases, and lifestyle changes (5l). Little is known about the diets and nutritional status of individuals 75 years of age and older, who are part of the most rapidly growing and frailest segment of the U.S. population. 

Future research also needs to address the differences In dietary patterns associated with various stages in the late life cycle and with the variety of settings within which older persons live (i.e., alone, with family, or institutionalized). In addition, the effects of interventions, social or nutritional, at these various stages and in these settings need to be evaluated (5i). 

Among the socioeconomic factors, the type and level of income are particularly important. Poverty for example, can restrict the amount and frequency of food purchases and also influence housing, cooking facilities, and overall health (3). Eating patterns and food choices are also determined by family structure, social situations, emotional status, cultural and religious beliefs, and living arrangements. Therefore, retirement, children leaving home, divorce or death of spouse, a 

move to an institution. a,new community, or a residence with limited cooking,facilities. or entering or.re-entering the labor force later in life can introduce changes in the food purchases,. food preparation methods, and eating environment.\* These changes, along with social isolation and. psychological problems, smay cause anorexia or disinterest in, food., Boredom can Iead to over eating Lewin's (52) social netvork analyses and cifft's.(53) examination ot nutriton. behavior, and change provide approaches to determine what social interactions change with age and how these changes effect nutritional status. Research that has Identified food- and.   
nutrition-related attitudes and knowledge of older persons will be discussed in the last section. norial diets further affect food choices.. Age-related sensory impairments.and prescriptions for special diets further affect food choices. train .oss.of.yision may,restrict ability to prepare food or obtain food.  Loss of hearing may constrain socializing at mealtime or may make it dif- ficult to get information on menu items or food. ..Loss of smell and taste acuity may directly affect appetite and decrease the desire to eat (54, 55). Professionally prescribed diets such as low sodium, low fat, and low sugar may. further depress appetite and increase anorexia. Future research should investigate the effect of special diets on food intakes and new ways to formulate appetizing foods lower in specific.. nutrients, yet acceptable to the target population. Answers to these questions will certainly require cooperation among gerontologists, physiologists, and food scientists.. Aging, and energy and nutrient requirements   
The nutritional requirements of those over 65 are difficult to determine and are largely unknown.   
Undetected disease and use of dietary supplements or medication complicate the task of defining   
population samples that are representative of various strata of older persons. In addition, there   
are few controlled metabolic studies in humans related to micronutrlent metabolism in aging (21).   
An examination of long-term diets of very old people who have remained healthy until an advanced   
age may shed.light on nutrient needs of older persons. 1 1 nersons   
agewaJ   
At present, most nutrient requirements are generally age invariant. However, RDAs for all persons   
over 51 are extrapolated from data collected mainly on males ages 20 to 30 years of age (48, 56).   
Current research on the yitamin nutriture of older persons may provide data to modify the current   
recommendations, especially as the relationships between specific nutrients and chronic diseases   
unfold or if newer RDAs optimize health and tissue function.. unIo1u   
Energy needs decline with age because of decrease in metabolism related to a decrease in physical   
activity and loss of lean body mass. Since energy needs decline while nutrient needs remain stable   
or perhaps increase, recommending nutrient levels in terms of weight of the nutrient per l00o kcal   
or per unit of lean body mass may be particularly useful for those over age 65 years. energy intake restriction and exercise affect aging. This topic will be addressed later. Protein synthesis appears to decline with age (44, 57), as does the synthesis of muscle tissues, organ tissue, and other protein moieties (e.g., collagen, immune system components, and enzymes) (33). Declining protein intakes do not appear to affect deleteriously older populations who have no evidence of wasting diseases (57). Nitrogen and dietary protein requirements may, however, be Increased in response to physiological stress common in older persons (i.e., infections, fractures, surgery and burns) (56). Preventing protein deficiency with attendant hypoalbuminemia is most Important in older persons when protein-bound drugs are taken (44). Patients with renal or hepatic disease may require protein restrict- lons. However, the quantity and type of protein best able to disease may require protein restrict- lons.. meet the needs of older people has not been ascertained, even for healthy populations. meet tne necu Present evidence indicates that vitamin A and riboflavin absorption or tissue levels do not decline. with age, despite intakes that are lower than the present RDA (17). Research on the role of carotenoids in cancer etiology may indicate advantages of increased intakes. Age does not appear to affect folate absorption and/or metabolism, except in individuals with atrophic gastritis (58). Individuals with hypo- and acholorhydria may compensate for the malabsorption through increased bacterial folate synthesis. 1eastfor Some research suggests that the RDAs for vitamin D, B6, and B12 might be too low, at least for certain groups of older persons (21). Reduced vitamin D synthesis in the skin, lack of sun exposure, low intakes, and impaired 1-a hydroxylation depress vitamin D production in older person: For now, Increased sun exposure combined with low-dose supplementation (i.e., 10 ug/day) (21) or twice-per- year regimen of 2.5 mg vitamin D2 (60) are recommended for housebound older persons to maintain adequate serum vitamin D. Both human and animal research suggest age-related or. increased urinary excretion), but more conclusive data are needed to suggest changes in the RDA (21). Serum vitamin B12 levels appear to decline with increasing age, perhaps because of pernicious anemia and/or atrophic gastritis-related malabsorption (21). Negative health consequences of these changes have not been documented (61).. cons equeu There is no consistent evidence for linking vitamin E. thiamin, or vitamin C requirements with The effect of increasing dietary vitamin E levels on tissue lipid peroxidation and platelet age. 

vitamin E levels (and function) needs further exploration (21). Age-related changes in thiamin. absorption vary depending on the assessment method used;. however, it is well known that alcohol interferes with thiamin absorption and phosphorylatlon.. Age-related declines in vitamin C levels. in the blood, plasma, and leukocytes are reported in most studies: however, changes in tissue levels are less consistent (21). Smoking (62), medication (63), and environmental stress (64) combined with low Intakes, can compromise vitamin C status, but the health consequences of these observations are not well-established (34). 

Until improved methods for biochemical evaluations of vitamin K and niacin nutriture are availabie, it is difficult to determine changes in nutrient requirements for these vitamins.. Incomplete food tables handicap studies on zinc, copper, chromium, and selenium status of the older persons. Fluid intake, especially water, declines in older persons along with a age-related loss of body water. Adequate water intake (e.g., 30 ml/kg of body weight) or approximately 1 ml of water for each. calorie insested) (64) is reasonable and important to normal renal and bowel function (5, 65).. 

Several auestions are important to consider in setting nutritional requirements for the aging (44) 

1. Can we formulate dietary recommendations that mitigate against development of aging changes in body composition?   
2. Since diseases such as osteoporosis, atherosclerosis, and cancer are in part age-related and appear to have long latency periods, can we offer guidelines for the diets of younger people which will protect them from the development of these diseases?   
3. What criteria should we use to determine the nutrient needs of elders?   
4. What are the speclally formulated preventive health goals for the elderly? Should they change with successive age strata over 65 years? 

Effects of energy intake and expenditures on the aging process 

Although some older persons seek the "fountain of youth" in dietary supplements, the answer to deceleration of the aging process may be found in caloric deprivation or increased energy expenditure. Energy intake restriction (ER) without essential nutrient deficiency has been the only intervention in animals that extends maximum lifespan in all species tested and across wide. phylogenetic differences. Long-term national studies of persons on low calorie diets are often. confounded by low levels of nutrients and/or poor personal health habits. 

Walford et al. (66) described four phases that trace the history of ER in the study of aging. Initial work showed that ER slows the biological aging process and favorably affects the incidence and age of onset of malignancies, arthritis, renal disease, and osteoporosis in animals. Secondly, animal studies demonstrated that ER animals had slowed age-related changes (not necessarily disease" related) in the immune system, liver enzymes, age pigments, behavioral and psychomotor patterns.. The third phase is a search for mechanisms that suggest causality that might include altered gene expression, thymic hormone levels, protection against free radical injury, and DNA repair.. Descriptions of the effect of ER on circulating levels of insulin, somatostatin, thyroxine, and other hormones are needed. Exploring energy restriction in humans is the next phase.. 

Increasing energy expenditure through exercise also appears to influence. mortality and morbidity. through a number of complex physiological mechanisms.. The effects of inactivity mimic the effects. of aging (67); almost 50z of the functional decline attributed to aging may in fact be related to inactivity (68). Combined with a calorie-appropriate diet, exercise maintains a,reasonable body weight, lean body mass and good physical performance.. This combination also helps to prevent or reduce fat cell hypertrophy, production of high density lipoproteins (HDls), hypertension,: osteoporosjs and insulin resistance. {A separate background paper. explores exercise in more. detail.} 

With the increasing interest in the effects of peroxidation processes on aging, intervention with. various antioxidants, including vitamins A, C, and E and selenium has been tried in both animal and human trials but the results have been mixed or inconcluslve.. More research is needed in this area. 

## Drug and nutrient/food interactions 

The high use of drugs among the aging may further compromise their health. The average older person receives more than 13 prescriptions a year and may take as many as 6 drugs at a time. Caxdiac drugs (e.g., diuretics) are most widely used by the aging population, followed by drugs to treat arthritis, psychic disorders, and respiratory and gastrointestinal conditions. Many of these diseases are diet- related, and the use of drugs may complement, supplement, or supplant diet ther apy - 

Long-term use of a variety of drugs (often at high doses) raises the risk of drug-nutrient.   
interactions. Individuals with nutritionally inadequate intakes and impaired nutritional status.   
are at the highest risk. Use of high-potency nutrient supplements may also affect drug efficacy. 

Physicians need to explain carefully the potential side-effects when certain drugs ana foods/supplements are taken together. For some older persons, altering the drug therapy may be more appropriate than recommending dietary changes or food restrictions. identify borderline nutritional status that require appropriate dietary recommendations, nutrient .lamentation, or change in drug regimen. 

Roe (44, 69) has detailed several areas of drug-nutrient interactions. These inciuue   
effects on drug disposition, 2) drug disposition in malnourished subjects, 3) drug induced   
malnutrition, and 4) drug-food and drug-nutrient incompatibilities. Key interactions relevant to   
the aging population are discussed below and more detail on drug use is provided in a separate More research is needed to explain these interactions and to determine their   
background paper.I -I.nificance in the aging population. 

Foods components and nutrients can affect drug absorption and metabolism. Heavy metais,. intakes and, to a lesser extent, high protein foods delay gastric emptying and, thus, delay the passage of drugs into the small intestines. High protein diets may also accelerate hepatic drug A fasting state may hasten drug absorption from an empty stomach.. 

Malnutrition also alters drug absorption, protein binding, drug metabolism and drug cieara. Protein-bound drugs such as warfarin and diazepam may be more toxic in patients with hypoalbuminemia. On the other hand, some drugs decrease absorption of nutrients or cause mineral depletion. Such drugs include laxatives, antacids, anti-inflammatories (e.g., aspirin), diuretics,. antibiotics, analgesics (e.g., Indomethacin), and hypocholesterolemics (e.g., cholestyramine). Appetite can be enhanced by tricyclic antidepressants, reserpine, antihistamines, and anabolic. steroids, whereas amphetamines and related drugs depress the appetite. But the aging process can reverse these effects. Phenothiazine, a psychotropic agent, that usually increases food intake may decrease appetite in older persons whose rate of drug metabolism is slowed. Specific foods or alcoholic beverages can precipitate adverse reactions to drugs. Some reactions such as the tyramine reactions with monoamine oxidase inhibitors may be life-threatening, while others such as. -enctions caused by disulfiram and hypoglycemic agents to alcohol are extremely unpleasant.. 

Guidelines for drug development are needed that inciude studies in the elderly and consiu. Initially, research must determine how much drug   
various drug and food/nutrient interactions.   
efficacy and safety might improve with proposed guidelines (70). The quality of such research   
depends in part on the reliability of nutritional status assessments conducted and nutritional   
standards appiied. Education-information transfer about drug-nutrient interactions for.the pubiic .areoivers also needs consideration (70). 

## Diet and chronic degenerative conditions 

The prevalence of chronic conditions, such as osteoporosis, gastrointestinal disorders, diadetes cardiovascular disease, and central nervous system disorders, increases with age.. are the role of nutrition in delaying the onset or mitigating the consequences of these conditions The following examples are illustrations of the focus of NIA-sponsored research and conferences.   
.nino and nutrition research topics: 

Osteoporosis is defined as an absolute decrease in the amount ot bone,. Osteoporosis: Although age-related bone loss is common, certain older persons. are at higher risk of developing fractures than others. Riggs (71, 72) suggests that osteoporosis may be two distinct bonethinning syndromes: 1) a \*postmenopausal" form (Type I), associated with. estrogen deficitncy and 2) a "senile" form (Type II), highly correlated with aging. Type I,. occurring predominantly in females 15-20 years after menopause, thins trabecular bones (e.g., vertebral bodies, ultradistal radius (forearm), and mandibles) that lead to fractures and tooth Type II, occurring mainly in persons of both sexes over 75 years, thins both the cortical. 1oss. and trabecular bones proportionately, leads to fractures of hip, femur, tibia, and pelvis.. 

Definitive etiologies for either the early deficit in trabecular bones in Type i or grauua. thinning in Type II need to be determined. Pharmacokinetic studies using calcitonin and   
diphosphonates have begun to explain the cellular mechanisms of bone resorption. Other studies (73, 74) have suggested risk factors including insufficient bone density at maturity, low levels of. endogenous estrogen and other hormones, prolonged immobility and weightlessness, long term use of corticosteroids, family history, impaired intestinal or renal function, and diet.   
osteoporosis has become a public health concern and has brought the promotion of foods high in calcium (e.g., milk products), calcium fortified foods (e.g., cereals, breads, and soft drinks), high potency calcium supplements, and other nutrient supplements.   
recommended calcium intakes at a level of 1000 to 1500 mg, estrogen therapy, and exercise for women. 

Questions remain about 1) what levels of calcium Intakes are most protective against agebone loss and do these levels vary with age or sex of individual, 2) do calcium requirements vary with the level and type of physical activity, 3) how does calcium intake/supplementation interact 

with estrogen status, 4) do calcium, fluoride, and vitamin D metabolites protect bones   
Independently or in conjunction with estrogen therapy, weight-bearing exercise, or other   
approaches, and 5) how do vitamin D, protein, phosphorus, and even alcohol affect calcium Lastly. designing precise methods for measurement of bone mass is critical for   
determining relationships between diet and bone loss for the population or assessing the risk of in individuals so as to use prophylactic therapy most effectively (76). 

Osteoarthritis (oA) also causes great pain, immobility, and loss of independence for many agiug. individuals. Although nutrient deficiencies or excesses have not been implicated in this disease,. obesity has been found to be associated with OA of the knee and hip but not of the sacroiliac joint ( 7 7) . 

glycosyldt   
Clycation in diabetes and cardiovascular disease: Glycation or non-enzymatic. Glycosylation describes the   
well be involved in the etiology of a number of age-related diseases..   
process whereby glucose, fructose, or galactose react with proteins or nucleic acids to form a. The Schiff base undergoes further changes to form advanced glycosylation end (AGE)   
products. The excessive accumulation of AGE products In the tissues, especially in the arterial   
walls, accelerates progressive stiffening or rigidity of these tissues. This rigidity may be -.d hu rhe cross-linking of proteins (e.g., collagen) and increases with age..   
Elevated glucose concentrations characteristic of diabetes promote advanced glycosyiation, Such rigidity may lead to reduced elasticity in the   
accelerating stiffness of the tissues. As a result, cardiac function declines, renal blood flow decreases, and   
vital lung capacity and oxygen uptake also decline. Further studies on advanced glycation may   
elucidate the mechanisms involved in the formation of senile cataracts, aging peripheral nervous tem. and etiology of atherosclerotic plaques. 

Hypochlorhydria: New research initiatives are studying the effects of aging on gastric secretsun. and the subsequent impact on nutritional status of the older persons. J Women are increases with age and may affect up to one-third of those people over 60 years of age. more often affected than men, but the current extent of the problem and those at highest risk for Future epidemiologic studies of hypochlorhydria must be based on a common disease are not known.I The causes of standardized case definition in order to assess the impact of aging on the disease. hypochlorhydria and the commonly associated atrophic gastritis are also largely unknown, yet these Ateardara have far reaching implications for health maintenance in the older population. 

The major clinical implications of hypochlorhydria are altered absorption of nutrients and arugs in the upper gastrointestinal tract, bacterial over growth resulting in infections and changes in the Immune response, and the predisposition to other diseases and disorders. Defective absorption of calcium, iron, folate, and vitamin B12 and the related deficiency diseases are of particular concern in hypochlorhydric patients. Reduced production of hydrochloric acid may affect the develonment of gastric cancer. 

Current knowledge of the extent ot interacrions. B-vitamins and central neryous system function:. nutrition and neurology is limited. The effect of B vitamins and other nutritional factors on. brain function, Including dementia and motor control, is better established. Deficiencies of various nutrients, particularly vitamin B12, thiamin, niacin, and folate impair cognition. Rigorously controlled, double-blind, prospective trials may elucidate the cognitive effects of. malnutrition, especially subclinical, or multiple deficiencies of B-vitamins. To date, much information in this field is based on animal studies that may have limited applicability to human. conditions.or on clinical pathology complicated by advanced age, alcoholism, and disease.. 

In addition, analytical methods specific and sensitive enough to measure the leveis ana melavu.. of B vitamins are only beginning to be developed. However, still more basic methodological. research is needed before further refinement in study design can be attempted. For example, based on new evidence using updated technology, it appears that folic acid as a naturally occurring. excitatory agent found in the brain may have a mechanistic relationship to neuropathological. conditions such as epilepsy-related brain damage, lithium neurotoxicity, tardive dyskinesia, and neuronal deseneration associated with aging.. 

The study of nutrients' effect on brain function has not received widespread attention oecause was commonly believed that the brain was well protected from fluctuating plasma levels of dietary nutrients by the blood-brain barrier (BBb). Now, it appears that food constituents affect the synthesis of brain neurotransmitter and thereby modify brain function (e.g., alertness or. depression) and behaviors (e.g., sleep). Fernstrom (78) and Wurtman (79) have shown that the levels of serotonin, an appetite-controlling neurotransmitter, can be increased by a high-carbohydrate, protein-poor meal that elevates brain tryptophan, accellerating serotonin synthesis. They report similar regulation of brain acetylcholine by ingestion of choline-containing compounds and of brain dopamine by tyrosine-containing compounds. Besides macronutrients, levels of trace minerals in the brain affect formation of synapses, nerve impulses and nther brain activity in neurotransmitter systems (80). Since the blood-brain barrier serves as the interface betveen brain metabolism and diet, understanding the BBB nutrient transport pruce. provide insights into the mechanisms by which diet may influence brain functions (8i). Research in. this area is still too young to attribute altered behavior solely to nutrlent-induced changes in neurotransmitter levels. Improved study designs are needed that use standardized methods for. measuring behavioral responses and that adequately evaluate the dietary components and nutritional enhiects and controls (82). 

Although clinical research has not associated the severe senile dementia in Alzneimer with aluminum toxicity (83) or other nutritional imbalances, future research in this area may be Appropriate biochemical testing of individuals suffering mental loss or other promising. reauired for differential diagnosis of these probiems.. 

ne1   
Also of research interest is the effect of aging on the interaction of B vitamins witn ot.. For example, alcohol consumption which can cause Wernicke's encephalopathy compromises thiamin pyrophosphate-dependent enzymes and interferes with thiamin absorption and phos- phorylation.   
Cinemet. used to treat Parkinsonism, can cause niacin deficiency. 

cervices in the health care of the older persons 

Nutritional   
About 85x of older persons have one or more chronic, potentially debilitating diseases and couiu. benefit from nutrition services. Up to half of older individuals have clinically identifiable nutrition problems requiring professional intervention (3). If the goal of health promotion is to. assure the older persons' health, independence, and quality of life, incorporation of nutritional services into the continuum of health care -- institution, ambulatory, and home-based care -- for Since older persons are more susceptible to foodborne poisoning than. younger people, proper sanitation practices are needed in food preparation and service in all these. health care settings. 

Nutritional Assessments Nutritional services, whether therapeutic, rehabilitative, or maintenance services, include. clinical, educational and foodservice components. assessments should become routine parts of physical examinations for all older residents of health homes, or community health centers (84). assessments should guide medical orders including drug regimens, scheduling surgery, dietary (The limltations of assessments were discussed earlier.) guidance, and other nutritional therapy. idontifv nutrient 

Complete diet histories provide information on eating habits that can identiiy specia1 inadequacies early. Since the food habits of the older persons reflect long-term patterns, attention to the food preferences, cultural and religious beliefs, economic status, drug and supplement use, and lifestyles can enhance compliance with specific dietary regimens, while Ah+ain enourh food and enough of the food they like. 

ensu.L"s intake may aie+ For hospitalized or institutionalized patients, regular documentation of food. health professionals to potential nutrition problems (5). Anorexia, induced by drug or radiation therapies or resulting from surgery or chronic conditions, can quickly lead to nutrient. deficiencies, especially in frail older persons.. parenteral, formulated feedings, have minimized attendant medical complications (e.g., infection), improved therapeutic responses, and sped recovery in some patients. However, the prospective. payment system jof financing health care (discussed below) may be a disincentive to use of. ...-irional support in hospitals. nnrt 

For the hospitalized or frail older persons who cannot eat, providing adequate nu. Entera1   
through tube or intravenous catheter can contribute to regaining health and independence..   
and parenteral feedings can sustain life for patients who are physically unable to swallow, digest, .henrh food and fluids taken by mouth and for patients who refuse to eat.. + h e 

Little is knowu The efficacy of these therapies is not universal across all diseases.. efficacy in older persons, partly because of the lack of information on the nutritional. requirements and standards for the older persons. Nutritionists and other health care. professionals will more frequently participate in debates about withholding and withdrawing nutritional support and hydradration\`from terminally ill, comatose, and severely debilitated. people. In addition, health care providers will be faced with questions about when and if to use these treatments with severely demented persons who cannot decide on the course of their therapy and mav need to be physically restrained (85).. 

Fducation and training for working with older persons 

With the emergence of diverse health problems among the fast-growing numbers of older per. NIA sets numher of education and training programs on aging and geriatric. 

and biomedical researchers to specialize in. as two high priorities: 1) training of clinicians. nutrition and aging issues and 2) development of centers of excellence in nutrition and aging re4earch. 

Professional socleties (86), research centers (87) and programs for medical, nursing, ana nu.. students (88, 89) have offered courses or seminars to address ethical concerns in nutrition for. attitudes toward the older persons.   
long-term care patients and to encourage positive   
may be necessary to train some health professionals to be geriatric specialists, the benefits of. "main-streaming" older persons into generic health care services outweigh the hazards of. Appropriate funding for ambulatory and stigmatizing and stereotyping their health problems (89).   
health care services for older persons may also change the perception of students that these jobs are often low paying. 

.ct of health care financing on nutritional care of older persons 

1 ne As the population ages and individuals live longer, health care expenditure will increase. major reason for this increase is that health care utilization is greatest among the older persons,. especially the oldest old -- the segment of our population that is growing the fastest. To date (1984) major sources of financing the health care of older persons in the United States are: 1). medicare (49x). 2) out-of-Pocket (25x), 3) medicaid (13x), 4) insurance (7x), and 5) other The federal government pays for about 68x of all health care expenditures. government sources (6%). (90) . 

Government expenditures are dispersed as follows: 39% to hospital costs, 20z to personal nea. In 1983, due to   
physician services expenditures, and 21x to nursing home and other expenditures. Congress and the Administration proposed reform -- the.   
escalating health care expenditures,. rtive navment system (Pps) for Medicare reimbursement of hospitals.. 

Under the Pps, Medicare pays for each hospital admission, a rate predetermined on the basis ot ... patient's principal diagnosis and certain other factors. Each admission is assigned to one of 468 diagnosis related groups (DRgs) for payment. PPs is intended to discourage extended inpatient stays and encourage the substi- tution of less expensive care outside of the hospital (9i). As a result of the Pps there has been a decline in the average length of stay for Medicare patients, and. therefore an increased demand for postdischarge services. The prospective payment system provides a financial incentive for hospitals to cut costs below the reimbursable level and adjust inputs, such as tests, personnel time, and special procedures (92). Studies are determining the impact of poc an the auality of care (92) and on access to in-hospital nutritional support services (93). 

The impact of pps on the nutritional status of post discharge patients also needs examining. Patients are discharged early in what appears to be poorer states of health and needing extensive Health providers are finding it harder to retain patients requiring long term care (94).   
nutritional support for a long enough time to monitor their status and train them before discharge. Since October 1983 greater numbers of these patlents (40z increase in discharges) are being. transferred to skilled-nursing homes or requiring home health care (95). Often these facilities do not have the proper equipment, supplies or trained personnel to deliver safe and appropriate tube. or intravenous catheter feeding (5). Hospice programs and some home health care programs inciude nutritional services: however, the majority of alternative community-based services do not include nutritional services (3). The costs of nutrition services provided by hospice programs are absorbed under the organization's administrative overhead (3) because medicare and most third party ervires do not reimburse nutrition services directly. 

Cost containment pressures are projected to shift more demand from the hospital to the community, especially to home care services traditionally provided through the nonprofit sector. The number of Medicare certified home health agencies increased from 2,212 in 1972 to 5,755 in 1985. The. growth has primarily taken place In facility-based and for-profit home health agencies, while the number of more traditional nonprofit providers -- visiting nurse associations and government. agencies -- has declined slightly (96). Questions arise as to how the communitycare nonprofit sector will cope with the increasing demands for delivering of highly technical in-home health care that drains resources from delivery of more traditional, community-decided, multi-services (e.g., anenartarion. food preparation assistance, primary health care) (97).. 

Technolosical adyances and feeding the older persons 

Changes in the physiology and organ systems of older persons challenge the food industry as it Creativity will be needed to formulate products   
attempts to serve the growing market of elders.   
that are flavorful, visually attractive, and have high nutrient densities. Products will need to Fortified products need to assure high.   
supply high nutrient levels for their caloric value. For several years, food manufacturers have been gradually   
bioavailability of the added nutrients..   
lowering the salt, fat, and sugar content of food, while retaining good flavor in most products.   
Manufacturers have also addressed current nutrition research concerns by increasing the fiber, and vitamin D content of cereals and other foods. Special diet products that are low. 

protein, cholesterol-free, lactose-free, or very low in sodium are also available (35, 98). An earlier section also discussed the use of parenteral and enteral feedings.. trlier section Supermarkets and food stores are recognizing their responsibilities toward their aging clients. ome grocery stores are establishing specific shopping hours for senior citizens complete with bus ervice. bargain sales, and refreshments. Other ways to reduce barriers to food shopping include: 1) sales on small packages and at off peak-hour times, 2) educational materials written in larger print that suggest tips for meal planning, budgeting and food preparation for single-person. households: 3) take-home product listings to use with telephone orders, 4) shelf-labels with large rint, 5) uncluttered aisles, and 6) convenient benches and rest rooms (81). 

Jutrition and food assistance programs.   
Jver the past 20 years, both the public and private sector have initiated and reformed food   
assistance programs to respond to evidence that nutritional deficiencies were prevalent in older   
persons, especially those with low-income or who are socially isolated. A variety of services are   
now available to elders with a continuum of functional capacity (99). The Continuum of Community   
Nutrition Services model developed by Balsam (loo) describes this variety.   
Federal nutrition programs include the food stamp program, the commodity supplemental food program,   
the congregate feeding program, and the home-delivered meal program. Private charities have teamed   
with the public programs to expand food service to elders. Luncheon clubs (lo1) have permitted.   
suppers and food pantries provide emergency food boxes. Luncheon clubs (lo1) have permitted   
seniors receiving home delivered meals to congregate in nelghbors' homes. Restaurants have cut   
prices for older persons and accepted their food stamps. Food industries have designed packaging   
and processing techniques to provide shelf-stable meals for evening and weekend use. Volunteers   
offer escort services to supermarkets or deliver groceries to many home-bound persons (102). to the ofIerescv   
Revisions to the usDA Food Stamp Program extended benefits to low income elders by eliminating the purchase requirement and increased their benefits by ailowing for medical and shelter deductions (103). Nonetheless, many older persons still receive only minimal benefits (\$io/month) and their participation rates are low (<50x of eligible) (90). For low-income, often frail, elders, who were uninterested in receiving food stamps and had difficulty in shopping, Congress authorized delivery .di+v Suoplemental Food Program. of low-cost commodity packages under the Commodity Supplemental Food Program. The Dhhs National Nutrition Program for Older Americans, as specified in Title IIl of the Older Americans Act, includes food service for both the ambulatory old (congregate feeding). and the home-bound old (home-delivered meals) (3). Evaluations (103, 104, 105, 106) of the congregate feeding program and the home-delivered meals (l07) generally show that participants have higher intakes of essential nutrients than nonparticipants.. nonnarticipants. During recent hearing on program reauthorization, the American Dietetic Association (ADA) (108) raised concern that future program budgets must account not only for the annual infiation but also for the annual rate of increase in the older population. The flexibility in funding for Title III. concerns many because it permits shifting funds from meal programs to supportive services. Currently, the congregate feeding program reaches only 1ox of the eligible population. The need for. home-delivered meals has increased significantly (35z to more than 50z increase in persons receiving meals) in the first year after the implementation of the new prospective payment system of health care financing (3). As dietary restrictions become more complex, especially for those in their late 70s or 80s, demand for special meals and nutrition information will increase, requiring additional program resources and qualified professionals.. reyuLL To formulate policies for food assistance programs requires attention to: Planning and conducting systematic evaluations of food programs to assure they meet the a. changing needs (nutritional, social, educational, and economical) of the heterogeneous Developing new approaches to reach underserved groups of elders, such as the homeless anc b. soclally impaired elderly, minority and ethnic elders, and to extend food service beyond. Setting and revising (as needed) nutritional guidelines for meals served in senior c. Establishing a clearinghouse for exchanging information on innovative programs that meet. d. Assuring that educated and trained nutrition professlonals assist with planning and e. monitoring these programs at all levels of government. 

The tools that promote good nutritional health for older persons are most probably the nutrition information gained from mass media or education programs. Because of the myriad of nutrition messages received, sorting out consistent truths from half-truths or conflicting information frustrates people at all ages. Educators need effective ways to minimize the confusion and also to translate current, relevant research into dietary advice applicable to elders. The great heterogeneity among older persons and the reality that life-long habits are resistant to change make desianing nutrition messages a challenge for educators. 

Key to appropriate, effective nutrition education for this group is understanding the complexities. of aging, applying knowledge of the change process, and assessing cognitive, affective, and. nutritional status changes (lo9). Effective nutrition education also requires knowing the. perceptions older persons have toward eating and foods. Many older persons, relate food to social. interactions and entertainment and also recognize food as a source of nutrients that is important to health (llo). More research on factors that facilitate learning and making dietary changes can improve nutrition education efforts (lll). 

Applying communication theory (l12) and marketing principles (113) to nutrition education enhances the chances that the consumer will act on the research-based dietary guidance. Such an approach. allows the audience to identify what they want to know, how they want to receive information, where they want to learn, and how often they want follow-up. For example, older persons have sought a. uniform set of dietary guidelines, appropriate for most chronic diseases. They have also posed. questions about health fraud, use of vitamin and other dietary supplements, and drug and food. interactions (114). 

Though not tailored specifically for older persons, the Dhhs/usdA Dietary Guidelines for Americans provide essential information for motivating dietary changes that promote health. Modifying the text slightly to be more relevant for older persons, printing copies with large lettering, and distributing them through Title III programs could permit wider use. The Healthy Older People program conducted by the Office of Disease Prevention and Health Promotlon promotes good nutrition, proper exercise, and other health messages through the media and consumer education materials. (l15). Combatting health fraud is a priority of the FDA, the Federal Trade Commission (Frc), and Congress. Ihe two agencies have launched an educational/media campaign against health fraud, and recently sought stronger court actions against false. advert sements for dietary supplements (ll5). Since nutrition education has been found to be negatively correlated with misconceptions about. "vitamin/mineral supplements" (ll6), informing older persons about the benefits and hazards of. dietary supplements could result in more prudent use of these substances. Food labels also provide. good sources of nutrition information: but without close monitoring of the health claims on labels, older persons could be deceived or adopt false expectations of the food.. 

Title IIl of the Older Americans Act is the only federal nutrition program for older people that relmburses nutrition education. Based on the recent National Association of Area Agencies on Aging and the Administration on Aging's survey results (li7), nutrition education, though often a high. priority for some program administrators, is not routinely incorporated into all programs. Thr ee reasons most frequently cited for lack of nutrition education are inadequate funds, the absence of qualified nutrition educators, and the lack of specific program standards and guidelines for nutritlon education (l18). 

Other nutrition policy considerations might include (ll9): 

1. What central nutritional message do seniors want - changing the amount of food eaten, e at ing more nutritious foods, understanding drug and food interactions, or learning about and using community nutrition programs?   
2. How can the messages delivered by the federal government be better coordinated, and how can the government messages be coordinated with those of the private sector?   
3. What format, Ianguage, and style for educational materials are most useful and appealing to older persons?   
4. What medium (e.g., groups, mass media) is most effective to use in reaching older persons as Broup and the various subgroups over age 65?   
5. What should be done to assure that qualified nutritionists assist with planning, coordinating. evaluating, and monitoring nutrition education programs at the federal, state, and local level? 

## REFERENCES 

U.S. Congress, Office of Technology Assessment. Technology and Aging in America. Health Promotion/Disease Prevention and Nutrition in the Elderly. Washington, D.C.: Government Printing Office, 1985. pp. 119-134 Costell, D0. Diagnosis of Non-Cardiac Chest Pain in 0lder Patients. Geriatrics 1985: 40(i0): 61-86 Posner, BM., Fanelli, MI., et al. Position of the American Dietetic. Association:  Nutrition, Aging, and the Continuum of Health Care. J Am Diet Assoc 1987: 87(3): 344-347 Guthrie, HA. Supplementation: A Nutritionist's View. J Nutr Ed 1986: 18(3): 130-132 Chernoff, R. and Lipschitz, DA. Aging and Nutrition. Comprehensive Therapy 1985: 11(8): 29-34 Norton, L. and Wozny, MC. Residentiai Location and Nutritional Adequacy Among Elderly Adults. J Gerontol 1984; 39: 592- 95 Akin, JS et al. Cluster Analysis of Food Consumption Patterns of Older Americans. J Am Diet Assoc 1986: 86: 616-24 Villers Foundation. On the Other Side of Easy Street. Washington, D.C.: Villers Foundation, 1987   
I. Lewis, M. Older Women and Health: An Overview. Women & Health 1985; 10:1-6   
). Bailey, FE. and Walker, ML. Socio-Economic Factors and Their Effects on the Nutrition and Dietary   
10. Habits of the Black Aged. J Gerontol Nursing 1982; 8(4): 203-7 Newman, JM. Cultural, Religious and Regional Food Practices of the Elderly. J Nutr Elderly 1985;   
11. 5(1): 15-19 Netland, PA. and Brownstein, H. Acculturation and the Diet of Asian- American Elderly. J Nutr Eld   
12. 1984; 3(3): 37-56 Newman, JM. and Ludman, EK. Chinese Elderly: Food Habits and Beliefs. J Nutr Eld 1984: 4(2): 3-13   
13. Davis, MA. and Randall, E. 198i Social Change and Food Habits of the Elderly. National Institute   
14. of Aging's Social and Psychological Developments in Aging. Paper for the White House Conference on Aging 1981.. Schneider, EL., Vining, EM., Hadley, EC., et al. Recommended Dietary Allowances and the Health of   
15. the Elderly. N Engl J Med 1986; 314(3): 157-60 Elahi, VK...Elaht. D:. Andres R., et al. A Longitudinal Study of Nutritional Intake in Men. J 16. Gerontol 1983: 162-180 Garcia PL., Battese GE., and Brewer, wD. Longitudinal Study of Age and Cohort Influences on 17. Dietary Patterns. J Gerontol 1975: 30: 349-56 Dresser, CM, Dietary Status of Community-Based Older Persons. Paper presented at the American 18. Dietetic Association 67th Annual Meeting, Washington, D.C., Oct. i5-18, 1984 Cronin, FJ., Krebs-Smith, SM., Wyse, BW., et al. Characterizing Food Usage By Demographic 19. Variables. J Am Diet Assoc 1982: 81: 661-73 USDA. Nutrient Intakes: Individuals in 48 States, Year 1877-78. Nationwide Food Consumption 20. Survey 1977-78 Report No. I-2. Human Nutrition Information Service, UsDA, 1984 21. Suter, PM. and Russell, RM. Vitamin Requirements of the Elderly. Am J clin Nutr 1987; 45: 501-1 Garry, PJ., Goodwin, JS., Hunt, wc., et al. Nutritional Status in a Healthy Elderly Population: 22. Dietary and Supplemental Intakes. Am J Clin Nutr 1982. 36: 319-31 Omdahl, Jl., Garry PJ., Hunsaker, LA.:.et al. Nutritional Status in a Bealthy Eiderly Population 23. Vitamin D. Am J Clin Nutr 1982; 36: 1225-33 DHHs/FDA. Consumer Nutrition Knowledge Study: A Nationwide Study of Foodshopper's Knowledge. Washingt? 24. Beliefs, Attitudes, and Reported Behavior Regarding Food and Nutrition Report II 1975. D.C.: Government Printing Office, 1976 :5. McDonald, JI. Vitamin and Mineral Supplement Use in the U.S.. Clin Nutr lyoo: Jtt, Stewart, ML., MeDonald, JI., Levy, AS...et al. Vitamin/Mineral Supplement Use: A Telephone Survey. !6. of Adults in the United States. j Am Diet Assoc 1985: 85(12): 1585-90 Shank, FR. and wilkening, VL. Consideration For Food Fortification Policy. Cereal Foods wld 1986:. !7.   
31(10): 728-740 Cordaro, JB.. and Dickinson: A. The Nutritional Supplement Industry-- Realities and Opportunities.   
28. J Nutr Ed 1986: 18(3): 128-129 Scheider, CL., and Nordlund, DJ., Prevalence of Vitamins and Mineral Supplement Use in the Elderly..   
29. J Fam Prac 1983: 17: 243-47 Garry, PJ., Goodwin, JS., Hunt, WC., et al. Nutritional Status in a Healthy Elderly Population:   
30. Vitamin C. Am J Clin Nutr 1982; 36: 332-39 Lecos, Cw. Diet and the Elderly, Watch Out for Food-Drug Mismatches. FDA Cons 1984/85: 18(10): 7-9   
31. DHHs/nchs. Health Promotion Data for the 199o Objectives, Vital and Health Statisties, Washington,.   
32. D.C.: Government Printing Office, Sept 1986; Number 126.   
33. Chernoff, R. Aging and Nutrition. Nut Today 1987: March/April: 4-11 U.S. Congress, Office of Technology Assessment. McGandy, R. Nutrition and Aging. Final Report fo1.   
34. the Office of Technology Assessment, 1985. Bidlack, WR., Smith, CH., Clemens, RA., et al. Nutrition and the Elderly. Institute of Food   
35. Technologists'. Expert Panel on Food Safety and Nutrition.   
36. DHHs/nchs. Health Statistics on Older Americans. Vital and Bealth Statistics Washington, D.C.:. Government Printing 0ffice, 1986 series 3(25)   
37. DHAs/nchs. Health United States 1985. Washington, D.C.: Government Printing Office, 1985 DBHs/nchs. Prevalence of Known Diabetes Among Black Americans, Vital and Health Statistics,   
38. Washington, D.C.: Government Printing Office,  1987: Number 130 Bauer, RL., Diehl, AK...Barton. SA...et al. Risk of Postmenopausal Hip Fracture in Mexican   
39. American Women. AJPs 1986: 76(8): 1020-21 Atwood, DA. Bone Loss of Edentulous Alveolar Ridges. J Periodontol 1979: 51: 11-21   
40. Tallgren, A. The Continuing Reduction of the Residual Alveolar Ridges in Complete Denture Wearers:   
41. A mixed-longitudinal Study Covering 25 Years. J Prosthet Dent 1972; 27: 120-32 Norris, AH. and Shock Nw. Aging and Variability. Annals NY Acad Sci 1966; 134: 591-601   
42. O'Hanlon, P. and Kohrs, MB. Dietary Studies of Older Americans. Am J Clin Nutr 1978; 31: 1257-69   
43.   
44. Roe DA. Gerlatric Nutrition. Englewood Cliffs, New Jersey: Prentice-Hall Inc., 1983. pp. 1-199 Chumlea, wC., Roche, AF., and Steinbaugh, ML. Estimating Stature From Knee Height for Persons 60   
45. to 90 Years of Age. J Am Geriatr Soc 1985: 33: 116-120 Lipschitz, DA., Mitchell, Co. Nutritional Assessment of the Elderly-- Special Considerations.   
46. Wright and S Heymsfield (Eds.), Nutritional Assessment Boston: Blackwell Scientific, pp. 131-39 Fanelli, MI. The ABC's of Nutritional Assessment in Older Adults. J Nutr Eld 1987: 6(3): 33-41   
47. Clemens, RA., and Brown, RC. Biochemical Methods for Assessing the Vitamin and Mineral Nutritiona!   
48. Status of the Elderly. Food Tech 1986: 40(2): 71-81 O'Neal, RM., Johnson, Oc.. and Schaefer, AE. Guidelines for Classification and Interpretation of   
49. Group Blood and Urine Data Collected as Part of the National Nutrition Survey. Pediatr Res 1970; :   
103-6   
50. Sauberlich, HE., Dowdy RP., and Skala, JH. Laboratory Tests for the Assessment of Nutritional Status. Cleveland, OH: CRC Press Inc., 1974.   
51. Howell. S. and Loeb, MB. Nutrition and Aging. Geriatr 1969:9(3): 1-122 



2. Methods of Change. The Problem of Changing Food Habits. Bulletin Number 108, Washington, v.c.:. National Academy Press, 1943 Gifft, HH., Washbon, MV.. Harrison, GG. Nutrition, Behavior, and Change. Englewood Cliffs, New   
3. Jersey: "Prentice-Hall, Inc., 1872. pp. xiii-xv Schiffman, SS. Mechanisms of Disease, Taste and Smell in Disease. N Engl J Med 1983: 308(21):   
4. 1275-79 Schiffman, SS. and Pasternak, M. Decreased Discrimmination of Food Odors in the Elderly. J   
5. Gerontol 1979; 34(i): 73-79 Bidlack, WR., Kirsch, A., and Meskin, MS. Nutritionai Requirements of the Elderly. Food Tech 1986;   
;6. 40(2): 61-9 Munro, HN., McGandy, RB., Hartz, SC. et al. Protein Nutriture of a Group of Free-living Elderly.   
57. Am J Clin Nutr 1987: 46(4): 586-92 Russell, RM., Krasinski, SD., Samloff, IM. et al. Folic Acid Malabsorption in Atrophic Gastritis:   
58. Compensation by Bacterial Folate Synthesis. Gastroenterology 1986; 91: 1476-82 MacLaughlin, J; and Holick, MF. Aging Decreases the Capacity of Skin to Produce Vitamin D3. J Cli:   
59. Invest 1985: 76: 1536-8 Davis, M., Mawer, EB., Hann, JT. et al. Vitamin D Prophylaxis in the Elderly: A Simple Effective   
60. Method Suitable for Large Populations. Age and Ageing i985: 14: 349-54 Bowman, BB.: Rosenberg, IH. Assessment of the Nutritional Status of the Elderly. Am J Clin Nutr   
61. 1982: 35: 1142-1151 Pelletier, 0. Vitamin C and Cigarette Smokers. Ann NY Acad Sci 1975: 258: 156-68   
62. Sahud, MA. and Cohen, RJ. Effect of Aspirin Ingestion on Ascorbic Acid Levels in Rheumatoid   
63. Arthritis. Lancet 1971: 1(2): 937-8 National Academy of Sciences, Food and Nutrition Board. Recommended Dietary Allowances.   
64. Washington, D.c.: National Academy Press, 1980 Krause, MV. and Mahan, LK. Food, Nutrition and Diet Therapy 7th Edition. Philadelphia,   
65. Pennsylvania: w.B. Saunders Co.. 1984. pp. 182, 327, 441, 605, Wolford, RL.. Harris, SB., and Weindruch, R. Dietary Restriction and Aging: Historical Phases,   
66. Mechanisms, Current Directions. J Nutr, in press Oct., 1987. Drinkwater, BL. The Role of Nutrition and Exercise in Health. Seattle, Washington: Continuing   
67. Dental Education, University of Washington, 1985. pp. 88-92 Nieman. DC. The Sports Medicine Fitness Course. Palo Alto, California:Bull Publishing Co., 1986   
68. Roe, DA. Nutrition and Drug Interactions, Present Knowledge in Nutrition. Washington, D.C.: The   
69. Nutrition Foundation, 1984, pp.797-818 Hartz, Sc., (ed). Drug-Nutrient Interactions, proceedings of the International Conference on   
70. Nutrients, Medicines and Aging. New York: Alan R. Liss, Inc. 1985: 4(1/2). Riggs, BL. and Merton III, LJ. Involution Osteoporosis. N Engl J Med 1986: 314(26): 1676-84 71. Riggs, BL., Wahner, w., Seeman, K., et.al. . Changes in Bone Mineral Density of the Proximal Femur 72. and Spine with Aging. J Clin Invest 1982: 70: 716-723 Kelsey, JL. and Hoffman, S. Risk Factors for Hip Fracture. N Engl J Med 1987: 316(7): 404-6 73. Johnston, Cc., Norton, J., Khairi, MRA., et al. Heterogeneity of Fracture Syndromes in 74. Postmenopausal Women. J Clin Endocrinol Metab 1985: 61(3):551-6 Dhas/nIH. Consensus Development Conference Statement, Osteoporosis. Washington, D.C.: U.S. 75. Government Printing Office, 1984 Assessment of the Risk of Vertebral Fracture in. 76. Buchanan, JR., Myers, C., Greer, RB., et al.. Menopausal Women. J Bone Joint Surg 1987: 69-A(2): 212-17   
77. Hartz. AJ.. Fischer, ME.. Bril. G.. et al, The Association.of Obesity With Joint Pain and. Osteoarthritis in the HANes Data. J Chronic Dis, 1986: 39(4): 311-19   
78. Fernstrom, JD. Acute and Chronic Effects of Protein and Carbohydrate Ingestion on Brain Tryptophan Levels and Serotonin Synthesis. Nut Reviews (Suppl) 1986; 44:25-36   
79. Wurtman, RJ. Ways That Foods Can Affect Ihe Brain. Nutr Reviews (Suppl) 1986: 44: 2-5   
80. Sandstead, HH. Nutrition and Brain Function: Trace Elements. Nutr Reviews (Suppl) 1986:44: 37-41   
81. Pardridge, WM. Blood-Brain Barrier Transport of Nutrients. Nutr Reviews (Suppl) 1986: 44: 15-23   
82. Anderson, Gh., and Brboticky, N. Approaches to Assessing the Dietary Component of the. Diet-Behavior Connection. Nutr Reviews (Suppl) 1986: 44: 42-51   
83. Wheater, RH. Aluminum and Alzheimer's Disease. JAMA 1985: 253(15): 2288   
84. Schaeffer, AE. Nutrition Policies for the Elderly. Am J Clin Nutr 1982; 36: 819-822   
85. U.S. Congress, Office of Technology Assessment. Life-Sustaining Technologies and the Elderly. Washington, D.C.: U.s. Government Printing Office, 1987.   
86. Lipschitz, DA.: and Chernoff, R. Nutritional Care a Growing Issue for Providers. Am Health Care Assoc J Dec 1985: 47-48   
87. Institute for Health and Aging. Health Promotion for the Elderly: Clinical Practice and Community Resource Series. University of California, San Francisco, 1986.   
88. Shoaf, LR. and Kotanchek, NS. Training in Geriatrics for Future Dietitians. J Am Diet Assoc 1987; 87(3): 330-33   
89. Wilson, Sl., Whittington, FJ. Preparing Nutrition Students to Work With the Elderly. J Nutr Ed 1985: 17(2): 44-6   
90. U.S. Senate, Special Committee on Aging.' Developments in Aging: 1986 Volume 3. Washington, D.C.: U.S. Government Printing Office, 1987.   
91. U.S. Congress, office of Technology Assessment. Medicare's Prospective Payment System--Strategies for Evaluating Cost, Quality and Medical Technology. Washington, D.C.: U.S. Government Printing Office, 1985   
92. Prospective Payment Assessment Commisssion. Report and Recommendations to the Secretary, U.S. Department of Health and Human Services, Aprii 1, 1987. Washington, D.C.: Prospective Payment Assessment Commission, 1987   
93. Adamow, CL. and Clipper, AJ. Is prospective payment inhibiting the use of nutrition support. services? Discussion and research implications. J Am Diet Assoc 1985: 85(12):1616-9   
94. Statements of Eleanor Chelimsky, GAo, Judith Wagner, Office of Technology Assessment, and Donald A Young, Prospective Payment Assessment Commission, on "Quality of Care Issues in the Medicare Program" before the U.s. Senate, Committee on Finance, June 3, 1986.   
95. U.S. Senate, Special Committee on Aging. Developments in Aging: 1986 Volume 1. Washington, D.C.: U.S. Government Printing Office, 1987   
96. U.S. General Accounting Office. Medicare: Need to Strengthen Home Health Care Payment Controls an Address Unmet Needs. Washington, D.c.: Government Printing Office, 1986.   
97. Estes, CL. The Aging Enterprise: In Whose Interests?. Int J Health Serv 1986: 16: 243-251   
98. Leveille, GA. and Cloutier, PF. Role of the Food Industry in Meeting the Nutritional Needs of the Elderly. Food Technology 1986: 2: 82-88   
99. Posner, B. and Karachenfels, M. Optimal Nutrition Services for Older Americans, Boston: Mass Dept. of Public Health, 1985   
100. Balsam, A. and Osteraas, G. Instituting A Continuum of Community Nutrition Services:. Massachusetts Elderly Nutrition Programs. J Nutr Eld. accepted for publication in Spring. 1987   
101. Balsam, AL. and Duffy, M.. Elderiy Luncheon Clubs: Bridging the Gap Between Congregate and Home Delivered Meals. J Nutr Eld 1983: 2(4): 31-35   
.02. Steele, MF. and Bryan, JD. Dietary Intake of Homebound Elderly Recipients and Non-Recipients of Home Delivered Meals. J Nutr Eld 1985/6: 5(2): 23-34   
.03. Weimer, JP. The Nutritional Status of the Elderly. J Nutr Eld 1983: 2(4): 17-25   
104. Kirschner Associates, Inc. and Opinion Research Corporation. An Evaluation of the Nutrition Services for the Eiderly, prepared for the Administration on Aging, Dhgs, Washington, D.C.: Government Printing Office, 3 Vols., 1983   
105. Harrill, I., Bowski, M.. and Kyler, A. The Nutritional Status of Congregate Meals Recipients.. Aging 1980: 311, 312 : 36-41   
106. Balsam, A., Osteraas, G., Bass, S., et al. An Evaluation of the Congregate Nutrition Program for the Elderly. Boston: Univ Mass Ger Program, 1985   
107. Yessian, M. and Monier, C. Follow Up on the Home Delivered Meals Program Service Delivery. Assessment. DhHs, Office of the Inspector General, 1982.   
108. American Dietetic Association. ADA Testimony on the 1987 Reauthorization of the Older Americans Act. of 1965. J Am Diet Assoc 1987: 87(7): 943-4   
109. Shannon, B. and Smiciklas-Wright, H. Nutrition Education in Relation to the Needs of the Elderly.. J Nut Ed 1979; 11: 85-89   
110. Axelson, L. and Penfield, MP. Food and Nutrition-Related Attitudes of Elderly Persons Living Alone. J Nut Ed 1983:15(1): 23-27 1l1. Sims, LS. Nutrition Education Research: Reaching Toward the Leading Edge. J Am Diet Assoc (Suppl) 1987: 87(9): 10-18 Communication Theory as a Basis for Nutrition Edueation. J Am Diet Assoc (Suppl) 112. Gillespie, AH. 1987: 87(9): 44-52 113. Fleming. PL. Applications of the Marketing Perspective in Nutrition Education. J Am Diet Assoc (Suppl) 1987: 87(9): 64-8 114. Maloney, SK., Fallon, B., and Wittenberg, CK. Study of Seniors Identifies Attitudes, Barriers to Promoting Their Health. Promot Health 1984; Sept- Oct: 6-8 115. U.s. Senate, Special Committee on Aging. Developments in Aging: 1986 Volume 2-Appendixes. Washington, D.C.: U.S. Government Printing Office, 1987 116. Grotkowski, ML. and Sims, LS. Nutritional Knowledge, Attitudes and Dietary Practices of the Elderly. J Am Diet Assoc 1983; 47: 263-68 117. Aging Health Policy Center. Nutrition Policy and the Elderly, Policy Paper No. 2. San Francisce University of California, 1983 Aging 1980: 311, 312: 17-20 118. Hickman, D. Nutrition Education, Past, Present and Future. Aging 1980; 31l, 312: 17-20 119. Posner, BM., Nutrition Education for Older Americans: National Policy Recommendations. J Am Diet Assoc 1982; 80: 455-8 

"""

# Step 1: 分块
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000,   # 每块最大字符数
    chunk_overlap=100  # 块之间重叠字符数
)
docs = text_splitter.create_documents([big_text])

print(f"分块数量: {len(docs)}")

# Step 2: 生成向量库
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
db = FAISS.from_documents(docs, embeddings)

# Step 3: 创建检索器
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 5})

# Step 4: 问答链
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-4"),   # 替换成你要用的模型
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

# Step 5: 问问题
query = "请问这段文本里，作者是如何描述气候变化对农业的影响？"
result = qa(query)

print("=== 最终答案 ===")
print(result["result"])

print("=== 相关块 ===")
for doc in result["source_documents"]:
    print("---")
    print(doc.page_content[:200])  # 打印部分块内容

