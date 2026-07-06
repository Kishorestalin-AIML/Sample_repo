import spacy as sp

nlp = sp.load("en_core_web_sm")
doc = nlp("Tokenization is important in NLP.")
print([token.text for token in doc])