def find_fewest_coins(coins, target):
	result = []
	if target == 0:
		return result
	fewest = target % coins[-1]
	count = int(target/coins[-1])
	reverse = coins[::-1]
	if fewest == 0: 
		for i in range(count-1):
			result.append(coins[-1])
		return result
	else: 
		for i in range(count - 1):
			result.append(coins[-1])
		for i in reverse:
			if fewest == i:
				result.append(i)
		return result	
 	
		
