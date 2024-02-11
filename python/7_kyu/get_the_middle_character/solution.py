def get_middle(s):
    length = len(s)
    
    if length % 2 != 0:
        mid = length // 2
        return s[mid]
    else:
        first_mid = (length // 2) - 1
        second_mid = length // 2
        return s[first_mid] + s[second_mid]