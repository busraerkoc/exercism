import re
from collections import Counter
def count_words(sentence):
    sentence = sentence.replace("_", " ")
    sentence = sentence.replace(",", " ")
    sentence = sentence.lower().split()
    words = [word.strip(",'.:!@%&^!$") for word in sentence]
    return Counter(words)
