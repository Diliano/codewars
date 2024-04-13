def power_of_two(x):
    # return False for 0 as it is not a power of 2
    if x == 0:
        return False
    
    # return True for 1 as it is a power of 2 (2^0)
    if x == 1:
        return True
    
    # while x is an even number
    while x % 2 == 0:
        # divide x by 2
        x //= 2
    
    # after all divisions, if x is 1 then the original x was a power of 2, as all powers of 2 reduce to 1 when repeatedly divided by 2
    return x == 1