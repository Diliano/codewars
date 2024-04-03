def is_palindrome(s):
    # lower the given string to ensure case insensivity 
    s = s.lower()
    
    return s == s[::-1]