def shortcut(s):
    # use list comprehension to create a list of characters found in the given string, providing that they are not 'a', 'e', 'i', 'o' or 'u'
    result = [c for c in s if c not in "aeiou"]
    
    return ("").join(result)