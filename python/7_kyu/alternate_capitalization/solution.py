def capitalize(s):
    # first solution below
        # pattern_one = ""
        # pattern_two = ""
        # for index, value in enumerate(s):
        #     if index % 2 == 0:
        #         pattern_one += f"{value.upper()}"
        #         pattern_two += f"{value.lower()}"
        #     else:
        #         pattern_one += f"{value.lower()}"
        #         pattern_two += f"{value.upper()}"
        # return [pattern_one, pattern_two]
    
    
    # refactored to a more performant solution
    # use list comprehension to build the pattern and join, rather than a new string being created with each concatenation

    pattern_one = ("").join([value.upper() if index % 2 == 0 else value.lower() for index, value in enumerate(s)])
    pattern_two = ("").join([value.lower() if index % 2 == 0 else value.upper() for index, value in enumerate(s)])
    
    return [pattern_one, pattern_two]