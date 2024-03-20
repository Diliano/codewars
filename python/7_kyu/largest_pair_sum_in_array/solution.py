def largest_pair_sum(numbers): 
    numbers.sort()
    return numbers[-1] + numbers[-2]