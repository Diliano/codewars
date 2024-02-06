def is_isogram(string):
    # first solution below
    # iterate through each character in the given string, converting each to lowercase
    # if the character is found in count_dict, return False as the character is repeating
    # otherwise add the character to count_dict with a value of 1
    # if the loop completes without returning False, return True as the string must be an Isogram
        # count_dict = {}
        # for c in string:
        #     c = c.lower()
        #     if c in count_dict:
        #         return False
        #     else:
        #         count_dict[c] = 1
        # return True
    

    # refactored to create a set from the given string after being converted to lowercase
    # the set is a collection of the unique values i.e "HiHi" would become {"h", "i"}
    string_set = set(string.lower())
    
    # compare the length of the given string and the set
    # if the lengths are equal, the string must be an Isogram and otherwise is not
    return len(string) == len(string_set)