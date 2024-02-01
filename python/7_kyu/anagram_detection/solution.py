def is_anagram(test, original):
#   use list comprehension to build a list of lowercase characters for both the test and original arguments
#   sort the lists and then compare if they are the same
    test_list = sorted([c.lower() for c in test])
    original_list = sorted([c.lower() for c in original])
    
    return test_list == original_list