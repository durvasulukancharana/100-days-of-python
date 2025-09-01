# Check if a number is a palindrome number (e.g., 121 → palindrome).

x=121
y=str(x)
z=''
for i in range(len(y)-1,-1,-1):
    z+=y[i]
if z==y:
    print('palindrome')
else:
    print('not a palindrome')


# Find the sum of prime numbers between 1 and 100.
sum=0
for i in range(1,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sum+=i
print(sum)


# Write a program to find the factorial using a loop (not recursion).
x=5
y=1
for i in range(1,x+1):
    y*=i
print(y)

# Print all numbers from 1–100 that are divisible by both 3 and 5.

for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)

# 🔹 Strings

# Write a program to remove all punctuation marks from a string.

x='vamsi!enduri!!@#$%^&*'
y=''
for i in x:
    if i.isalpha():
        y+=i
print(y)

x='vamsi!enduri!!@#$%^&*'
y=''
for i in x:
    if not i.isalpha():
        y+=i
print(y)


# Find the first non-repeated character in a string.

x='aabbccdefe'
y=''
z=''
for i in x:
    if i not in y:
        y+=i
    else:
        z+=i
# print(y)
# print(z)
for i in y:
    if i not in z:
        print(i)
        break

# Count how many times each word appears in a sentence.

x='hello guys how are you you know who you are'
y=x.split()
z={}
for i in y:
    if i not in z:
        z[i]=1
    else:
        z[i]+=1
print(z)


# 🔹 Lists

# Find the maximum and minimum elements in a list without using max() and min().

x=[1,2,3]
min=float('inf')
for i in x:
    if i<min:
        min=i
print(min)

x=[1,2,3]
max=-float('inf')
for i in x:
    if i>max:
        max=i
print(max)

x='i ove my india'
y=x.split()
z=''
for i in y:
    if len(i)>len(z):
        z=i
print(z)
print(len(z))

x='i ove my india'
y=x.split()
z=''
for i in y:
    if i.isalpha():
        if len(i)<len(z):
            z=i
print(z)
print(len(z))

# Write a program to separate even and odd numbers into two lists.

x=[1,2,3,4,5,6]
y=[]
z=[]
for i in x:
    if i%2==0:
        y.append(i)
    else:
        z.append(i)
print(y)
print(z)


# 🔹 Dictionaries, Sets & Functions

# Write a function that accepts a dictionary of students and marks, and returns the student with highest marks.

def topper():
    max=-float('inf')
    x={
        'vamsi':80,
        'ravi':90,
        'ajay':99,
        'kumar':98
    }
    for i,j in x.items():
        if j>max:
            max=j
    # print(max)
    for i,j in x.items():
        if j==max:
            print(i,j)
topper()


# Create a set from a list and show how it automatically removes duplicates.

x=[1,2,3,4,5,6,1,2,3,4]
y=set(x)
print(x,y)
