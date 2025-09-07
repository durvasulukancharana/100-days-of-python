# Write a program to find the sum of factorials of first n natural numbers.

x=int(input('enter a num:'))
for i in range(1,x+1):
    if x%i==0:
        print(i)

# Find all perfect squares between 1 and 500.

num=25
x=int(num**0.5)
if num==x**2:
    print('yes')
else:
    print('no')

x=28
count=0
for i in range (1,x):
    if x%i==0:
        count+=i
if count==x:
    print('yes')
else:
    print('no')


# 🔹 Loops & Patterns

# Print this star pattern:

# *****
#  ****
#   ***
#    **
#     *

n=5
for i in range(1,n):
    print(' '*(n-i)+'* '*i)

rows=3
columns=8
for i in range(1,rows+1):
    print('* '*columns)

for i in range(1,5):
    print('* '*i)

for i in range(1,5):
    print(' '*(5-i)+'*'*i)

for i in range(1,5):
    print(' '*(i)+'*'*(5-i))

for i in range(1,5):
    print('*'*i)

for i in range(1,5):
    print('* '*(5-i))
    

# Write a program to display the multiplication tables from 1 to 5.

x=5
for i in range(1,6):
    for j in range(1,11):
        print(i,'X',j,'=',i*j)
        

# Write a program to calculate the sum of even digits of a number.

x=123456
z=0
for i in str(x):
    y=i
    if int(i)%2==0:
        z+=int(i)
print(z)

x=101
count=0
for i in str(x):
    count+=int(i)
print(count)


# 🔹 Strings

# Write a program to remove all consonants from a string.

x='vamsi'
y=''
for i in x:
    if i in 'aeiou':
        y+=i
print(y)

# Count how many times each vowel appears in a string.

# 🔹 Lists & Tuples

# Write a program to split a list into two lists: even numbers and odd numbers.

x=[1,2,3,4,5,6,7,8]
y=[]
z=[]
for i in x:
    if i%2==0:
        y=y+[i]
    else:
        z=z+[i]
print(y)
print(z)


# Find the second smallest element in a list.

x=[1,2,3,4,5,6,-1]
first=second=float('inf')
for i in x:
    if i<first:
        second=first
        first=i
    elif first<i<second:
        second=i
print(second)


# Convert a list of numbers into a list of their binary equivalents.

x=[1,2,7,9,15,25]
y=[]
for i in x:
    y.append(bin(i)[2:])
print(y)

# 🔹 Dictionaries, Sets & Functions

# Write a program to invert a dictionary (swap keys and values).

x={1:'a',2:'b',3:'c'}
y={value:key for key,value in x.items()}
print(y)

# Write a function that returns the union of multiple sets (not just two).

def fun():
    x={1,2,3,4}
    y={3,4,5,6}
    z={5,6,7,8}
    print(x.union(y,z))
fun()


# Write a function that accepts a sentence and returns a dictionary of word lengths.
# Example: "I love Python" → {"I":1, "love":4, "Python":6}
x='i love python'
y=x.split()
z={}
for i in y:
    z[i]=len(i)
print(z)
