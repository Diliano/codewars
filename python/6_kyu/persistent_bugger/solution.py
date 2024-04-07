def persistence(n):
    count = 0

    # until n is a single digit number
    while n > 9:
        # use list comprehension to build a list of the digits that form n
        digits = [int(str_digit) for str_digit in str(n)]

        # set n to 1 in order to calculate the product of our digits
        n = 1

        # iterate through each digit, multiplying each by the next to form our new n
        for digit in digits:
            n *= digit

        # increment our counter as we have completed one step
        count += 1
        
    # return our count once n is a single digit number
    return count