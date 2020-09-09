def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    middle = len(aStr)//2
    if len (aStr) == 0:
        return False
    if len (aStr) == 1 and aStr[0] == char:
        return True
    if aStr[middle-1] == char or aStr[middle] == char:
        return True
    elif aStr[middle-1] > char:
        return isIn (char, aStr[0:middle])
    elif aStr[middle-1] < char:
        return isIn (char, aStr [middle+1:len(aStr)+1])
    else:
        return False
