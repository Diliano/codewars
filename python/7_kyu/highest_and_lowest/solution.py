def high_and_low(numbers):
    # use list comprehension to create a list of integers, converted from the string of space separated numbers provided
    int_list = [int(string_num) for string_num in numbers.split(" ")]
    
    # use max and min functions to obtain the desired values from the list and format as required by the kata
    return f"{max(int_list)} {min(int_list)}"