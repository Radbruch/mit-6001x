# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 00:04:38 2020

@author: Joyce
"""

# =============================================================================
# L5 Problem 1
# =============================================================================
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    i = exp
    while i > 0:
        result = result * base
        i -= 1
    return result

print(iterPower(3, 3))

# =============================================================================
# Recursion
# =============================================================================
def recurMul(a,b):
    if b == 1:
        return a
    else:
        return a + recurMul(a,b-1)
        
recurMul(3, 2)

def f(x):
    if x == 1:
        return x
    else:
        return x * f(x-1)
    

# =============================================================================
# L5 P2
# =============================================================================
base = 2
exp = 8

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp-1)
print(recurPower(base, exp))

# =============================================================================
# L5 P3
# =============================================================================
def recurPowerNew(base, exp):
    if exp % 2 == 0 and exp != 0:
        return recurPowerNew(base*base, exp//2)
    elif exp % 2 != 0:
        return base * recurPowerNew(base, exp-1)
    else:
        return 1

print(recurPowerNew(2, 10))  
        
# =============================================================================
# L5 P4
# =============================================================================

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    test = min(a,b)
    def f(test):
        if a % test == 0 and b % test ==0:
            return test
        elif test != 1:
            return f(test - 1)
        else:
            return 1
    return f(test)

print(gcdIter(50, 30) )
    
    
# =============================================================================
# L5 P5
# =============================================================================
    
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    test = min(a,b)
    if test == 0:
        return  max(a,b)
    elif a % test == 0 and b % test == 0:
        return test
    else:
        return gcdRecur(b, a % b)
    
gcdRecur(55, 7)
    
# =============================================================================
# Towers of Hanoi
# =============================================================================
def printMove(fr,to):
    print('move from ' + str(fr) + ' to ' + str(to))
    
def Towers(n, fr , to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
        
print(Towers(2, '1', '3', '2'))  

# =============================================================================
# Fibonacci
# =============================================================================
def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    assert type(x) == int and x >= 0
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
    
# =============================================================================
#     回文结构
# =============================================================================
def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
                print(ans)
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

print(isPalindrome('abba'))

# =============================================================================
# L5 P6
# =============================================================================

def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    ans = 0
    for i in aStr:
        ans += 1
    return ans
    
print(lenIter('fdsfegsdfeges'))



# =============================================================================
# L5  P7
# =============================================================================
def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    if aStr == '':
        return 0
    else:
        return lenRecur(aStr[1:]) + 1
    
print(lenRecur('gsdgdfsewgewe'))


# =============================================================================
# L5 P8
# =============================================================================
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    else:
        testChar = aStr[len(aStr)//2]
        if char == testChar:
            return True
        elif char < testChar and len(aStr) != 1:
            return isIn(char,aStr[:len(aStr)//2])
        elif char > testChar and len(aStr) != 1:
            return isIn(char,aStr[len(aStr)//2:])
        else:
            return False
aStr = 'Hello, world'
print(isIn('', 'H'))


# =============================================================================
# L5 P9
# =============================================================================
def semordnilapWrapper(str1, str2):
    #这里首先把长度为1和相等的字符串排除掉
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    if len(str1) == 1:
        #这里的len==1指的是用recursion递减以后最后剩下一个时，进行对比
        return str1 == str2
    if len(str1) != len(str2):
        return False
    if str1[0] == str2[-1]:
        return semordnilap(str1[1:], str2[:-1])
    #这里不能把递归return到semordnilapWrapper，否则len==1直接False
    else:
        return False



print(semordnilapWrapper('sefff', 'fffes'))

# =============================================================================
# 在函数中定义全局变量
# =============================================================================
def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)


def testFib(n):
    for i in range(n+1):
        global numCalls
        numCalls = 0
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print('fib called ' + str(numCalls) + ' times')
        
        
        

