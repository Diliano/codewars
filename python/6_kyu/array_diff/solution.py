def array_diff(a, b):
    # convert b to a set for performance of checking if num is in b, as b gets larger
    b = set(b)
    # use list comprehension to create a new list, adding each num in a if it is not found in b 
    return [num for num in a if num not in b]