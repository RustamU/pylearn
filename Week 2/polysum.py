from math import pi, tan
def polysum (n, s):
    """
    polysum function takes number of sides 'n' and length of each side 's'
    function returns sum of polygon area and squared perimetr
    result will be rounded to four decimal digits
    """
    return round((0.25*n*s**2)/(tan(pi/n))+(n*s)**2, ndigits = 4)
