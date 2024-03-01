def high(x):
    words = x.split(" ")
    max_score = float("-inf")
    result = None
    
    # iterate through each word in the words list
    for word in words:
        score = 0
        # iterate through each character in the current word
        for c in word:
            # calculate the current character score by subtracting 96 from the ASCII value of the letter (obtained by using ord(c)
            # add the current character score to the current word score
            score += (ord(c) - 96)
        # if the current word score is larger than our current max_score
        if score > max_score:
            # set max_score to current word score
            max_score = score
            # set our winning word to current word
            result = word
            
    return result