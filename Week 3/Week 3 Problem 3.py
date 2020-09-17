def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    out = ''
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',\
                'p','q','r','s','t','u','v','w','x','y','z']
    for i in lettersGuessed:
        alphabet.remove (i)
    return out.join(alphabet)

print (getAvailableLetters(['a','z','o']))
