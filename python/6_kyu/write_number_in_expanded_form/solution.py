def expanded_form(num):
    # convert number to a string
    str_num = str(num)
    # initialise a list to store each expanded form
    result = []
    
    # use enumerate to access the index and digit of each value in str_num
    for index, digit in enumerate(str_num):
        # if the current digit is not 0 (skip if 0 as this is not required for expanded form)
        if digit != "0":
            # calculate the power of 10 i.e rightmost digit would be 10^0, with power increasing by 1 each time we move left  
            power = len(str_num) - 1 - index
            # calculate the value of the expanded form
            expanded = int(digit) * (10 ** power)
            # convert expanded form to string and append to the list 
            result.append(str(expanded))
    
    # join the list by a " + " as per the instructions  
    return (" + ").join(result)