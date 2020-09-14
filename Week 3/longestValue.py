def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    maxVal = 0
    maxIndex = None
    for i in aDict.keys():
        if len(aDict[i]) > maxVal:
            maxVal = len(aDict[i])
            maxIndex = i
        else:
            pass


    return maxIndex

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print (biggest (animals))
