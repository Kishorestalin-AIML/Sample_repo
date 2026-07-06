#Removeal of the stopwords 
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "This is a sample sentence showing stopword removal."

stop_words = set(stopwords.words('english'))
tokens = word_tokenize(text.lower())

filtered_tokens = [word for word in tokens if word not in stop_words]

print("Original:",tokens)
print("Filtered:",filtered_tokens)


#Remove the punctuation 
text = "Hello! Welcome to NLP, using NLTK."

tokens = word_tokenize(text)

clean_text = [
    word for word in tokens
    if word.isalnum()
]

print(' '.join(clean_text))

