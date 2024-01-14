def replace_exclamation(st):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    return ("").join(map(lambda c: "!" if c in vowels else c, st))