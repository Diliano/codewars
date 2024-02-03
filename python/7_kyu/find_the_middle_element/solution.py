def gimme(input_array):
    # find middle value by sorting the input list and accessing the value at index 1 
    middle = sorted(input_array)[1]
    
    # return the index that the middle value is found in the input list
    return input_array.index(middle)