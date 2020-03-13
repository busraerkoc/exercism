from math import ceil, sqrt
def cipher_text(plain_text):
	normalized = "".join(i.lower() for i in plain_text if i.isalnum())
	length = len(normalized)
	c = ceil(sqrt(lenght))
	r = ceil(lenght/c)
	last = 0
	last = []
	k = 0
	last = c
	while last < length+c:
		list.append(normalized[k:last])
		k = last
		last +=c
	for i in r:
 		new = list
