def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
# This code works
    # guess = True
    # for a in secretWord:
    #     if a not in lettersGuessed:
    #         guess = False
    # return guess
# But this code is better
    return False not in [a in lettersGuessed for a in secretWord]

print (isWordGuessed('abzsfw', ['c', 'a', 'b', 'z','s','f','w']))
