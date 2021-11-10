# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 00:41:36 2020

@author: Joyce
"""

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    #单词的分值是字母分值的和，乘上单词的长度，如果n个字母一次被组成为单词，额外加50分
    #在计算积分之前需要检查手上的牌是否真的有1个 'w', 2个 'e'， 1个 'd'!
    def num_of_char(wordlst):
        wordset = set(wordlst)
        ans = {}
        for i in wordset:
            ans[i] = wordlst.count(i)
        return ans
    #wordlist2中某元素的个数是否小于等于wordlist1中相同元素的个数
    ifnumtrue = 0
    for i in num_of_char(word):
        if int(num_of_char(word)[i]) <= int(num_of_char(hand)[i]):
            ifnumtrue += 1
        else:
            ifnumtrue += 0
    if ifnumtrue == len(set(word)) and set(word).issubset(hand):
        points = 0
        for i in word:
            points += int(SCRABBLE_LETTER_VALUES[i])
        if len(word) == n:
            return points*len(word) + 50
        else:
            return points*len(word)



#判断list2是不是list1的子集
list1 = set(['a', 'p', 'p', 'l', 'e'])
list2 = set(['p', 'p', 'e', 'e', 'r'])
set(list2).issubset(list1)


#寻找所有元素的个数
wordlist1 = ['a', 'p', 'p', 'l', 'l', 'e', 'e']
wordlist2 = ['a', 'p', 'l', 'e', 'e', 'e']
def num_of_char(wordlist):
    wordset = set(wordlist)
    ans = {}
    for i in wordset:
        ans[i] = wordlist.count(i)
    return ans
#wordlist2中某元素的个数是否小于等于wordlist1中相同元素的个数
ifnumtrue = 0
for i in num_of_char(wordlist2):
    if int(num_of_char(wordlist2)[i]) <= int(num_of_char(wordlist1)[i]):
        ifnumtrue += 1
    else:
        ifnumtrue += 0
if ifnumtrue == len(set(wordlist2)) and set(list2).issubset(list1):
    

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    points = 0
    for i in word:
        points += int(SCRABBLE_LETTER_VALUES[i])
    if len(word) == n:
        return points*len(word) + 50
    else:
        return points*len(word)