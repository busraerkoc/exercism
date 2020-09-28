def latest(scores):
	return scores[-1]

def personal_best(scores):
        return max(scores)

def personal_top_three(scores):
        score =  sorted(scores, reverse = True)
        return score[:3]
