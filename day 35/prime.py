# 🔹 Beginner Level

# Write a program to check if a given number is prime.

x=int(input('enter a num:'))
count=0
for i in range(1,x+1):
    if x%i==0:
        count+=1
if count==2:
    print('prime')
else:
    print('not a prime')


num=int(input('enter a num:'))
def check(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    else:
        return True
print(check(num))

# Print all prime numbers between 1 and 50.

for i in range(1,50):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)

def check(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
for i in range(1,50):
    if check(i):
        print(i)


# Find the sum of all prime numbers between 1 and n.

n=int(input('enter a num:'))
sum=0
for i in range(1,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sum+=i
print(sum)


# Count how many prime numbers are there between 1 and n.

n=int(input('enter a num:'))
count=0
for i in range(1,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        count+=1
print(count)


# Input a number and print the next prime number after it.

def check(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
num=int(input('enter a num:'))
high=num+1
if check(num):
    print(num)
else:
    while True:
        if check(high):
            print(high)
            break
        high+=1


# 🔹 Intermediate Level

# Input a number and print the nearest prime (smaller or larger).

def check(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
num=int(input('enter a num:'))
high=num+1
low=num-1
if check(num):
    print(num)
else:
    while True:
        if check(high):
            print(high)
            break
        elif check(low):
            print(low)
            break
        high+=1
        low-=1

# Input a number and print the two nearest primes if they are equally close.
# (Example: 12 → 11 and 13)

def check(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
num=int(input('enter a num'))
high=num+1
low=num-1
if check(num):
    print(num)
else:
    count=0
    while count<2:
        if check(high):
            count+=1
            print(high)
        if check(low):
            count+=1
            print(low)
        high+=1
        low-=1

# Write a program to print the first 20 prime numbers.

count=[]
for i in range(1,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        count.append(i)
    
    if len(count)==20:
        break
print(count)


def check(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
x=[]
for i in range(1,100):
    if check(i):
        x.append(i)
    if len(x)==20:
        break
print(x)


def check(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
x=2
y=[]
while x>1:
    if check(x):
        y.append(x)
    if len(y)==20:
        break
    x+=1
print(y)