def count_words(sentence):
	for word in sentence:
		word = word.lower()
		if word.isalpha():
			return """"{}":{}""".format(word, word.count)
