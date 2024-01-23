def first_non_consecutive(arr):
    # check if array is empty or only has one element
    if not arr or len(arr) == 1:
        return None
    
    # loop through array, starting from the first element
    for i in range(1, len(arr)):
        # check if the current value is not equal to the previous value plus one (not consecutive)
        # if True, return the value
        if arr[i] != (arr[i - 1] + 1):
            return arr[i]
        
    # if all are consecutive, return None
    return None    