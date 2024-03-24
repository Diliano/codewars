def binary_array_to_number(arr):
    result = 0
    # each digit in the binary representation is equivalent to 2 to the power of x
    # as the rightmost digit will be 2^0, the leftmost digit will be 2^(length of array - 1) to account for the 0th start
    power = len(arr) - 1
    
    # iterate through each value in the list
    for value in arr:
        # if the current value is 1
        if value == 1:
            # calculate the integer value by using 2^power and add this to our result
            result += 2**power
        # before we move to the right, lower the power by 1
        # for example if we are currently at 2^3, the next iteration to the right will need to be 2^2 and so on, until 2^0
        power -= 1
        
    return result