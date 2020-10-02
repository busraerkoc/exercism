def steps(number):
    step = 0
    if number <= 0:
        raise ValueError("Error")
    while number != 1:
        if number % 2 == 0:
            number/=2
        else:
            number=(number*3)+1
        step+=1
    return step
