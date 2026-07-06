from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
text = "Hello! How are you doing today?"
print(word_tokenize(text))

symbol = "john.doe@email.com"
print(word_tokenize(symbol))


text = "Hello everyone. Welcome to GeeksforGeeks. You are studying NLP article."
print(sent_tokenize(text))


corpus = ["Machine learning models require large datasets.","Artificial intelligence is changing the world.",
    "Neural networks are inspired by the human brain.","Deep learning is a subset of machine learning.",
    "Data preprocessing is essential for better accuracy."]

tokenized_corpus = [word_tokenize(sentence) for sentence in corpus]

print("Generated Tokens: ")
for i, tokens in enumerate(tokenized_corpus):
    print(f"Sentence {i+1} tokens:", tokens)