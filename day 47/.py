# Find the sum of prime numbers up to n.

x=int(input('enter a num :'))
sum=0
def check(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
for i in range(1,x+1):
    if check(i):
        sum+=i
print(sum)

count=0
n=int(input('enter a num :'))
for i in range(1,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        count+=i
print(count)


# Write a program to print all Armstrong numbers between 1 and 1000.

for num in range(1, 1001):
    digits = str(num)
    power = len(digits)
    total = 0    
    for i in digits:
        total += int(i) ** power
    if total == num:
        print(num)

for i in range(1,1000):
    x=str(i)
    total=0
    for j in x:
        total+=int(j)**3
    if total==i:
        print(i)


x=121
y=0
for i in str(x):
    if int(i)**3:
        y+=int(i)
if x==y:
    print('arm')
else:
    print('no')


# Write a program to print the reverse multiplication table of a number (from 10 down to 1).

for i in range(3,0,-1):
    for j in range(10,0,-1):
        print(i,'X',j,'=',i*j)

# Find the LCM of a list of numbers (not just two).

x=50
y=120
gcd=1
for i in range(1,min(x,y)+1):
    if x%i==0 and y%i==0:
        gcd=i
print(gcd)


# 🔹 Strings

# Write a program to count how many words in a sentence start with a vowel.

x='i love python in apnacollege at the end'
y=x.split()
for i in y:
    if i[0] in 'aeiou':
        print(i)


# Replace every space with an underscore in a string.

x='i love python world'
y=''
for i in x:
    if i.isspace():
        y+='_'
    else:
        y+=i
print(y)


# Write a program to check if a string is a heterogram (no letter repeats).

x='lamp'
y=''
for i in x:
    if i not in y:
        y+=i
if len(x)==len(y):
    print('hetrogram')
else:
    print('not')


# 🔹 Lists & Tuples

# Write a program to merge two sorted lists into one sorted list.

x=sorted([1,3,5,7])
y=sorted([2,4,6,8])
print(sorted(x+y))


# Remove the k-th element from a list without using pop().

x=[1,2,3,4,5]
k=2
z=x[0:k]+x[k+1:]
print(z)

x=[1,2,3,4,5]
k=2
y=[]
for i in range(len(x)):
    # print(i)
    if i != k:
        y.append(x[i])
print(y)


# 🔹 Dictionaries, Sets & Functions

# Write a program to create a dictionary where the keys are numbers from 1 to n and the values are their cubes.

n=int(input('enter a num :'))
x={}
for i in range(1,n+1):
    x[i]=i**3
print(x)


# Write a function that counts how many times each digit (0-9) appears in a given number.

x='1234554321686'
# a=str(x)
y={}
for i in x:
    if i not in y:
        y[i]=1
    else:
        y[i]+=1
print(y)

num = int(input("Enter a number: "))
num_str = str(num)
counts = {}
for i in range(10):
    counts[str(i)] = 0
for ch in num_str:
    if ch.isdigit():
        counts[ch] += 1
for d in counts:
    print(d, ":", counts[d])
