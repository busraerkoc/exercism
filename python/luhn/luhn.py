class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")        

    def valid(self):
        num = self.card_num
        result = 0
        if (not num.isdigit()) or len(num) < 2:
            return False
        for i in range(len(num)):
            if i%2==0:
                result+=int(num[i])*2
                if int(num[i])*2 > 9:
                    result-= 9
            else:
                result+=int(num[i])
        return result%10 == 0
