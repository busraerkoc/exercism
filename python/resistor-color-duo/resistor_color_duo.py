def value(colors):
    coding = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    result = ""
    for i in range(2):
        result += str(coding.index(colors[i]))

    return int(result)
