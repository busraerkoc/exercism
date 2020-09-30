def prime(number):
    prime_l = [2, 3, 5, 7, 11, 13]
    if number <= len(prime_l):
        return list[number-1]
    else:
        num = 13
        while len(prime_l) < number:
            cnt=0
            num+=1
            for k in range(2, num):
                if num%k==0:
                    cnt+=1
            if cnt==0:
                    prime_l.append(num)
    return prime_l[number-1]

