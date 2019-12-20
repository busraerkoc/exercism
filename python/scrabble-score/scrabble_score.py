def score(word):
	u_word = word.upper()
	w_len = len(u_word)
	point_1 = ['A','E','I','O','U','L','N','R','S','T']
	point_2 = ['D','G']
	point_3 = ['B','C','M','P']
	point_4 = ['F','H','V','W','Y']
	point_5 = ['K']
	point_8 = ['J','X']
	point_10 = ['Q','Z']
	score = 0
	for i in range(w_len):
		if u_word[i] in point_1:
			score+=1
		elif u_word[i] in point_2:
			score+=2
		elif u_word[i] in point_3:
			score+=3
		elif u_word[i] in point_4:
			score+=4
		elif u_word[i] in point_5:
			score+=5
		elif u_word[i] in point_8:
			score+=8
		else: 
			if u_word[i] in point_10:
				score+=10
	return score
