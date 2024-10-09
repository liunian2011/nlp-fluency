import spacy
import en_core_web_sm


def main():
    nlp = spacy.load('en_core_web_sm')
    ner_categories = ['PERSON', 'ORG', 'GPE', 'PRODUCT']
    text = "The long-term stability of methylammonium lead triiodide (MAPbI3) perovskite in moist environments is a paramount challenge to realise the commercialization of perovskite solar cells. In an attempt to address this concern, we have carried out systematic first-principles studies on the MAPbI3 perovskite with a hydrophobic graphene layer interfaced as a water barrier. We find there is a charge transfer at the graphene/MAPbI3 interface and electrons can be excited from graphene into the perovskite surface, leading to well separated electron–hole pairs, i.e. reduced recombination. By studying the optical properties, we find the hybrid graphene/MAPbI3 nanocomposite displays enhanced light absorption compared with the pristine MAPbI3. Furthermore, from an ab initio molecular dynamics simulation, the graphene/MAPbI3 nanocomposite is confirmed to be able to resist the reaction with water molecules, highlighting a great advantage of this nanocomposite in promoting long-term photovoltaic performance."

    doc = nlp(text)

    #identity and classify named entities
    entities = []
    for ent in doc.ents:
        print('ent:{} label:{}'.format(ent.text, ent.label_))
        if ent.label_ in ner_categories:
            entities.append((ent.text, ent.label_))

    print("======entities=====")
    for entity, category in entities:
        print(f"{entity}:{category}")


def test2():
    nlp = en_core_web_sm.load()
    text = """As sedimentologists study the composition of lake sediments, one key aspect they often examine is the carbonate content. Carbonates, primarily in the form of calcite and aragonite, can provide valuable insights into the paleoenvironmental conditions of a lake. Increases in carbonate content in lake sediments can be attributed to various factors including biological productivity, water chemistry, and climate changes.
During periods of increased biological productivity, organisms such as algae and aquatic plants can contribute to higher carbonate levels through the process of biomineralization. This process involves organisms extracting dissolved inorganic carbon from the water and converting it into carbonate minerals as part of their biological functions.
The water chemistry of a lake also plays a significant role in carbonate deposition. Lakes with higher concentrations of dissolved ions such as calcium and bicarbonate are more conducive to the precipitation of carbonate minerals. This precipitation can be further influenced by factors such as pH levels and water temperature.
Climatic conditions can also impact the carbonate content of lake sediments. For example, warmer temperatures can enhance the rate of chemical weathering of rocks in the lake's drainage basin, leading to increased ion concentrations in the water, which in turn promotes carbonate precipitation. Conversely, cooler temperatures can slow down these processes.
Overall, the study of carbonate content in lake sediments provides sedimentologists with crucial information about the historical conditions of the lake environment, aiding in the reconstruction of past climatic and ecological scenarios."""

    doc = nlp(text)
    for ent in doc.ents:
        print('ent:{} label:{}'.format(ent.text, ent.label_))


if __name__=='__main__':
    #main()
    test2()
