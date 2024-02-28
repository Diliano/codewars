def sort_array(source_array):
    # use list comprehension and sorted() to create a sorted list of the odd numbers
    sorted_odds = sorted([x for x in source_array if x % 2 != 0])
    # initialise a variable to track the indexes of sorted_odds 
    i = 0
    
    # use enumerate to access the index and value of each element in source_array
    for index, value in enumerate(source_array):
        # if the current value is odd
        if value % 2 != 0:
            # replace the current odd element with the next element in sorted_odds
            source_array[index] = sorted_odds[i]
            # increment i to move to the next element in sorted_odds
            i += 1
            
    return source_array 