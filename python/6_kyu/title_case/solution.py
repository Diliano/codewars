def title_case(title, minor_words=''):
    # split the given title into a list of title cased words
    title_words = title.title().split(" ")
    # split the given minor words into a list of title cased words
    minors = minor_words.title().split(" ")
    # initialise an empty list to store the results
    result = []
    
    # use enumerate to access the index and word of each value in title_words
    for index, word in enumerate(title_words):
        # as the first word should always be title cased       
        if index == 0:
            # append the first word to result
            result.append(word)
        else:
            # if the current word is found in the minor words list
            if word in minors:
                # append a lowercased version of the word to result
                result.append(word.lower())
            else:
                # otherwise, simply append the title cased word to result
                result.append(word)

    # join the results back together by a space       
    return (" ").join(result)