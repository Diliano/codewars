def is_valid_walk(walk):
    # return false if walk is not exactly 10 minutes, as per instructions
    if len(walk) != 10:
        return False
    
    # initialise x and y as the starting point 
    x, y = 0, 0
    
    # use a dictionary to match each direction with its effect on the x and y value
    direction_dict = {
        "n": (0, 1),
        "s": (0, -1),
        "w": (-1, 0),
        "e": (1, 0)
    }
    
    # iterate through each direction in the given walk
    for direction in walk:
        # update x using the direction key and its corresponding x value
        x += direction_dict[direction][0]
        # update y using the direction key and its corresponding y value
        y += direction_dict[direction][1]
        
    # check if we have returned to the starting point
    return x == 0 and y == 0