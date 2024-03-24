def binary_array_to_number(arr):
    # use list comprehension to build a string version of the current list and then join to form our binary string representation
    binary = ("").join([str(value) for value in arr])
    # use int() function to convert the binary representation to an integer using base 2
    return int(binary, 2)