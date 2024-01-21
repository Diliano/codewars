def take(arr,n):
    # use list slicing with default start (at the beginning of the list), up until and not including the nth index (exclusive)
    # as 0 indexed, up until the nth will cover the first n elements
    return arr[:n]