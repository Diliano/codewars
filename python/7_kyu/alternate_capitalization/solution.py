def capitalize(s):
    pattern_one = ""
    pattern_two = ""
    
    for index, value in enumerate(s):
        if index % 2 == 0:
            pattern_one += f"{value.upper()}"
            pattern_two += f"{value.lower()}"
        else:
            pattern_one += f"{value.lower()}"
            pattern_two += f"{value.upper()}"
    
    return [pattern_one, pattern_two]