def disemvowel(string_):
    filtered = [c for c in string_ if c not in "aeiouAEIOU"]
    
    return ("").join(filtered)