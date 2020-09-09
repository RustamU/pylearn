# def gcdIter(a, b):
#     '''
#     a, b: positive integers
#
#     returns: a positive integer, the greatest common divisor of a & b.
#     '''
#     gcd = 1
#     lowest = min(a,b)
#     for i in range (1, lowest +1):
#         if a % i == 0 and b % i == 0 and i > gcd:
#             gcd = i
#     return gcd
#print (gcdIter(19,12))


def gcdRecur(a, b):
    if b == 0:
        print ('gcd is', a)
        return a
    else:
        print ('a is %d now, b is %d now' % (a , b))
        return gcdRecur (b, a%b)
print (gcdRecur (10000,100))
