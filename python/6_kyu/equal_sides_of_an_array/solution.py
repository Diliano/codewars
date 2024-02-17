def find_even_index(arr):
    # initialise sum_right as the total sum of the array as we have not iterated through yet
    sum_right = sum(arr)
    # initialise sum_left as 0 to match the instructions, where at index 0 the left is considered 0
    sum_left = 0
    
    # use enumerate to access each index and num in arr
    for index, num in enumerate(arr):
        # as we do not consider the current num, update sum_right by taking away num from it
        sum_right -= num

        # if the sum on both sides match, we have found our index
        if sum_left == sum_right:
            return index
        
        # if not, prepare for the next iteration by adding the current num to sum_left
        sum_left += num

    # if no suitable index is found, return -1 as per the instructions    
    return -1