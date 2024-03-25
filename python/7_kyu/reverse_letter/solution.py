def reverse_letter(s):
    # use list comprehension to build a list of only letters
    filtered = [c for c in s if c.isalpha()]
    
    # join the list into a string and use slicing to reverse it
    return ("").join(filtered)[::-1]