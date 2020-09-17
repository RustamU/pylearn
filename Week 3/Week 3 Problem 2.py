def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    out = ''
    # for i in secretWord:
    #     if i in lettersGuessed:
    #         out = out + i
    #     else:
    #         out = out + '_'
    # return out
    return out.join( [out + i if i in lettersGuessed else out +'_' for i in secretWord] )


print (getGuessedWord('umaturman', ['a','n','t']))
