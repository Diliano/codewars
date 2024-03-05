def find_uniq(arr):
    # as list is guaranteed to have at least three elements, store the values of the first three
    first = arr[0]
    second = arr[1]
    third = arr[2]
    
    # if first and second are different, one of them is unique
    if first != second:
        # if third is the same as first, second is our unique
        if third == first:
            return second
        else:
            # otherwise third must be the same as second, first is our unique
            return first
    
    # if the first three elements are the same, iterate through the remaining elements
    for i in range(2, len(arr)):
        # if the current element is not the same as first (or second, third), it is our unique
        if arr[i] != first:
            return arr[i]