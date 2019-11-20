def is_isogram(string):
	string = string.lower()
	for i in string:	
		if i.isalpha():
			if string.count(i) > 1:
				return False	
	return True
