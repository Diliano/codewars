def nb_dig(n, d):
    # first solution below
    # convert digit to a string and create a list of squares (also as strings) for 0 to n (inclusive)
    # iterate through the squares and then each character, increasing count by 1 if the character matches the target digit
        # string_d = str(d)
        # count = 0
        # squares = [str(k ** 2) for k in range(0, n + 1)]
        # for square in squares:
        #     for c in square:
        #         if c == string_d:
        #             count += 1
        # return count
    


    # refactored to a more concise solution
    # convert digit to a string
    string_d = str(d)
    
    # create a list of squares (also as strings) for 0 to n (inclusive)
    squares = [str(k ** 2) for k in range(0, n + 1)]
    
    # use string count function to count each target digit found in each square
    # use sum function to aggregrate the counts into a total count
    return sum(square.count(string_d) for square in squares)