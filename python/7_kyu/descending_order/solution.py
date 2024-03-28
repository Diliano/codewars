def descending_order(num):
    # convert the given number to a string
    num = str(num)
    
    # use list comprehension to create a list of each digit in num
    digits = [digit for digit in num]
    # use the built-in sort() function with reverse set to True, thereby sorting the list in descending order
    digits.sort(reverse = True)
    
    # join the digits and convert back to an integer
    return int(("").join(digits))