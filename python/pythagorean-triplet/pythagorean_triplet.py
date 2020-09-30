def triplets_with_sum(number):
    triplets = []
    for a in range(number//2):
        for b in range(a, number//2):
            c = number - a - b
            if (a < b < c) and (a**2 + b**2 == c**2):
                triplets.append([a, b, c])
    return triplets
