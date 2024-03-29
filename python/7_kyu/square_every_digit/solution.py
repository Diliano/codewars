def square_digits(num):
    # convert the given number to a string
    num = str(num)
    
    # use list comprehension to build a list formed with each digit squared, converted to a string
    digits = [str(int(digit)**2) for digit in num]
    
    # join the squared digits and then convert back to an integer
    return int(("").join(digits))