# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:18:06 2020

@author: Joyce
"""
secretWord = chooseWord(wordlist).lower()

secretWord = 'c'



def isWordGuessed(secretWord, lettersGuessed):
    #判断是否所有的secretWord都在lettersGuessed中
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    Alltrue = 0
    for i in secretWord:
        if i in lettersGuessed:
            Alltrue += 1
    if Alltrue == len(secretWord):
        return True
    else:
        return False
    
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    avalist = []
    import string
    avastr = string.ascii_lowercase
    for a in avastr:
        avalist += a
    for i in lettersGuessed:
        if i in avalist:
            avalist.pop(avalist.index(i))      
    avastr = ''
    for e in avalist:
        avastr += e
    return avastr

def getGuessedWord(secretWord, lettersGuessed):
    ans = ''
    for i in secretWord:
        if i in lettersGuessed:
            ans += i
        else:
            ans += '_ '
    return ans


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = []
    guesstrueletters = ''
    mistakesMade = 0
    guessesleft = len(secretWord) - len(guesstrueletters)
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(guessesleft) + ' letters long.')

    while True:
        if isWordGuessed(secretWord, lettersGuessed) == False and mistakesMade < 8:
            print('-----------')
            print('You have ' + str(8 - mistakesMade) + ' guesses left.')
            print('Available letters: ' + str(getAvailableLetters(lettersGuessed)))
            Guessedthistime = input("Please guess a letter: ").lower()
            if Guessedthistime in secretWord and Guessedthistime not in lettersGuessed:
                lettersGuessed += Guessedthistime
                print('Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed)))            
            elif Guessedthistime in lettersGuessed:
                print("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)))
            else:
                print("Oops! That letter is not in my word: " + str(getGuessedWord(secretWord, lettersGuessed)))
                lettersGuessed += Guessedthistime
                mistakesMade += 1
        elif isWordGuessed(secretWord, lettersGuessed) == True:
            print('-----------')
            print ('Congratulations, you won!')
        else:
            if len(secretWord) == 1:
                print ('-----------')
                print ('Sorry, you ran out of guesses. The word was ' + secretWord + '.' )
                break
            else:    
                print ('-----------')
                print ('Sorry, you ran out of guesses. The word was else. ')
                break
secretWord = 'ette'
print(hangman(secretWord))

