import math
def cipher_text(plain_text):
    if plain_text == "":
        return ""
    result = ""
    normalized = "".join(i.lower() for i in plain_text if i.isalnum())
    c = math.ceil(math.sqrt(len(normalized)))   # columns
    r = math.ceil(len(normalized) / c )  # rows
    if len(normalized) < 2:
        result = ''.join([normalized[i::c] for i in range(c)])
    else:
        result = ''.join([normalized[i::c]+" " for i in range(c)])
    return result.rstrip()
