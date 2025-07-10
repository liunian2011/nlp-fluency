from datatrove.utils.lid import FT176LID
from datatrove.data import Document


def language_predict(text:str):
    model = FT176LID(['en'])
    content = Document(text=text, id=1)
    best_lang_pair, lang_pairs = model.predict(content)
    lang, lang_score = best_lang_pair
    return lang, lang_score

if __name__ == '__main__':
    text = "this is a cat."
    print(language_predict(text))