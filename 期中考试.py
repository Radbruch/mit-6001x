# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:34:48 2020

@author: Joyce
"""
# =============================================================================
# def myLog
# =============================================================================
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    low = 0
    high = x
    mid = (low + high)//2
    epsilon = 1
    while abs(x - b**mid) > epsilon:
        if x > b**mid:
            low = mid
        elif x < b**mid:
            high = mid
        mid = (low + high)/2  
    return int(mid)


n = myLog(3, 2)

# =============================================================================
# def laceStrings
# =============================================================================

def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    lists1 = []
    lists2 = []
    for i in s1:
        lists1 += i
    for j in s2:
        lists2 += j
    ans = ''
    anslist = []
    if len(s1) <= len(s2) and s2 != '':
        for n in range(len(s1)):
            anslist += lists1[n]
            anslist += lists2[n]
        if len(s1) != len(s2):
            anslist += lists2[len(s1):]
        else:
            anslist += ''
        for o in anslist:
            ans += o
        return ans
    elif len(s1) >= len(s2) and s1 != '':
        for m in range(len(s2)):
            anslist += lists1[m]
            anslist += lists2[m]
        if len(s1) != len(s2):
            anslist += lists1[len(s2):]
        else:
            anslist += ''
        for o in anslist:
            ans += o
        return ans
    else:
        return s1 + s2
        
        
# =============================================================================
# def laceStringsRecur
# =============================================================================
        
def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return s2
        if s2 == '':
            return s1
        else:
            return s1[0] + s2[0] + helpLaceStrings(s1[1:], s2[1:], out)
    return helpLaceStrings(s1, s2, '')
        
        
laceStringsRecur('hi', '')        
        
# =============================================================================
# def McNuggets
# =============================================================================
        
def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # 1 20c 9b 6a
    for i in range(n//20 + 1):
        for j in range(n//9 + 1):
            for k in range(n//6 + 1):
                if 20*i + 9*j + 6*k == n:
                    return True
    return False
    
        
    
McNuggets(27)

    

    
    
    
    
    
    
    
    
    