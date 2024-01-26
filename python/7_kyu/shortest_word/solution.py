def find_short(s):
    # split string into a list of words
    words = s.split(" ")
    # use generator expression to create an interable of the lengths of each word
    # use min() function to find the smallest length 
    return min(len(word) for word in words)