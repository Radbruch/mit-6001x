# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:36:38 2020

@author: Joyce
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    assert word in wordList, False
    for i in word:
        assert i in hand, False
        assert getFrequencyDict(word).get(i,0)<=hand.get(i, 0),False
    return True
    
    
isValidWord('bug', hand, wordList)
    
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    numofTrue = 0
    if word in wordList:
        for i in word:
            if i in hand and getFrequencyDict(word).get(i,0)<=hand.get(i, 0):
                numofTrue +=1
    if len(word) == numofTrue:
        return True
    else:
        return False

        
x = isValidWord('chayote', {'a': 1, 'c': 2, 'u': 2, 't': 2, 'y': 1, 'h': 1, 'z': 1, 'o': 2}, wordList)
x = isValidWord('boar', {'b': 2, 'e': 1, 'd': 1, 'f': 1, 'i': 1, 'p': 1, 's': 1, 'r': 2, 'w': 1, 'x': 1}, wordList)
