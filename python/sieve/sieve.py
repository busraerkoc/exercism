def check_prime(num, all):
    for j in all:
        if num % j == 0:
            return 0
    return 1

def primes(limit):
    result = []
    if limit > 1 :
        result.append(2)
        if limit > 2:
            for i in range(3, limit+1, 2):
                if check_prime(i, result):
                    result.append(i)
    return result

