x = 76667
if x % 2 == 0:
    if x % 3 == 0:
        print("divided by 2 and 3")
    else:
        print("divided by 2 but not 3")
elif x % 3 == 0:
    print("divided by 3 but not 2")
else:
    print("not divided by 2 or 3")
    
10.0 // 3.0
10.0 / 3.0
10 / 3

"a" + "bc"
"bc" * 3
"abcd"[0:2]


numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print ("ooh")


print ("Outside the loop")

num = 12
while True:
    if num > 10:
        print ("Hello!")
    elif num <= 10:
        print (num)
    elif num <= 0:
        break
    num -=2
        
x = end = 6
while True:
    if end > 0:   
        end -= 1
        x += end
    elif end <= 0:
        print (x)
        break
    
    
greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print (letter) 
    print (letter)

print ('done')



L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print("Hello," + name + "!")
    
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')




n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')  
    
    

x = "App  le"
for m in x:
    if m == "a" or m == "e":
        print("aaaaa")
    elif m == "e" or m == "l":
        print("bbbb")
    else:
        print("NO")
        
        
        
school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print (char)
    else:
        numCons -= 1

print ('numVowels is: ' + str(numVowels))
print ('numCons is: ' + str(numCons) )


num = 10
for num in range(5):
    print (num)
print (num)




divisor = 2
for num in range(0, 10, 2):
    print (num/divisor) 
    
    
for variable in range(20):
    if variable % 4 == 0:
        print (variable)
    if variable % 16 == 0:
        print ('Foo!' )
        
for variable in range(20):
    if variable % 16 == 0:
        print (variable)  
        
        
        
        
for num in range(11):
    if num % 2 == 0:
        print(num)
print("Goodbye!")



for num in range(11):
    if num % 2 == 0 and num > 0:
        print(num)
print("Goodbye!")


print ("Hello!")
for x in [10, 9, 8, 7, 6, 5, 4, 3, 2]:
    if x % 2 == 0:
        print (x)
        
        
        
        
x = 0 
for num in range(6 + 1):
    x = x + num
print (x)



for num in range(0,6):
    end += num
print (end)

iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print ("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
    
    
    
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
    
    
count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print ("Iteration " + str(iteration) + "; count is: " + str(count))
    
    
    
iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print ("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 


    
count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print ("Iteration " + str(iteration) + "; count is: " + str(count))
    
count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print ("Iteration " + str(iteration) + "; count is: " + str(count))
    
    
    
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print ("Iteration " + str(iteration) + "; count is: " + str(count))
        break
    
    
#Convert decimal positive integer to binary
num = 256
result = ''
while num >= 1:
    result = str(num % 2) + result
    num = num // 2
    
    
    
# what about fractions?
num = float(input("Enter a decimal number between 0 and 1:"))
result = ""
while num > 0 and num < 1:
    result = result + str(int(num * 2 // 1))
    num = num * 2 % 1
result = "0." + result
print(result)





x = 2554535
epsilon = 0.1 #真实值与计算值的接近程度
step = epsilon**2
numguesses = 0
ans = 0.0
while (abs(ans**2 - x)) >= epsilon and ans <= x:
    ans += step
    numguesses += 1
print('numguesses = ' + str(numguesses))
if abs(ans**2 - x) >= epsilon:
    print('Failed on sqare root of' + str(x))
else:
    print(str(ans) + ' is close to the square root of ' + str(x))


# =============================================================================
# L3 P8 find square root of int.
# =============================================================================
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        guess += step
        print(abs(guess**2 - x))
    else:
        print('succeeded: ' + str(guess))
        break
        
if abs(guess**2 - x) >= epsilon:
    print ('failed')
    
    
while True:
    if abs(guess**2 -x) < epsilon:
        print('succeeded: ' + str(guess))
        break        
    elif guess <= x:
        guess += step
        print(abs(guess**2 - x))
    else:
        print ('failed')
        break
    
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break



x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
        print(guess)
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print ('failed')
else:
    print ('succeeded: ' + str(guess))
    
# =============================================================================
# Bisection search 二分法 有三个变量 low/High/ans
# =============================================================================

x = 24
epsilon = 0.01
low = 0
high = x
ans = (low + high)/2.0
while abs(ans**2 - x) >= epsilon:
    if ans**2 > x:
        high = ans
    else:
        low = ans
    ans = (low + high)/2.0
print(str(ans) + 'is close to square root of '+ str(x))
    
# =============================================================================
# Guess Guess Guess L3 P9
# =============================================================================

Secretguess = 42
low = 0
high = 100
ans = (low + high)//2
while Secretguess != ans:
    if ans > Secretguess:
        high = ans
    else:
        low = ans
    ans = (low + high)//2
    print(ans)
    
                

#初始测试代码
Secretguess = int(input("Enter a integer between 0(inclusive) and 100(exclusive):"))
low = 0
high = 100
ans = (low + high)//2
feedback = input("Is your secret number " + str(ans) + "?" 
                 + "\n" + "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly: ")
while feedback != "c":
    if feedback == "h":
        high = ans
    if feedback == "l":
        low = ans
    ans = (low + high)//2
    if feedback != "h" and feedback != "l":
        print("Sorry, I did not understand your input.")
    feedback = input("Is your secret number " + str(ans) + "?"
                     + "\n" + "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly: ")
if feedback == "c":
    print("Game over. Your secret number was:" + str(ans))


#提交答案代码（注意input 和 raw_input）
print("Please think of a number between 0 and 100!")
low = 0
high = 100
ans = (low + high)//2
feedback = input("Is your secret number " + str(ans) + "?" 
                 + "\n" + "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
while feedback != "c":
    if feedback == "h":
        high = ans
    if feedback == "l":
        low = ans
    ans = (low + high)//2
    if feedback != "h" and feedback != "l":
        print("Sorry, I did not understand your input.")
    feedback = input("Is your secret number " + str(ans) + "?"
                     + "\n" + "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
if feedback == "c":
    print("Game over. Your secret number was:" + str(ans))

# =============================================================================
# Newton-Raphson 牛顿迭代法
    # Xn+1 = Xn - f(Xn)/f'(Xn)
# =============================================================================
epsilon = 0.01
y = 1234567.0
guess = y/2.0
while abs(guess**2 - y) >= epsilon:
    guess = guess - (guess**2 - y)/(2*guess)
    print(guess)
print("Square root of" + str(y) + "is about" + str(guess))










