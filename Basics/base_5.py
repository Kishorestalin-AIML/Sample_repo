from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemma = WordNetLemmatizer()
text = "Kishore loves Dhivya more than He loved his friends"

tokens  = word_tokenize(text)

lemma_words = [lemma.lemmatize(word) for word in tokens]

print("Oringal:",text)
print("Lemma",lemma_words)