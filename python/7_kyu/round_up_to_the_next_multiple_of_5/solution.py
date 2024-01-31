def round_to_next5(n):
    # return n if already a multiple of 5
    if n % 5 == 0:
        return n
    
    # if not already a multiple of 5, find the remainder when divided by 5
    # calculate the difference between 5 and the remainder, before adding this to n 

    # for example, where n = 8 the remainder when divided by 5 is 3 
    # the difference between 5 and 3 is 2, therefore we calculate n + 2 to find the next multiple of 5 when rounded up (10)
    return n + (5 - (n % 5))