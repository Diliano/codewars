def is_isogram(string):
    count_dict = {}
    
    # iterate through each character in the given string
    for c in string:
        # convert the character to lowercase
        c = c.lower()
        # if the character is found in count_dict, return False as there is a repeating character
        if c in count_dict:
            return False
        else:
            # otherwise, add the character to count_dict with a value of 1
            count_dict[c] = 1
    
    # if the above completes without returning False (by finding a character that already exists in count_dict)
    # return True as the given string must be an Isogram
    return True