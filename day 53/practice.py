# Interview Questions – Logic-Based Programs

# 🔢 Prime and Armstrong Logic Questions
# 1. Print All Prime Numbers from m to n
# Problem: Given a range from m to n, print all prime numbers in that range.
# Input: m = 10, n = 30
# Output: 11 13 17 19 23 29
# Explanation: A prime number has only two factors: 1 and itself.

n=int(input('enter a num :'))
count=0
for i in range(1,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)

n=int(input('enter a num :'))
def check(num):
    if num<2:
        return False
    for i in range(2,num):
        if num % i==0:
            return False
    return True
for i in range(1,n):
    if check(i):
        print(i)


# 2. Count of All Prime Numbers from m to n
# Problem: Count how many prime numbers are there between m and n.
# Input: m = 1, n = 10
# Output: 4
# Explanation: Prime numbers are: 2, 3, 5, 7

m=int(input('enter a num :'))
n=int(input('enter a num :'))
count=0
for i in range(m,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        count+=1
print(count)

def check(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
count=0
for i in range(1,10):
    if check(i):
        count+=1
print(count)


# 3. Print All Armstrong Numbers in a Range
# Problem: Print all Armstrong numbers between m and n.
# Input: m = 1, n = 500
# Output: 1 153 370 371 407
# Explanation: Armstrong number = sum of each digit raised to the power of number of digits.

for i in range(1,500):
    x=str(i)
    z=len(x)
    y=0
    for j in x:
        y+=int(j)**z
    if y==i:
        print(i)

x=122
y=0
while x>0:
    y=x%10+y*10
    x//=10
print(y)


# 4. First Prime Number from m to n
# Problem: Find the first prime number in the given range.
# Input: m = 10, n = 25
# Output: 11

m=10
n=25
for i in range (m,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
        break

def check(num):
    if num<2:
        return False
    for i in range (2,num):
        if num%i==0:
            return False
    return True
for i in range(10,25):
    if check(i):
        print(i)
        break


# 5. Last Prime Number from m to n
# Problem: Find the last prime number in the given range.
# Input: m = 10, n = 25
# Output: 23

m=10
n=25
x=0
for i in range (m,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        x=i
print(x)
        
def check(num):
    if num<2:
        return False
    for i in range (2,num):
        if num%i==0:
            return False
    return True
x=0
for i in range(10,25):
    if check(i):
        x=i
print(x)

# 6. First Vowel in a Name
# Problem: Given a string, find the first vowel in the string.
# Input: name = "Krishna"
# Output: i
# Explanation: First vowel from left is ‘i’

name='krishna'
for i in name:
    if i in 'aeiou':
        print(i)
        break


# 7. Last Vowel in a Name
# Problem: Given a string, find the last vowel in the string.
# Input: name = "Ramakrishna"
# Output: a
# Explanation: Last vowel is ‘a’

name='ramakrishnae'
x=''
for i in name:
    if i in 'aeiou':
        x=i
print(x)


# 8. Print All Even Numbers Using Continue
# Problem: Use continue statement to skip odd numbers and print only even numbers between 1 and n.
# Input: n = 10
# Output: 2 4 6 8 10

for i in range(1,10):
    if i % 2 !=0:
        continue
    else:
        print(i)


# 9. Print All Odd Numbers Using Continue
# Problem: Use continue statement to skip even numbers and print only odd numbers.
# Input: n = 10
# Output: 1 3 5 7 9

for i in range(1,10):
    if i % 2 ==0:
        continue
    else:
        print(i)


# 10. Count of Prime and Composite Numbers from m to n
# Problem: Count how many are prime and how many are composite numbers in range m to n.
# Input: m = 1, n = 10
# Output: Prime: 4, Composite: 4
# Explanation: Prime: 2,3,5,7 | Composite: 4,6,8,9

x=0
y=0
# count=0
for i in range(1,10):
    count=0
    for j in range(1,10):
        if i%j==0:
            count+=1
    if count==2:
        x+=1
    else:
        y+=1
print(x,y)

