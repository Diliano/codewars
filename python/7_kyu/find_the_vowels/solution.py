def vowel_indices(word):
    result = []
    vowels = set("aeiouyAEIOUY")
    
    # use enumerate to iterate through each index and character in the given word
    for index, c in enumerate(word):
        # if the current character is a vowel
        if c in vowels:
            # add the current index + 1 to the result, as the kata uses 1-indexing
            result.append(index + 1)
        
    return result