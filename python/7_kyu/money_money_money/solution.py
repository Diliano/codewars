def calculate_years(principal, interest, tax, desired):
    years = 0
    
    # check if the initial principal is already equal to the desired amount
    # if so, return the initialised number of years (0)
    if principal == desired:
        return years
    
    # loop until the principal reaches or exceeds the desired amount
    while principal < desired:
        # calculate the accrued interest for the year
        accrued_int = principal * interest
        # calculate the tax due on the acrrued interest
        int_tax = accrued_int * tax
        # calculate the new value of principal
        principal = principal + accrued_int - int_tax
        # increment the year counter
        years += 1
        
    return years