import math
def largest_product(series, size):
    if size < 0 or len(series) < size:
        raise ValueError("Error")
    if size == 0:
        return 1
    series = [ int(x) for x in series ]
    result = 0
    if len(series) == size:
        return math.prod(series)
    for i in range(len(series)-size+1):
        if (math.prod(series[i:(i+size)]) > result):
                result = math.prod(series[i:i+size])
    return result
