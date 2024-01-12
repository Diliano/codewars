import functools

def sum_mix(arr):
    # use lambda function to handle addition, treating both elements as integers    
    # pass lambda function and arr to reduce, applying the function to each value and accumulating the sum along the way
    return functools.reduce(lambda a, b: int(a) + int(b), arr)