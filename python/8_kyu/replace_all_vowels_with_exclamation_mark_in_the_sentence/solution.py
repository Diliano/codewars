def replace_exclamation(st):
    # vowels stored in a variable
    vowels = "aeiouAEIOU"
    # use map to iterate over each character in the given string
    # use lambda function, replacing character with "!" if found in vowels
    # join resulting elements back into a string
    return ("").join(map(lambda c: "!" if c in vowels else c, st))