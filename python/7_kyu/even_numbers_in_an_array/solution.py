def even_numbers(arr,n):
    evens = [num for num in arr if num % 2 == 0]
    
    return evens[-n:]