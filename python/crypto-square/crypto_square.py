import math
def cipher_text(plain_text):
    normalized = "".join(i.lower() for i in plain_text if i.isalnum())
    c = math.ceil(math.sqrt(len(normalized)))   # columns
    r = len(normalized) / c    # rows
    new = ''.join([normalized[i::c] for i in range(c)])
    return new
