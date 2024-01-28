def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    
    # use sum and range functions to iterate through and sum values
    # use end_number + 1 to ensure that end_number is considered in the sum, providing it falls in the sequence
    return sum(range(begin_number, end_number + 1, step))