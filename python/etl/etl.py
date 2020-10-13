def transform(legacy_data):
    result = {}
    for key, value in legacy_data.items():
        for i in value:
            result[i.lower()] = key
    return result
