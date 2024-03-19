def DNA_strand(dna):
    complements = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    
    result = []
    
    for symbol in dna:
        result.append(complements[symbol])
        
    return ("").join(result)