# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 14:46:53 2020

@author: Joyce
"""
# =============================================================================
# HANGMAN PART 1: IS THE WORD GUESSED? 
# =============================================================================
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


# =============================================================================
# PRINTING OUT THE USER'S GUESS
# =============================================================================

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretWordlist = []
    getGuessedword = ''
    for i in secretWord:
        secretWordlist += i
    for e in secretWord:
        if e not in lettersGuessed:
            position = get_index(secretWord, e)
            for o in position:
                secretWordlist[o] = '_ '
    for a in secretWordlist:
        getGuessedword += a       
    return getGuessedword
            

def get_index(secretWord, letter):
    position = []
    tag = 0
    for i in secretWord:
        if i == letter:
            position.append(tag)
        tag += 1
    return position



secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print (getGuessedWord(secretWord, lettersGuessed))

# =============================================================================
# 上一题别人更简单的方法
# =============================================================================

def getGuessedWord(secretWord, lettersGuessed):
    ans = ''
    for i in secretWord:
        if i in lettersGuessed:
            ans += i
        else:
            ans += '_ '
    return ans

# =============================================================================
# PRINTING OUT ALL AVAILABLE LETTERS
# =============================================================================
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

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print (getAvailableLetters(lettersGuessed))


 