def is_anagram(test, original):
#   first solution below
#   use list comprehension to build a list of lowercase characters for both the test and original arguments
#   sort the lists and then compare if they are the same
    
        #   test_list = sorted([c.lower() for c in test])
        #   original_list = sorted([c.lower() for c in original])
        #   return test_list == original_list
    
#   learnt that the list comprehension could be omitted and instead apply sorted directly to the lowercase strings as below
    
        #   return sorted(test.lower()) == sorted(original.lower())
    



    # refactored to a more performant solution below, counting rather than multiple comparisons/rearrangements required to sort
    test_dict = {}
    original_dict = {}
    
    # fill the dictionary of lowercase character counts for test
    for c in test:
        if c.lower() in test_dict:
            test_dict[c.lower()] += 1
        else:
            test_dict[c.lower()] = 1
        
    # fill the dictionary of lowercase character counts for original
    for c in original:
        if c.lower() in original_dict:
            original_dict[c.lower()] += 1
        else:
            original_dict[c.lower()] = 1

    # compare the resulting dictionaries to check for an anagram    
    return test_dict == original_dict