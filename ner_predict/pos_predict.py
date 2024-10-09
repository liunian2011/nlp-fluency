from flair.data import Sentence
from flair.nn import Classifier
from flair.splitter import SegtokSentenceSplitter
from flair.models import SequenceTagger

# load tagger
tagger = SequenceTagger.load('ner')
pos_tagger = SequenceTagger.load("flair/pos-english")

def nount_statis(paragram, word_entity_set=None):
    sentence = Sentence(paragram)
    # predict ner and pos tags
    pos_tagger.predict(sentence)

    noun_pos_list = ['NN', 'NNS']
    noun_set = set()
    nouns_set = set()
    for entity in sentence:
        #print('{}:{}'.format(entity.text, entity.tag))
        if entity.tag == 'NNS':
            nouns_set.add(entity.text.lower())
        if entity.tag == 'NN' or entity.tag == 'NNP':
            noun_set.add(entity.text.lower())

        #if entity.tag in noun_pos_list:
        #    noun_set.add(entity.text)

    nouns_to_noun_set = transfer_nouns_to_noun(list(nouns_set))

    print('所有名词数:{}'.format(len(noun_set.union(nouns_to_noun_set))))
    print('所有名词列表:{}'.format(noun_set.union(nouns_to_noun_set)))
    total_words_count = len(paragram.split())
    print('所有单词数:{}'.format(total_words_count))

    expected_nount_set = noun_set.union(nouns_to_noun_set)
    if word_entity_set:
        word_entity_set_str = ' '.join(word_entity_set)
        print('word_entity_set_str:{}'.format(word_entity_set_str))
        word_entity_to_noun_set = transfer_sentence_to_noun_setence(word_entity_set_str)
        print('word_entity_to_noun_set:{}'.format(word_entity_to_noun_set))
        expected_nount_set = noun_set.union(nouns_to_noun_set) - word_entity_to_noun_set

    print('排除word entity后名词数:{}'.format(len(expected_nount_set)))
    percent = round(len(expected_nount_set) * 100/total_words_count, 2)
    print('排除word entity后名词数比例:{}%'.format(percent))


def transfer_sentence_to_noun_setence(paragram):
    sentence = Sentence(paragram)
    # predict ner and pos tags
    pos_tagger.predict(sentence)

    noun_set = set()
    for entity in sentence:
        #print('{}:{}'.format(entity.text, entity.tag))
        if entity.tag == 'NNS':
            nouns = entity.text.lower()
            noun = nouns[:-1]
            noun_set.add(noun)
        if entity.tag == 'NN' or entity.tag == 'NNP':
            noun_set.add(entity.text.lower())

    return noun_set
def transfer_nouns_to_noun(nouns_list:set):
    noun_list = set()
    if nouns_list:
        for nouns in nouns_list:
            if nouns.endswith('s'):
                noun = nouns[:-1]
                noun_list.add(noun)
            else:
                noun_list.add(nouns)

    return noun_list


def pos_compare():
    pre_prompt = """As sedimentologists study the composition of lake sediments, one key aspect they often examine is the carbonate content. Carbonates, primarily in the form of calcite and aragonite, can provide valuable insights into the paleoenvironmental conditions of a lake. Increases in carbonate content in lake sediments can be attributed to various factors including biological productivity, water chemistry, and climate changes.
During periods of increased biological productivity, organisms such as algae and aquatic plants can contribute to higher carbonate levels through the process of biomineralization. This process involves organisms extracting dissolved inorganic carbon from the water and converting it into carbonate minerals as part of their biological functions.
The water chemistry of a lake also plays a significant role in carbonate deposition. Lakes with higher concentrations of dissolved ions such as calcium and bicarbonate are more conducive to the precipitation of carbonate minerals. This precipitation can be further influenced by factors such as pH levels and water temperature.
Climatic conditions can also impact the carbonate content of lake sediments. For example, warmer temperatures can enhance the rate of chemical weathering of rocks in the lake's drainage basin, leading to increased ion concentrations in the water, which in turn promotes carbonate precipitation. Conversely, cooler temperatures can slow down these processes.
Overall, the study of carbonate content in lake sediments provides sedimentologists with crucial information about the historical conditions of the lake environment, aiding in the reconstruction of past climatic and ecological scenarios."""

    after_prompt = """In sedimentology, the study of lake sediments yields important insights into past climatic and environmental conditions. One key aspect of this research is the observation of carbonate content in these sediments. It is well-documented that carbonate content tends to increase over time in certain lake sediments, and understanding the factors that drive this increase is essential for reconstructing historical environmental changes.
The increase in carbonate content can be influenced by various factors such as the water chemistry, biological activity, and hydrodynamic conditions of the lake. For instance, in lakes where there is strong tidal current, the agitation of the water can promote the precipitation of carbonate minerals. Additionally, the presence of certain microbial communities also plays a significant role in the deposition of carbonate minerals. These communities can form layered thrombolite structures, which are organo-sedimentary deposits that are usually found in shallow water environments with moderate to high water agitation.
The formation of these layered thrombolite structures is a complex process that includes the interaction of microorganisms, such as cyanobacteria, with the surrounding sediment and water chemistry. The microbial activity is embedded in the sedimentary record, and as these microbes photosynthesize and metabolize, they induce changes in the water chemistry that promote the precipitation of carbonates. Over time, as layer upon layer of microbial mats and trapped sediment accumulate, the carbonate content within the lake sediments increases.
In sedimentological studies, examining the composition and structure of lake sediments, including variations in carbonate content, provides valuable clues to the historical conditions of the lake. By studying the patterns and processes, such as the formation of layered thrombolites and the influence of tidal currents, scientists can better understand the environmental dynamics that have occurred over geological time scales. This knowledge is crucial for predicting future environmental changes and managing water resources effectively."""

    nount_statis(pre_prompt)
    print('==after enlarge==')
    nount_statis(after_prompt)


if __name__=='__main__':
    pos_compare()
