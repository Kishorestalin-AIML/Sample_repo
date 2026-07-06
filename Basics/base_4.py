from nltk.stem import PorterStemmer

port_stemmer = PorterStemmer()

words = ["running", "jumps", "happily", "running", "happily"]

stemming  = [port_stemmer.stem(word) for word in words]

print("Original:",words)
print("Stemming:",stemming)
