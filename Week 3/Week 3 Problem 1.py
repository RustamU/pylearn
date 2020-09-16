def isWordGuessed(secretWord, lettersGuessed):
    print ('secretWord = ', secretWord)
    print ('lettersGuessed =', lettersGuessed )
    guess = True
    for a in secretWord:
        if a not in lettersGuessed:
            guess = False
    return guess

print (isWordGuessed('ab', ['c', 'a', 'b']))
