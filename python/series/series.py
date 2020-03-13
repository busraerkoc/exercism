def slices(series, length):
        if len(series) < length or length <= 0 or len(series) < 0:
            raise ValueError("Error")
        return [series[k:length+k] for k in range(len(series)) if length+k < len(series)+1]

