def check_exam(arr1,arr2):
    score = 0
    
    # iterate through each answer in the given lists
    for i in range(len(arr1)):
        # if the current answer of each list are equal
        if arr1[i] == arr2[i]:
            # increase score by 4 as the answers match
            score += 4
        # otherwise, if the current student answer is neither correct or blank
        elif arr2[i] != "":
            # decrease score by 1 as the answer is wrong
            score -= 1
            
    if score < 0:
        return 0
    else:
        return score