def mango(quantity, price):
    # calculate how many sets of 3 mangoes are within the quantity
    sets_of_three = quantity // 3
    # calculate any remaining mangos after all the sets of 3 are accounted for
    remaining_mangos = quantity % 3

    # find the total by adding the prices of the sets of the three and the remaining mangos
    # for sets of three, each set will have 2 mangos charged for and therefore is calculated by: number of sets * 2 * price
    return (sets_of_three * 2 * price) + (remaining_mangos * price)