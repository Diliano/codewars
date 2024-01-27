def capitals(word):
    # First solution below:
    # result = []
    # for index, value in enumerate(word):
    #     if value.isupper():
    #         result.append(index)
    # return result

    # Refactored solution using list comprehension to create a new list
    # use enumerate to access the index and value of each character in the given word
    # if the character in the current iteration is uppercase, add its index to the resulting list
    return [index for index, value in enumerate(word) if value.isupper()]