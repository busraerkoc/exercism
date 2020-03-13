class Cipher:
	def __init__(self, key=None):
        	self.alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
		self.revalphabet = ['Z','

	def encode(self, text):
        	for i in len(text):
			index = self.alphabet.index(text[i])
			text[i] = self.revalphabet[index]
		return text
	def decode(self, text):
        	for i in len(text):
			index = self.revalphabet(text[i])
			text[i] = self.alphabet[index]
		return text

