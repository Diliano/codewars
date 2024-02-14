def solution(s):
    # initialise an empty list
    # list rather than string to avoid repeatedly creating new strings with concatenation
    result = []
    
    # loop through each character in the given string
    for c in s:
        # if the current character is uppercase, add the character to the list with a space beforehand
        if c.isupper():
            result.append(f" {c}")
        else:
            # otherwise, add the character to the list as is
            result.append(c)
            
    # join the list elements together and return
    return ("").join(result)