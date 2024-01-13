def how_much_i_love_you(nb_petals):
    # The phrases repeat every 6 petals
    phrases = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    # As there are 6 phrases but lists are zero-indexed, minus 1 from the number of petals to align with the 0-5 indexes
    # When dividing by a fixed divisor, the remainder will always cycle through from 0 to divisor - 1 (aligning with the 0-5 indexes of the phrases list)
    # Use modulo operator to calculate the correct index, where if the numerator (top number) is lower, the remainder is the numerator i.e 4 % 6 = 4, 2 % 6 = 2 etc
    # if the denominator is lower, we wrap around and still access an index within the 0-5 range i.e 16 % 6 = 4, 14 % 6 = 2 etc
    index = (nb_petals - 1) % 6
    return phrases[index]