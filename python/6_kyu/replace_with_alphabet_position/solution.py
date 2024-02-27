def alphabet_position(text):
    result = []
    # convert text all to lowercase to make the process simpler
    text = text.lower()
    
    # iterate through each character in text
    for c in text:
        # if the current character is alphabetic
        if c.isalpha():
            # calculate the alphabet position by subtracting 96 from the ASCII value of the letter (obtained by using ord(letter))
            # for example, "a" is 97 which becomes 1, "b" is 98 which becomes 2 and so on
            result.append(str(ord(c) - 96))
            
    return (" ").join(result)