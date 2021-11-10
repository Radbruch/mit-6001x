# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 01:30:08 2020

@author: Joyce
"""

# =============================================================================
#def syntax 
# =============================================================================
def myFunction(argument):
   """
   Docstring goes here. Explain what type argument(s) should have, and what your function
   is going to return.
   """
   < Code for your function (the body of the function) goes here >

def a(x):
   '''
   x: int or float.
   '''
   return x + 1

# =============================================================================
# L4 P1
# =============================================================================

def a(x):
   '''
   x: int or float.
   '''
   return x + 1

def b(x):
   '''
   x: int or float.
   '''
   return x + 1.0

def c(x, y):
   '''
   x: int or float. 
   y: int or float.
   '''
   return x + y

def d(x, y):
   '''
   x: Can be of any type.
   y: Can be of any type.
   '''
   return x > y

d('apple', 11)


def e(x, y, z):    
   '''
   x: Can be of any type.
   y: Can be of any type.
   z: Can be of any type.
   '''
   return x >= y and x <= z


def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2
   
# =============================================================================
# L4 P2
# =============================================================================

def a(x, y, z):
     if x:
         return y
     else:
         return z


def b(q, r):
    return a(q>r, q, r)


# =============================================================================
# 把iteration loop改写为def形式
# =============================================================================

#原代码，求x的p次幂
x = float(input('Enter a number:'))
p = int(input('Enter a integer power:'))
result = 1#别忘了设置一个初始值#
for turn in range(p):
    print('iteration' + str(turn) + 'current result' + str(result))
    result = result * x
print('iteration' + str(turn+1) + 'current result' + str(result))
    
    
#改写，用函数表示#
def iterative_power(x,p):
    result = 1
    for turn in range(p):
        print('iteration' + str(turn) + 'current result' + str(result))
        result = result * x
    return result

z = iterative_power(5,6)#这里（5，6）不会改变原x和p的赋值，因为这是在Environmente2运行的



# =============================================================================
# L4 P3
# =============================================================================
def square(x):
    '''
    x: int or float.
    '''
    y = x**2
    return y


square(88.5)

# =============================================================================
# L4 P4
# =============================================================================
    
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    y = a*(x**2) + b*x + c
    return y 
    
evalQuadratic(1, 7, 4, 7)

# =============================================================================
# 关于内外环境，每个函数的内环境是独立的
# =============================================================================
    
def f(x):
    y = 1
    x = x + y
    print("x = " + str(x)) # 这里print出的是def里面x的值，与外部x无关
    return x # 这里的x不会影响到外部x

x = 3
y = 2
z = f(x)
print('x = ' + str(x))
print('y = ' + str(y))
print('z = ' + str(z))


# =============================================================================
# L4 P5 如何得到中间数
# =============================================================================



def clip(low, x, high):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - low, when x < low
     - high, when x > high
     - x, otherwise
    '''
    # Your code here

    return min(high,max(x, low))
    print(clip(1, -6, 3))

    return max(low, min(x, high))



# =============================================================================
# L4 P7 def套def :直接看return的是什么
# =============================================================================
def foo(x):
   def bar(x):
      return x + 1
   return bar(x * 2)

foo(3)

#改写为

def bar(x):
    return x + 1
def foo(x):
    return bar(x * 2)
foo(3)

# =============================================================================
# Method to search root of a number
# =============================================================================
def find_root(x,power,epsilon):
    '''x and epsilon int or float, power an int
        epsilon > 0 & power >= 1'''
    if x < 0 and power%2 == 0:
        return None
    #can't find even powered root of negative number
    low = min(-1,x)
    high = max(1,x)
    ans = (high + low)/2.0
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    return ans

find_root(-75,3,0.01)


# =============================================================================
# L4P8
# =============================================================================
def square(x):
    '''
    x: int or float.
    '''
    # Your code here
    y = x**2
    return y

def fourthPower(x):
    '''
    x: int or float.
    '''
    # Your code here
    x = square(square(x))
    return x

fourthPower(3)


# =============================================================================
# L4 P9
# =============================================================================
def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    return (x%2==1)
    
odd(8.8)

# =============================================================================
# L4 P10
# =============================================================================
def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    return (char == 'A' or char =='a' or char =='E' or char =='e' or char =='I' or char =='i' or char =='O' or char =='o' or char =='U' or char =='u')

isVowel('f')

# =============================================================================
# L4 P11
# =============================================================================
Vowel = ['A','a','E','e','I','i','O','o','U','u']
def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    return (char in Vowel)


isVowel2('A')

# =============================================================================
# L4 P12
# =============================================================================
s = 'abc'
s.capitalize()
s.upper()

str1 = 'exterminate!' 
str1.isupper()

str2 = 'Number one - the larch'
str1.index('a')
str2.index('!')
str1.find('e')
str1 = str1.replace('e', '*')
str2.replace('one', 'seven')
str2.find('!')

# =============================================================================
# P S 1 - 1
# =============================================================================
s = 'azcbobobegghakl'
def Number_of_vowels(s):
    x = s.count('a')
    y = s.count('e') 
    z = s.count('i') 
    m = s.count('o') 
    n = s.count('u') 
    return (x + y + z + m + n)
print('Number of vowels: ' + str(Number_of_vowels(s)))

#w呜呜呜
def Num_of_vow(s):
    result = 0
    for vowel in 'aeiou':
        result += s.count(vowel)
    return result   
print('Number of vowels: ' + str(Num_of_vow(s)))

# =============================================================================
# P S 1 - 2
# =============================================================================
s = 'azcbobobegghakl'
s.find('bob')
x = str(s.split('bo',1))
y= x.split('bo',1)


def f(s):
    result = 0
    while 'bob' in s:
        s ='b' + s.split('bob',1)[-1]
        result +=1
    return result
print('Number of times bob occurs is: ' + str(f(s)))

    
    
s = 'bbobbobbbobbbobobobbbob' 
print('Number of times bob occurs is: ' + str(f(s)))
s = 'dfwgwefwe'
print('Number of times bob occurs is: ' + str(f(s)))
s = 'obobbboaydobobbobobo' 
print('Number of times bob occurs is: ' + str(f(s)))
s = 'bbobbobkbobobvbobobboboboboooboobbobbobobobboq'
print('Number of times bob occurs is: ' + str(f(s)))
s = 'oboboboobjoboboobetbobbobobeobobqobboobfpibob' 
print('Number of times bob occurs is: ' + str(f(s)))
s = 'oboobobbobobobboboboboobobobpenbobobebooboa' 
print('Number of times bob occurs is: ' + str(f(s)))


# =============================================================================
# P S 1 - 3 错误的答案，不过方法值得记录
# =============================================================================
s1 = 'azcbobobegghakl'

def find_lcsubstr(s1, s2):   
    m=[[0 for i in range(len(s2)+1)]  for j in range(len(s1)+1)]  #生成0矩阵，为方便后续计算，比字符串长度多了一列  
    mmax=0   #最长匹配的长度  
    p=0  #最长匹配对应在s1中的最后一位  
    for i in range(len(s1)):  
        for j in range(len(s2)):  
            if s1[i]==s2[j]:  
                m[i+1][j+1]=m[i][j]+1  
                if m[i+1][j+1]>mmax:  
                    mmax=m[i+1][j+1]  
                    p=i+1  
    return s1[p-mmax:p],mmax   #返回最长子串及其长度  

print (find_lcsubstr(s1,s2))

s2 = ''.join(sorted(s1))
# =============================================================================
# P S 1 - 3 最终答案
# =============================================================================
s = 'azcbobobegghakl'
s = 'abcbcd'
s = 'zyxwvutsrqponmlkjihgfedcba'

def find_longest_str(s):
    temp = s[0]
    result = s[0]
    for i in range(0, len(s)-1):
        if s[i+1] >= s[i]:
            temp += s[i+1]
            if len(result) < len(temp):
                result = temp
        else:
            temp = s[i+1]
    return result

print('Longest substring in alphabetical order is: '  + str(find_longest_str(s)))

s = 'zyxwvutsrqponmlkjihgfedcba'   z
s = 'sigiazttr'    gi


# =============================================================================
# P S 2 - 1
# =============================================================================

f(balance,annualInterestRate,10)

x = 10
balance = 5000.0
annualInterestRate = 0.18

balance = 3926
annualInterestRate = 0.2

def f(balance,annualInterestRate,lowestpayment):
    # 求12个月后还欠多少钱
    i = 0
    while i < 12:
        balance = ((balance - lowestpayment) * (1+(annualInterestRate/12.0)))
        balance = round(balance, 2)
        i = i + 1
    return balance




n = 1
lowestpayment = (10 * n)
while True:
    if f(balance,annualInterestRate,lowestpayment) > 0:
        n += 1
        lowestpayment = (10 * n)
    else:
        break
print('Lowest Payment: ' + str(lowestpayment))


# =============================================================================
# P S 2 - 2 bisection research
# =============================================================================
balance
annualInterestRate
Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0


balance = 320000
annualInterestRate = 0.2



def f(balance,annualInterestRate,Monthlypayment):
    # 求12个月后还欠多少钱
    i = 0
    while i < 12:
        balance = ((balance - Monthlypayment) * (1+(annualInterestRate/12.0)))
        i = i + 1
    return balance

Monthlypayment_lower = balance / 12
Monthlypayment_upper = (balance * (1 + (annualInterestRate/12.0))**12) / 12
Monthlypayment = (Monthlypayment_lower + Monthlypayment_upper)/2
while abs(f(balance,annualInterestRate,Monthlypayment)) >= 0.01:
    Monthlypayment = (Monthlypayment_lower + Monthlypayment_upper)/2
    if f(balance,annualInterestRate,Monthlypayment) > 0:
        Monthlypayment_lower = Monthlypayment
    elif f(balance,annualInterestRate,Monthlypayment) < 0:
        Monthlypayment_upper = Monthlypayment
Monthlypayment = round(Monthlypayment,2)
print('Lowest Payment: ' + str(Monthlypayment))   