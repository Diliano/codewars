def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    
    # set the base case
    # by convention, where n is 0 (0!) the value is 1
    if n == 0:
        return 1
    else:
        # otherwise, recursively call the function with an argument of n - 1 and multiply the result by n
        # follow the tree, for example if n = 3
            # 3 * factorial(2)
                # 2 * factorial(1)
                    # 1 * factorial(0)
                        # 1
                            # our answer is therefore 1 * 1 * 2 * 3 = 6
        return n * factorial(n - 1)