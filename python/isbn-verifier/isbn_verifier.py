def is_valid(isbn): 
    result = 0
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
    last = -1
    if isbn[-1] == "X":
        isbn = isbn.replace("X", "")
        result+=10
        last = 0
    if isbn.isdigit():
        for i in range(9, last, -1):
            result+=(int(isbn[9-i])*(i+1))
        return result%11==0
    else:
        return False
