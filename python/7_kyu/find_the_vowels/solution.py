def vowel_indices(word):
    result = []
    vowels = set("aeiouyAEIOUY")
    
    for index, c in enumerate(word):
        if c in vowels:
            result.append(index + 1)
        
    return result