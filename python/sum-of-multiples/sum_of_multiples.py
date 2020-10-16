def sum_of_multiples(limit, multiples):
    result = []
    for multiple in multiples:
        if multiple > 0:
            for i in range(multiple,limit, multiple):
                if i not in result:
                    result.append(i)
    return sum(result)
