def tower_builder(n_floors):
    result = []
    # initialise stars with top floor amount of 1
    stars = 1
    # as the top floor will have one star, the space on either side will be n_floors - 1
    space = n_floors - 1

    # iterate through each floor
    for i in range(n_floors):
        # add the formatted floor to our result in the format space/stars/space
        result.append(f"{space * ' '}{stars * '*'}{space * ' '}")
        # increment stars by 2 to meet the pattern
        stars += 2
        # decrement space on either side by 1 as we have increased stars by 2
        space -= 1
        
    return result