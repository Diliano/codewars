def duplicate_count(text):
    # lowercase the input text to ensure case consistency
    text = text.lower()
    # initialise a dictionary to track the occurences of each character
    occurences = {}
    # initialise the duplicate count as 0
    count = 0

    # iterate through each character in text
    for c in text:
        # if the character is a key in the occurences dictionary
        if c in occurences:
            # if so, check if the character occurences are 1 
            if occurences[c] == 1:
                # increment character occurences by 1 to 2, which skips this condition being met again for the given character
                occurences[c] += 1
                # increment count by 1
                count += 1
        else:
            # if the character is not a key in the dictionary, add it with a value of 1
            occurences[c] = 1
    
    return count