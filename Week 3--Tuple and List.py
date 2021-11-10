# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:34:06 2020

@author: Joyce
"""

## divisors

def findDivisors(n1, n2):
    #找公约数
    """assumes that n1 and n2 are positive ints
       returns a tuple containing the common divisors of n1 and n2"""
    divisors = () # the empty tuple
    for i in range(1, min(n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            divisors = divisors + (i,)
    return divisors

print(findDivisors(20, 100))

divisors = findDivisors(20, 100)
total = 0
for d in divisors:
    total += d
print(total)

# =============================================================================
# L6 P2
# =============================================================================

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''

    if aTup == ():
        return ()
    if len(aTup) != 0 and len(aTup) < 3:
        return (aTup[0],)
    else:
        return (aTup[0],) + oddTuples(aTup[2:]) 
    


aTup = ('I', 'am', 5, 'test', 'tuple',)
x = oddTuples(aTup)


# =============================================================================
# applyToEach
# =============================================================================
 

def applyToEach(L, f):
    """assumes L is a list, f a function
       mutates L by replacing each element, e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])


L = [1, -2, 3.4]

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

applyToEach(L, abs)
print(L)

applyToEach(L, int)
print(L)

applyToEach(L, fact)
print(L)

applyToEach(L, fib)
print(L)

# =============================================================================
# L6 P10
# =============================================================================
def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    ans = 0
    for i in aDict:
        ans += len(aDict[i])
    return ans



# =============================================================================
# L6 P11
# =============================================================================
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    if len(aDict) == 0:
        return None
    else:
        lenth = []
        copy = []
        for i in aDict:
            copy += i
            lenth.append(len(aDict[i]))
        maxx = lenth.index(max(lenth))
        return copy[maxx]

# =============================================================================
# P S 3-1
# =============================================================================

def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

print(f(0))
print(f(2.5))

print((f(0)+f(1)+f(2)+f(3)+f(4))*1)
print((f(5)+f(6)+f(7)+f(8)+f(9)+f(10))*1)
def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    NumofPortions = int((stop - start)/step)
    S = 0
    for i in range(NumofPortions):
        S += step * f(start + step*i)
    return S

print(radiationExposure(0, 11, 0))
        
