def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result = result * base
        exp -= 1
    return result

print ("ITER", iterPower (3,3))

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    else:
        return base*recurPower(base, exp-1 )

print ("RECUR", recurPower (3,3))
