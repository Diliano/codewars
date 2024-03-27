def sum_digits(number):
    sum_digits = 0
    # convert the given number to a string and remove any leading '-' negative signs
    string_number = str(number).strip("-")
    
    # iterate through each string digit in the string number
    for string_digit in string_number:
        # add the integer value of the string digit to our sum of digits
        sum_digits += int(string_digit)
        
    return sum_digits