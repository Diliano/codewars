# First solution below
# Iterate through each character of input and if lowercase, exit and return False

# def is_uppercase(inp):
#     for c in inp:
#         if c.islower():
#             return False
#     return True


# Refactor after learning about any()
# using the any() function with a condition that checks for any character that is lowercase, returning True if it finds one
# As we are looking for the inverse (a lowercase is not desired), use the not keyword to return False when a lowercase is found

def is_uppercase(inp):
    return not any(c.islower() for c in inp)