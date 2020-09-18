def square(number):
    if ( number <= 0 or number > 64):
        raise ValueError("Error")
    else:
        return 2**(number-1) 


def total():
    return (2**(64-1))*2 - 1
