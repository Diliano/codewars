def multiplication_table(size):
    result = []
    
    # iterate through rows i.e if size is 3, rows will be 1, 2, 3
    for i in range(1, size + 1):
        # use list comprehension to build the row by iterating through each column and multiplying the row value
        # in our example, row 1 would have values 1 * 1, 1 * 2 and 1 * 3, leading to [1, 2, 3]
        # likewise row 2 would have values 2 * 1, 2 * 2 and 2 * 3, leading to [2, 4, 6] 
        result.append([i * j for j in range(1, size + 1)])
        
    return result