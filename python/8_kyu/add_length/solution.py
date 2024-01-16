def add_length(str_):
    # split string into list of words
    words = str_.split(" ")
    # use map function to iterate over each word in words
    # use lambda function to return a formatted string for each word
    # as map returns a map object, convert to a list
    return list(map(lambda word: f"{word} {len(word)}", words))