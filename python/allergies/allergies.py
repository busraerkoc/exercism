
class Allergies:

    def __init__(self, score):
        self.score = score % 256          	#scores
        self.allergens = ['eggs','peanuts','shellfish', 'strawberries', 'tomatoes','chocolate', 'pollen' ,'cats']

    def allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        allergens_list = []
        scores = [1, 2, 4, 8, 16, 32, 64, 128]
        for i in range(len(self.allergens), -1, -1):
            if self.score in scores:
                allergens_list.append(self.allergens[scores.index(self.score)])
                self.score -=2**(scores.index(self.score))
            elif self.score >= 2**i:
                allergens_list.append(self.allergens[i])
                self.score -= 2**i
            else: 
                continue
        return allergens_list

