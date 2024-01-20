# First solution below to understand the conversion process
# Step 1: repeatedly divide number by 2 until the number becomes 0, tracking the remainder at each step
# Step 2: the binary representation is formed by the remainders, read in reverse order 
# Step 3: use slicing with a negative step to reverse the string and convert to an integer as required by the kata

# def to_binary(n):
#     binary = ""
#     while n != 0:
#         binary += str(n % 2)
#         n //= 2
#     return int(binary[::-1])



# Refactored to the below
def to_binary(n):
    # use bin() function to convert number to binary
    # use slicing to start at index 2, removing the '0b' prefix that is included in the result of using bin()
    # convert to integer as required by the kata
    return int(bin(n)[2:])