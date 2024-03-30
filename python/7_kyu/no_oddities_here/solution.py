def no_odds(values):
    # use list comprehension to build a list of values that are not odd (by checking they are even)
    return [value for value in values if value % 2 == 0]