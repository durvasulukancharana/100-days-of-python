# Write a program to print the first 10 natural numbers using a loop.

for i in range(1,11):
    print(i)


# Write a program to find the sum of all numbers in a list.

x=[1,2,3,4,5,6]
print(sum(x))

x=[1,2,3,4,5]
y=0
for i in x:
    y+=i
print(y)


# Given a string, count how many vowels it contains.

x='vamsi'
for i in x:
    if i in 'aeiou':
        print(i)


# Create a dictionary from two lists: keys = ['a','b','c'], values = [1,2,3].

keys=['a','b','c']
values = [1,2,3]
print(dict(zip(keys,values)))


# Write a program to check if a given number is even or odd.

x=10

if x% 2==0:
    print('even')


# Print all elements of a list along with their index using enumerate.

x=[1,2,3,4,5]
y=enumerate(x)
print(y)


# Write a program to find the maximum number in a list without using max().

x=[1,2,3]
print(max(x))

x=[1,2,3,4]
max=-float('inf')
for i in x:
    if i>max:
        max=i
print(max)

# Write a program to merge two lists into a dictionary (list1 → keys, list2 → values).

x=[1,2,3]
y=['a','b','c']
print(dict(zip(x,y)))


# Write a program to reverse a string without using slicing ([::-1]).

x='vamsi'
y=x[::-1]
print(y)

x='vamsi'
y=''
for i in x:
    y=i+y
print(y)

x='ismav'
for i in range(len(x)-1,-1,-1):
    print(x[i])

# Write a program to count the frequency of each word in a file.

x='pablo is a very very very good boy'
z=x.split()
y={}
for i in z:
    if i not in y:
        y[i]=1
    else:
        y[i]+=1
print(y)


# Write a program to remove duplicates from a list.

x=[1,2,3,4,5,6,7]
y=[]
for i in x:
    if i not in y:
        print(i)


# Given a dictionary, find the key with the largest value.

x={
    'a':'vamsi',
    'b':'ajay',
    'c':'raviteja'
}
max=-float('inf')
for i,j in x.items():
    if len(j)>max:
        max=len(j)
print(max)
for i,j in x.items():
    if len(j)==max:
        print(i,j)


# Write a program to check if a given substring exists in a string.

x='hii hello every one'
y='hii'
if y in x:
    print('true')
else:
    print('false')


# Write a program to print all prime numbers between 1 and 50.

for i in range(50,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)


# Given a list of numbers, print the second largest number.

x=[1,2,3,4,5,6]
first=0
second=0
for i in x:
    if i>first:
        second=first
        first=i
    elif first>i and second<i:
        second=i
print(second)


# Write a program to find the sum of all even numbers in a given range.

x=0
for i in range (1,20):
    if i %2==0:
        x+=i
print(x)



# Write a program to check if two strings are anagrams of each other.

x='listen'
y='silent'
a=sorted(x)
b=sorted(y)
if a==b:
    print('anagram')
else:
    print('not a anagram')


# Write a program to sort a dictionary by its values in descending order.

x={'a':3,'b':1,'c':7,'d':2}
y=sorted(x.values())
print(y)


# Write a program to generate Fibonacci numbers up to n using recursion.

a,b=0,1
for i in range(6):
    a,b=b,a+b
    print(a)


# Write a program to read a nested dictionary and print all keys and values in a structured format.

x={
    'name':'vamsi',
    'marks':{
        'phy':95,
        'chem':89,
        'math':99
    }
}
print(x['name'])
