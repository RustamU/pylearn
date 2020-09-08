def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    gcd = 1
    lowest = min(a,b)
    for i in range (1, lowest +1):
        if a % i == 0 and b % i == 0 and i > gcd:
            gcd = i
    return gcd

print (gcdIter(19,12))
