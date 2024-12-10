from flair.data import Sentence
from flair.nn import Classifier
from flair.splitter import SegtokSentenceSplitter
from flair.models import SequenceTagger
from collections import Counter

# load tagger
#tagger = SequenceTagger.load('ner')
pos_tagger = SequenceTagger.load("flair/pos-english")

def nount_statis(paragram, word_entity_set=None):
    print('word entity set:{}'.format(word_entity_set))

    paragram = paragram.lower()
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

    total_words_set = set(paragram.split())
    print('所有单词去重数:{}'.format(len(total_words_set)))

    expected_nount_set = noun_set.union(nouns_to_noun_set)
    if word_entity_set:
        word_entity_set_str = ' '.join(word_entity_set)
        #print('word_entity_set_str:{}'.format(word_entity_set_str))
        word_entity_to_noun_set = transfer_sentence_to_noun_setence(word_entity_set_str)
        print('word_entity_to_noun_set:{}'.format(word_entity_to_noun_set))
        expected_nount_set = noun_set.union(nouns_to_noun_set) - word_entity_to_noun_set

    print('排除word entity后名词数:{}'.format(len(expected_nount_set)))
    percent = round(len(expected_nount_set) * 100/total_words_count, 2)
    print('排除word entity后名词数比例:{}%'.format(percent))

    percent1 = round(len(noun_set.union(nouns_to_noun_set)) * 100/total_words_count, 2)
    print('不排除word entity后名词数比例:{}%'.format(percent1))
    percent2 = round(len(expected_nount_set) * 100/len(total_words_set), 2)
    print('排除word entity后名词数占比所有单词去重的比例:{}%'.format(percent2))
    return percent, total_words_set, expected_nount_set


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
    pre_prompt = """The Connection Between Food, Mental or Behavioral Dysfunction, and Machine Activity in Medical Rehabilitation\n\nIn the realm of medical science, the relationship between food consumption and mental and physical health has long been established. However, recent advancements in technology have introduced the concept of machine activity in the management and rehabilitation of patients with mental or behavioral dysfunctions related to dietary habits. This article aims to explore the interrelation among diet, dysfunction, patient care and machine-assisted activities within a medical context.\n\nNutrition and Mental Health: An Overview\nFood serves as the primary source of energy and nutrients necessary for overall health. Studies have consistently shown that diets lack essential nutrients predispose individuals to a variety of physical health problems; similarly, nutrition plays a crucial role in mental health. Several research findings have shown that deficiencies in certain nutrients such as omega-3 fatty acids, vitamins, and minerals can lead to mental and behavioral disorders like depression, schizophrenia, attention deficit hyperactivity disorder (ADHD), and Alzheimer\u2019s disease.\n\nThe role of dietary patterns, including the consumption of high-sugar and high-fat diets, has also been linked with the alteration of behavior and cognitive functions. These dietary patterns can induce inflammation and oxidative stress, exacerbating mental disorders or leading to the development of neurological dysfunction.\n\nDiet-Induced Behavioral Dysfunctions and Patient Populations\nWhen diet influences brain functioning, it can lead to a range of mental or behavioral dysfunctions which could vary from mild cognitive impairments to severe cases of depression and psychotic disorders. Patients with these conditions often require a broad spectrum of interventions including medical, nutritional, and increasingly, technological interventions.\n\nIn particular, dietary-induced disorders such as eating disorders including anorexia and bulimia nervosa do not only affect mental health but also cause severe physical health complications. These conditions require comprehensive treatment strategies that often involve multiple healthcare professionals.\n\nMachine Activity in the Rehabilitation of Patients\nIn the evolving field of medical technology, machine activity has been innovatively used to support the rehabilitation of patients suffering from diet-related mental or behavioral dysfunctions. Machine activity in this context primarily relates to the use of medical or therapeutic machines that assist in monitoring, managing and sometimes even improving patient conditions.\n\nOne such example of machine activity is the use of virtual reality (VR) therapy in treating eating disorders. VR environments can simulate real-life situations that can be used therapeutically to teach patients new behavioral and coping strategies. It allows for controlled exposure to food-related cues and the practice of correct dietary behaviors in a safe, controlled setting.\n\nAnother area where machine activity is contributing is through biofeedback mechanisms. Biofeedback machines help patients gain greater awareness and control over physiological functions that may be altered due to dietary deficiencies, such as brain activity correlations with emotional disturbances or anxiety. Through sensors and monitors, these machines provide real-time feedback to patients about their brain waves, heart rate, or other relevant physiological responses and enable adjustments through guided mental exercises.\n\nFurthermore, robotic-assisted therapy has been incorporated in rehabilitation approaches especially for physical ailments resulting from severe eating disorders or nutritional deficiencies. These robotic systems assist in completing movements and tasks, promoting physical strength and the relearning of motor skills while reducing the burden on human therapists.\n\nThe Use of AI and Big Data in Understanding Food-Induced Dysfunctions\nArtificial intelligence (AI) and big data are increasingly being utilized to decode complex interactions between diet and mental health. Predictive analytics from machine learning algorithms can identify at-risk individuals based on dietary patterns and genetic predispositions. This advancement enables customization in therapeutic interventions, potentially predicting the onset of dysfunction before it fully manifests.\n\nConclusion\nThe incorporation of machine activity into the diagnosis, management, and rehabilitation of dietary-related mental or behavioral dysfunctions marks a cutting-edge merger between technology and traditional medical science. As these applications continue to expand, they offer promising avenues for innovating patient care and treatment effectiveness. By embracing these technological advancements, healthcare practitioners can enhance the evaluation and delivery of needed treatments, ultimately leading to better patient outcomes and improved quality of life. Through the synergy between food, dysfunction understanding, patient rehabilitation, and machine activity, the potential to revolutionize medical approaches is vast and promising."""
    nount_statis(pre_prompt)

if __name__=='__main__':
    pos_compare()
