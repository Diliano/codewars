def no_boring_zeros(n):
    if n == 0:
        return n
    
    # if n has a trailing 0, dividing by 10 will leave a 0 remainder
    # while True, repeatedly divide by 10 until no longer True
    while n % 10 == 0:
        n //= 10

    return n