def find_it(seq):
    count_dict = {}
    
    # for each value in the given sequence
    for value in seq:
        # if the value already exists as a key in count_dict, increment by 1
        if value in count_dict:
            count_dict[value] += 1
        # otherwise, add the value as a key in count_dict, with a starting value of 1
        else:
            count_dict[value] = 1

    # for each key in the resulting count_dict    
    for key in count_dict:
        # if the current key has an odd count, return it
        if count_dict[key] % 2 != 0:
            return key