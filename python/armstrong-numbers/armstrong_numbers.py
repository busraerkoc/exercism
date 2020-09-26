def is_armstrong_number(number):
    result=0
    number=str(number)
    for num in number:
        result+=int(num)**len(number)
    if result == int(number):
        return True
    else:
        return False
