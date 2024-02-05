def stray(arr):
    # if the first two elements are equal
    if arr[0] == arr[1]:
        # loop through the remaining elements (third element onwards)
        for i in range(2, len(arr)):
            # if an element is not equal to the first (or second as both are equal), it is the stray number
            if arr[i] != arr[0]:
                return arr[i]

    # if the first two elements are equal, one of them is the stray number
    # if the third element is equal to the first, the second element is the stray number
    if arr[2] == arr[0]:
        return arr[1]
    # otherwise if the third element is equal to the second, the first element is the stray number
    else:
        return arr[0]