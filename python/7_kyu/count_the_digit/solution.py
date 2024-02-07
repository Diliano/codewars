def nb_dig(n, d):
    # convert digit to a string
    string_d = str(d)
    count = 0
    
    # create a list of string squares for 0 to n (inclusive)
    squares = [str(k ** 2) for k in range(0, n + 1)]
    
    # loop through each of the string squares
    for square in squares:
        # loop through each character in the string square
        for c in square:
            # if the character matches the string digit, increase count by 1
            if c == string_d:
                count += 1
    
    return count