def small_enough(array, limit):
    return all(num <= limit for num in array)