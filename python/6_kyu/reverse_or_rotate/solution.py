def rev_rot(str, sz):
    # handle edge cases as instructed by the kata
    if sz <= 0 or len(str) == 0 or sz > len(str):
        return ""
    
    # use list comprehension to build chunks according to the given size
    chunks = [str[i: i + sz] for i in range(0, len(str), sz)]
    result = []
    
    # iterate through each chunk
    for chunk in chunks:
        # eliminate any trailing chunks in the wrong size by checking len(chunk) == size
        if len(chunk) == sz:
            # check if the sum of all chunk digits cubed are divisible by 2
            if sum(int(digit)**3 for digit in chunk) % 2 == 0:
                # if so, use list slicing to reverse the chunk
                result.append(chunk[::-1])
            else:
                # if not, use list slicing to move the first digit to the end
                result.append(chunk[1:] + chunk[0])

    # join result into a string 
    return ("").join(result)
        
