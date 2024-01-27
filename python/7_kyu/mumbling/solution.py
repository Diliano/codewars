def accum(st):
    # pattern for each section is the uppercase letter to start, followed by the lowercase version 'index' number of times

    # use list comprehension to create a new list, using enumerate to access the index and value of each character in the given string
    # construct each section to match the pattern and then join by hyphens into the final string
    return ("-").join([f"{value.upper()}" + f"{value.lower() * index}" for index, value in enumerate(st)])