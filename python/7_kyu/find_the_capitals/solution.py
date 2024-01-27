def capitals(word):
    result = []
    # use enumerate to access index and value of each character in the given word
    for index, value in enumerate(word):
        # if the value in the current iteration is uppercase, add to the result list
        if value.isupper():
            result.append(index)
    return result