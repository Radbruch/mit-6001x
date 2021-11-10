# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 21:08:20 2020

@author: Joyce
"""

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """   
    word = ''     
    wordused = ''
    getscorethistime = 0
    Totalscore = 0
    while True:
        if calculateHandlen(hand) - len(wordused) > 1:
            print('Current Hand:  ', end = '')
            displayHand(updateHand(hand, wordused))
            word = input('Enter word, or a "." to indicate that you are finished: ')
            if isValidWord(word, hand, wordList) == True: 
                getscorethistime = getWordScore(word, calculateHandlen(hand))
                Totalscore += getscorethistime
                wordused += word
                print( '"' + word +'"' + ' earned ' + str(getscorethistime) + ' points. Total: ' + str(Totalscore) + ' points')
            elif isValidWord(word, hand, wordList) == False:
                print('Invalid word, please try again.')
        elif calculateHandlen(hand) - len(wordused) == 1:
            print('Current Hand:  ', end = '')
            displayHand(updateHand(hand, wordused))
            wordfinal = input('Enter word, or a "." to indicate that you are finished: ')
            if wordfinal == '.':
                print('Goodbye! Total score: ' + str(Totalscore) +' points. ')
            break
        else:
            print ('Run out of letters. Total score: ' + str(Totalscore) + ' points.')
            break
        
        
        
