# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 22:47:34 2020

@author: Joyce
"""

j = 0
k = 0

import time

t1 = time.time()

while j < 10000000:
    j += 1

t2 = time.time()

for k in range(0, 10000000):
    k += 1
    
t3 = time.time()


print("t2 - t1 = " + str(t2 - t1))
print("t3 - t2 = " + str(t3 - t2))

# =============================================================================
# 
# =============================================================================
def program1(L):
    multiples = []    #1
    for x in L:         
        for y in L:
            multiples.append(x*y) #2
    return multiples


def program2(L):
    squares = []        #1
    for x in L:
        for y in L:
            if x == y:  #1
                squares.append(x*y)  #2
    return squares                      #1


def program3(L1, L2):
    intersection = []       #1
    for elt in L1:
        if elt in L2:
            intersection.append(elt)
    return intersection

def genSubsets(L):
    res = []
    if len(L) == 0:
        return [[]]
    smaller = genSubsets(L[:-1])
    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small+extra)
    return smaller+new


L = ['a', 'b', 'c', 'd']
x = genSubsets(L)



# =============================================================================
# 
# =============================================================================

def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal= L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal= L[j]
            j += 1
        temp = L[i]
        L[i] = L[minIndx]
        L[minIndx] = temp 

L = [3, 6, 7, 1, 4, 57, 17, 9]
x = selSort(L)


def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp

def mySort(L):
    clear = False
    while not clear:
        clear = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
            print(L)
L = [3, 6, 7, 1, 4, 57, 17, 9]
mySort(L)


import operator


