def sum_of_minimums(numbers):
    sum_of_minimums = 0
    
    for list in numbers:
        sum_of_minimums += min(list)
        
    return sum_of_minimums