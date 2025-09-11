# Write a program to check if a number is a perfect number (sum of divisors equals the number, e.g., 28 → 1+2+4+7+14 = 28).

num=28
x=0
for i in range(1,num):
    if num%i==0:
        x+=i
if num==x:
    print('yes')
else:
    print('no')


# 🔹 Loops & Patterns

# Print the following pattern:

# * * * *
# * * *
# * *
# *
for i in range(5,0,-1):
    print(i*'* ')
print()


# Write a program to calculate the sum of squares of first n natural numbers.

n=int(input('enter a num:'))
x=0
for i in range(1,n+1):
    x+=(i**2)
print(x)

# Generate the first 15 numbers of the Fibonacci sequence.

a=0
b=1
for i in range(15):
    print(a)
    a,b=b,a+b


# 🔹 Strings

# Write a program to check if a string contains only alphabets (no numbers/special characters).

x='helloeveryone'
if x.isalpha():
    print('yes')
else:
    print('no')

# Count how many uppercase and lowercase letters are in a string.

x='VAMSI enduri'
y=0
z=0
for i in x:
    if i.isupper():
        y+=1
    elif i.islower():
        z+=1
print(y)
print(z)

# Write a program to find the longest word in a sentence.

x='i love my india'
y=x.split()
z=''
for i in y:
    if len(i)>len(z):
        z=i
print(z)


# 🔹 Lists

# Write a program to find the average of numbers in a list.
x=[1,2,3,4,5]
y=0
for i in x:
    y+=i
print(y/len(x))


# Write a program to remove all negative numbers from a list.

x=[1,2,3,4,-1,-2,-3,-4]
y=[]
for i in x:
    if i > 0:
        y.append(i)
print(y)

# 🔹 Dictionaries, Sets & Functions

# Write a function to merge two lists into a dictionary (keys from one list, values from another).
x=[1,2,3]
y=['a','b','c']
z=dict(zip(x,y))
print(z)


# Write a program to find the union, intersection, and difference of two sets.
a={1,2,3,4,5}
b={3,4,5,6,7,8}
print(a.union(b))

a={1,2,3,4,5}
b={3,4,5,6,7,8}
print(a.intersection(b))

a={1,2,3,4,5}
b={3,4,5,6,7,8}
print(b.difference(a))


# Write a function that checks if a given word is a pangram (contains all letters a–z).

y= 'Vamsi'
x= "abcdefghijklmnopqrstuvwxyz"

for i in x.lower(): 
    if i not in y:
        print("no")
        break
else:
    print("yes")

sum=0
for i in range(100,50,-1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
        sum+=i
print(sum)