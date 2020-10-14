def proteins(strand):
    protein = {'Methionine': ['AUG'], 'Phenylalanine': ['UUU', 'UUC'], 'Leucine': ['UUA', 'UUG'], 'Serine': ['UCU', 'UCC', 'UCA', 'UCG'], 'Tyrosine': ['UAU', 'UAC'], 'Cysteine': ['UGU', 'UGC'], 'Tryptophan': ['UGG'], 'STOP': ['UAA', 'UAG', 'UGA']}
    result = []
    for i in range(0,len(strand)-2,3):
        if strand[i:i+3] in protein.get('STOP'):
            break
        for key, value in protein.items():
            if strand[i:i+3] in value:  
                result.append(key)
    return(result)
