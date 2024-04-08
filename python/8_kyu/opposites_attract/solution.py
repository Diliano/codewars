def lovefunc( flower1, flower2 ):
    # use (flower % 2 == 0) to establish if there is an even number of petals in each flower

    # return True if one flower has an even number of petals and the other has an odd number of petals
    return (flower1 % 2 == 0) != (flower2 % 2 == 0)