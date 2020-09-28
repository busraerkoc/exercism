def classify(number):
	sum = 0
	if number == 0 or number == -1: 
		raise ValueError("Error") 
	for i in range(1,number//2+1):
		if number%i == 0:
                        sum+=i
	if sum == number:
		return "perfect"
	elif sum > number:
		return "abundant"
	else:
		return "deficient"
