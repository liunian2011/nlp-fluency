import time

import openai
from openai import OpenAI

client = OpenAI(api_key="sk-Avu1NSpZvuMReDJJ27BcC6Ff4b024e1c83Ef4cBa52D69e80",
                base_url="https://openai.sohoyo.io/v1")

def chart_with_gpt(input):
    chat_completion = None
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": input}]
        )
    except openai.RateLimitError:
        print('上游负载已饱和.过30s再试.')
        time.sleep(30)
    except openai.InternalServerError:
        print('internal server error.')

    if chat_completion:
        return chat_completion.choices[0].message.content
    else:
        return None


if __name__ == '__main__':
    input_prompt = """Suppose you are a senior medical expert. Please write an article on the topic of food based on relevant facts, and specifically include the concept of machine activity. This article should meet the following requirements: 
1. The content should be novel and related to the field of medical science. 
 2. The content length should be no less than 1,000 words. 
 3. Establish a logical connection between food and machine activity as following:  
food ->mental or behavioral dysfunction ->patient or disabled group ->machine activity
 Here are some examples from other experts:  Example 1: "A virus is a submicroscopic infectious agent that replicates only inside the living cells of an organism. Viruses infect all life forms, from animals and plants to microorganisms, including bacteria and archaea. Viruses are found in almost every ecosystem on Earth and are the most numerous type of biological entity. Since Dmitri Ivanovsky's 1892 article describing a non-bacterial pathogen infecting tobacco plants and the discovery of the tobacco mosaic virus by Martinus Beijerinck in 1898, more than 11,000 of the millions of virus species have been described in detail. The study of viruses is known as virology, a subspeciality of microbiology." 
Example 2: "Deoxyribonucleic acid (DNA) is a polymer composed of two polynucleotide chains that coil around each other to form a double helix. The polymer carries genetic instructions for the development, functioning, growth and reproduction of all known organisms and many viruses. DNA and ribonucleic acid (RNA) are nucleic acids. Alongside proteins, lipids and complex carbohydrates (polysaccharides), nucleic acids are one of the four major types of macromolecules that are essential for all known forms of life. 
The two DNA strands are known as polynucleotides as they are composed of simpler monomeric units called nucleotides. Each nucleotide is composed of one of four nitrogen-containing nucleobases (cytosine [C], guanine [G], adenine [A] or thymine [T]), a sugar called deoxyribose, and a phosphate group. The nucleotides are joined to one another in a chain by covalent bonds (known as the phosphodiester linkage) between the sugar of one nucleotide and the phosphate of the next, resulting in an alternating sugar-phosphate backbone. The nitrogenous bases of the two separate polynucleotide strands are bound together, according to base pairing rules (A with T and C with G), with hydrogen bonds to make double-stranded DNA. The complementary nitrogenous bases are divided into two groups, the single-ringed pyrimidines and the double-ringed purines. In DNA, the pyrimidines are thymine and cytosine; the purines are adenine and guanine. \n Both strands of double-stranded DNA store the same biological information. This information is replicated when the two strands separate. A large part of DNA (more than 98% for humans) is non-coding, meaning that these sections do not serve as patterns for protein sequences. The two strands of DNA run in opposite directions to each other and are thus antiparallel. Attached to each sugar is one of four types of nucleobases (or bases). It is the sequence of these four nucleobases along the backbone that encodes genetic information. RNA strands are created using DNA strands as a template in a process called transcription, where DNA bases are exchanged for their corresponding bases except in the case of thymine (T), for which RNA substitutes uracil (U). Under the genetic code, these RNA strands specify the sequence of amino acids within proteins in a process called translation. \n Within eukaryotic cells, DNA is organized into long structures called chromosomes. Before typical cell division, these chromosomes are duplicated in the process of DNA replication, providing a complete set of chromosomes for each daughter cell. Eukaryotic organisms (animals, plants, fungi and protists) store most of their DNA inside the cell nucleus as nuclear DNA, and some in the mitochondria as mitochondrial DNA or in chloroplasts as chloroplast DNA. In contrast, prokaryotes (bacteria and archaea) store their DNA only in the cytoplasm, in circular chromosomes. Within eukaryotic chromosomes, chromatin proteins, such as histones, compact and organize DNA. These compacting structures guide the interactions between DNA and other proteins, helping control which parts of the DNA are transcribed."""
    output = chart_with_gpt(input_prompt)
    print(f'output:{output}')

