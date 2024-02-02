def solve(s):
    lower_count = 0
    upper_count = 0
    
    for character in s:
        if character.islower():
            lower_count += 1
        else:
            upper_count += 1
            
    if upper_count > lower_count:
        return s.upper()
    else:
        return s.lower()