from transformers import GPT2LMHeadModel, GPT2TokenizerFast
from accelerate.test_utils.testing import get_backend

device, _, _ = get_backend() # automatically detects the underlying device type (CUDA, CPU, XPU, MPS, etc.)
model_id = "openai-community/gpt2-large"
model = GPT2LMHeadModel.from_pretrained(model_id).to(device)
tokenizer = GPT2TokenizerFast.from_pretrained(model_id)


from datasets import load_dataset

#test = load_dataset("wikitext", "wikitext-2-raw-v1", split="test")
#print(f'text:{test["text"]}')

my_text = [' Bert Gordon - Nominated Villain \n', " AFI 's 100 Years ... 100 Movie Quotes : \n", ' " Eddie , you \'re a born loser . " - Nominated \n', " AFI 's 100 Years ... 100 Movies ( 10th Anniversary Edition ) - Nominated \n", " AFI 's 10 Top 10 - # 6 Sports Film \n", '', ' = = Legacy = = \n', '', ' In the decades since its release , The Hustler has cemented its reputation as a classic . Roger Ebert , echoing earlier praise for the performances , direction , and cinematography and adding laurels for editor Dede Allen , cites the film as " one of those films where scenes have such psychic weight that they grow in our memories . " He further cites Fast Eddie Felson as one of " only a handful of movie characters so real that the audience refers to them as touchstones . " TV Guide calls the film a " dark stunner " offering " a grim world whose only bright spot is the top of the pool table , yet [ with ] characters [ who ] maintain a shabby nobility and grace . " The four leads are again lavishly praised for their performances and the film is summed up as " not to be missed . " \n', ' Paul Newman reprised his role as Fast Eddie Felson in the 1986 film The Color of Money , for which he won the Academy Award for Best Actor in a Leading Role . A number of observers and critics have suggested that this Oscar was in belated recognition for his performance in The Hustler . In 1997 , the Library of Congress selected The Hustler for preservation in the United States National Film Registry as " culturally , historically , or aesthetically significant . " Carroll and Rossen \'s screenplay was selected by the Writers Guild of America in 2006 as the 96th best motion picture screenplay of all time . In June 2008 , AFI released its " Ten top Ten " — the best ten films in ten " classic " American film genres — after polling over 1 @,@ 500 people from the creative community . The Hustler was acknowledged as the sixth best film in the sports genre . \n', ' The Hustler is credited with sparking a resurgence in the popularity of pool in the United States , which had been on the decline for decades . The film also brought recognition to Willie Mosconi , who , despite having won multiple world championships , was virtually unknown to the general public . Perhaps the greatest beneficiary of the film \'s popularity was a real @-@ life pool hustler named Rudolf Wanderone . Mosconi claimed in an interview at the time of the film \'s release that the character of Minnesota Fats was based on Wanderone , who at the time was known as " New York Fatty " . Wanderone immediately adopted the Minnesota Fats nickname and parlayed his association with the film into book and television deals and other ventures . Author Walter Tevis denied for the rest of his life that Wanderone had played any role in the creation of the character . Other players would claim , with greater or lesser degrees of credibility , to have served as models for Fast Eddie , including Ronnie Allen , Ed Taylor , Ed Parker , and Eddie Pelkey . \n', '']
#encodings = tokenizer("\n\n".join(test["text"]), return_tensors="pt")
#encodings = tokenizer("\n\n".join(my_text), return_tensors="pt")

#text = """## Understanding the Relationship between Grainstone and Packstone in Sedimentary Layers\n\nIn the discipline of sedimentology, unraveling the intricacies of rock formation and layering provides invaluable insights into past depositional environments and geological processes. Among the different types of carbonate rocks, grainstone and packstone stand out due to their distinctive characteristics and the unique insights they offer into sedimentological and diagenetic histories. This article delves into the relationship between these two rock types, with a focus on the occurrence of grainstone within packstone units and the alternation of packstone with grainstone layers."""
#text = """Title: Integrative Roles of Fish Social Behavior and Clinical Attributes in Understanding Cellular Functions\n\nAbstract: \nThis article explores the intricate relationship between unique social behaviors exhibited by fish, their consequential clinical attributes, and the specific cellular functions they influence. The study analyzes various social interactions among fish species and their implications on health and disease at the cellular level. The review aims to elucidate potential benefits and mechanisms through which understanding fish behavior can contribute toward medical science, particularly in terms of cellular processes like cell communication, immunity, and regeneration.\n\nIntroduction:\nFish are a diverse group of organisms that exhibit a wide range of social behaviors, from solitary existences to complex interactions within shoals and schools. These behaviors are not only fundamental for their survival but also have profound implications on their physiological health and overall wellbeing. The social structure can influence clinical attributes which, in turn, affect cellular functions crucial for health and disease. Understanding these interactions opens up novel approaches to human medical research, especially in terms of preventive and therapeutic strategies derived from bio-inspiration and comparative medicine.\n\nFish Social Behavior and its Impact:\nFish, as social animals, communicate and interact within their environments in ways that are critical for their survival, such as foraging, predator avoidance, and reproduction. Social hierarchies and behaviors such as aggression, schooling, and mating rituals can affect their stress levels, immune responses, and other physiological aspects. Studies have shown that social isolation or overcrowded environments can lead to higher cortisol levels, indicative of stress, which directly impacts fish immune systems at the cellular level.\n\nLink Between Clinical Attributes and Cell Function:\nClinical attributes in fish, such as stress responses, growth rates, and susceptibility to diseases, are deeply intertwined with cellular functionality. For instance, long periods of stress not only affect the neuroendocrine system but also impact cellular immunity. Lymphocytes and macrophages show altered activities under stress, leading to modified responses to pathogens and diseases. Additionally, fish schooling behavior has been linked with synchronized cell processes, including metabolism and gene expression, due to the need for homogeneity within groups.\n\nCellular Functions Influenced by Fish Behavior:\nOne of the key cellular functions influenced by fish behavior is cell communication, essential for maintaining homeostasis and responding to environmental stimuli. The neuro-immunological interface in fish showcases how stress and social interactions can modulate neurotransmitter levels and cytokine production, thereby influencing cellular communication pathways. Moreover, the phenomenon of cellular regeneration in fish, especially noticeable in species like zebrafish which can regenerate their hearts, is highly influenced by both intrinsic (genetic) and extrinsic (environmental) factors, including social interactions.\n\nNovel Medical Insights Gained from Fish Studies:\nUnderstanding fish social behavior and its impacts on cell function has myriad applications in medical science. For instance, by studying the mechanisms of cellular regeneration in zebrafish, researchers can explore new avenues for tissue regeneration in humans. The social dependency of certain metabolic processes in fish can also enlighten pathways to investigate metabolic disorders in humans. Furthermore, the stress and immune responses modulated by social interactions in fish provide a comparative basis to study similar phenomena in human psycho-neuroimmunology.\n\nConclusion:\nIn conclusion, fish and their complex social behaviors offer a unique window into the interconnected relationship between behavior, clinical attributes, and cellular function. By exploring these links, medical researchers can not only gain deeper insights into cellular processes but also explore potential therapeutic and preventive measures derived from these studies. Future research should focus on more in-depth molecular mechanisms and potential applications of these discoveries in human health sciences, paving the way for innovative cross-disciplinary medical advancements. The study of fish, therefore, becomes not just an exploration of ecological interest but a promising frontier in medical science.\n\nReferences:\n[1] Scholarly articles and research studies on fish behavior and its physiological impacts.\n[2] Clinical studies on stress, immunity, and cellular functions in marine organisms.\n[3] Reviews on comparative medicine and bio-inspired medical approaches."""
#text = """## The Relationship between Grainstone and Packstone Units in Sedimentology\n\nAs a geoscientist, understanding and characterizing distinctive rock formations is critical to properly unraveling the geological history of an area. This article aims to discuss two particular types of rock units in the discipline of sedimentology: grainstone and packstone, also highlighting the fact that grainstone is encountered within packstone units.\n\nSedimentologists often use the Dunham texture classification system to categorize carbonate sediments such as grainstone using factors like grain texture and the amount of interstitial material. Grainstone is defined by Robert L. Folk, a renowned sedimentologist, as a carbonate rock solely made of grains and is devoid of any mud. """
text = """my name is Jone."""
text = """good morning to you."""
text = """new to Medium, create a new account ,story available, account."""
text = """ times, quantities, monetary values, percentages, etc. In this blog."""
text = "This article aims to discuss two particular types of rock units in the discipline of sedimentology: grainstone and packstone, also highlighting the fact that grainstone is encountered within packstone units."
text = "Sedimentologists often use the Dunham texture classification system to categorize carbonate sediments such as grainstone using factors like grain texture and the amount of interstitial material."

encodings = tokenizer(text, return_tensors="pt")

#print(f'encodings:{encodings}')

import torch
from tqdm import tqdm

#print(f'mode config:{model.config}')
max_length = model.config.n_positions
stride = 512
seq_len = encodings.input_ids.size(1)

nll_sum = 0.0
n_tokens = 0
prev_end_loc = 0
print(f'seq_len:{seq_len}, stride:{stride}')
for begin_loc in tqdm(range(0, seq_len, stride)):
    print(f'begin_loc:{begin_loc}')
    end_loc = min(begin_loc + max_length, seq_len)
    trg_len = end_loc - prev_end_loc  # may be different from stride on last loop
    input_ids = encodings.input_ids[:, begin_loc:end_loc].to(device)
    target_ids = input_ids.clone()
    target_ids[:, :-trg_len] = -100

    with torch.no_grad():
        outputs = model(input_ids, labels=target_ids)

        # loss is calculated using CrossEntropyLoss which averages over valid labels
        # N.B. the model only calculates loss over trg_len - 1 labels, because it internally shifts the labels
        # to the left by 1.
        neg_log_likelihood = outputs.loss

    # Accumulate the total negative log-likelihood and the total number of tokens
    num_valid_tokens = (target_ids != -100).sum().item()  # number of valid tokens in target_ids
    batch_size = target_ids.size(0)
    num_loss_tokens = num_valid_tokens - batch_size  # subtract batch_size due to internal label shift
    nll_sum += neg_log_likelihood * num_loss_tokens
    n_tokens += num_loss_tokens

    prev_end_loc = end_loc
    if end_loc == seq_len:
        break

avg_nll = nll_sum / n_tokens  # average negative log-likelihood per token
print('start torch exp.')
ppl = torch.exp(avg_nll)
print(f'ppl:{ppl}')
