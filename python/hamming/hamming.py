def distance(strand_a, strand_b):
	hamming_dist = 0
	if (len(strand_a) != len(strand_b)):
		raise ValueError("Error")
	else:
		for i in range(len(strand_a)):
			if strand_a[i] != strand_b[i]:
				hamming_dist += 1
	return hamming_dist
