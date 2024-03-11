def sum_of_differences(arr):
    result = 0
    
    if len(arr) < 2:
        return result
    
    arr.sort(reverse = True)
    
    for i in range(1, len(arr)):
        result += (arr[i - 1] - arr[i])
        
    return result