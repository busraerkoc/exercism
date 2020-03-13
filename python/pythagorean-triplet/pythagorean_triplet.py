
import math
def triplets_with_sum(number):
	triplets = []
	for b in range(number):
		for a in range(1, b):
			c = math.sqrt(a**2 + b**2)
			if (a + b + c) == number:
					triplets.append([a, b, c])	
	return triplets

def triplets_in_range(start, end):
    pass


def is_triplet(triplet):
	a, b, c = triplet 
	return (a**2 + b**2 == c**2) and a < b < c

