def longest(a1, a2):
    # combine the input strings and convert them to a set to remove all duplicates
    # convert the set into a list, ready for sorting
    result = list(set(a1 + a2))
    
    # sort the list
    result.sort()
    
    # combine the list into the string result as required
    return ("").join(result)