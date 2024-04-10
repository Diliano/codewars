def unique_in_order(sequence):
    if len(sequence) == 0:
        return []
    
    # initialise the result with the first element of the sequence
    result = [sequence[0]]
    
    # iterate through the sequence, starting from the second element
    for i in range(1, len(sequence)):
        # if the current element is not the same as the previous element
        if sequence[i] != sequence[i - 1]:
            # add the current element to the result 
            result.append(sequence[i])
            
    return result  