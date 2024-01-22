def string_clean(s):
    # use filter and lambda functions to return 'True' for characters that are non-numeric within the given string (filtering out all numeric characters)
    # use join to concatenate the filtered characters back into a string 
    return ("").join(filter(lambda c: not c.isnumeric(), s))