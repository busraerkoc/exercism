def is_pangram(sentence):
	sentence = sentence.lower()
	alph = "abcdefghijklmnopqrstuvwxyz"
	for ch in alph:
		if ch not in sentence:
			return False
	return True	
