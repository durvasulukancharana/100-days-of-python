# Write a program to find the second largest number in a list.

# nums=[1,2,3,4,5,6]
# x=0
# y=0
# for i in range(len(nums)+1):
#     if i>x:
#         y=x
#         x=i
#     elif x>i and i>y:
#         y=i
# print(y)


# Reverse a list without using reverse().

# x=[1,2,3,4,5]
# x.reverse()
# print(x)


# Write a program to count how many times each element appears in a list.

# x=[1,2,3,4,5,4,3,2,1,2,3,4,5,6,7]
# y={}
# for i in x:
#     if i not in y:
#         y[i]=1
#     else:
#         y[i]+=1
# print(y)


# 🔹 Dictionaries & Sets

# Write a program to merge two dictionaries.

# x={1:'apple',2:'ball'}
# y={3:'cat',4:'dog'}
# x.update(y)
# print(x)


# Create a dictionary and print only the keys.

# x={'a':1,'b':2,'c':3}
# for i in x.keys():
#     print(i)


# Write a program to remove duplicates from a list using a set.

# x={1,2,3,4,3,2,1}
# print(x)


# Write a program to check if a number is an Armstrong number (e.g., 153 → 1³+5³+3³=153).

# x=153
# y=0
# for i in str(x):
#     y+=int(i)**3
# print(y)
# if x==y:
#     print('arm')
# else:
#     print('not')

# x=int(input('enter a num:'))
# y=0
# for i in str(x):
#     y+=int(i)**3
# # print(y)
# if x==y:
#     print('arm')
# else:
#     print('not')


# Find the greatest common divisor (GCD) of two numbers.

# Write a program to generate a random number between 1 and 100.

# import random
# x=random.randint(1,100)
# print(x)


# 🔹 Loops & Series

# Print the sum of all even numbers from 1 to 50.

# x=0
# for i in range(1,51):
#     if i%2==0:
#         x+=i
# print(x)

# Print this pattern:

# 1
# 1 2
# 1 2 3
# 1 2 3 4

# for i in range(1,5):
    # for j in range(1,i+1):
    #     print(j,end='')
    # print()


# Find the sum of a geometric series (e.g., 2 + 4 + 8 + 16 … up to n terms).

# x=int(input('enter:'))
# count=0
# for i in range(1,x):
#     count+=i*2
# print(count)


# 🔹 Strings

# Count how many digits, alphabets, and special characters are in a string.

# x='virat@123'
# a=0
# b=0
# c=0
# for i in x:
#     if i.isdigit():
#         a+=1
#     elif i.isalpha():
#         b+=1
#     else:
#         c+=1
# print(a)
# print(b)
# print(c)

# Write a program to check if two strings are anagrams (e.g., listen → silent).

# x='listen'
# y='silent'
# a=sorted(x)
# b=sorted(y)
# if a==b:
#     print('yes')
# else:
#     print('no')

# Convert a string into title case (first letter of each word capitalized).

# x='hello i love python world'
# print(x.title())

# x='hello i love python world'
# y=''
# x=x.split()
# for i in x:
#     y+=i.capitalize()+' '
# print(y)


# 🔹 Lists & Tuples

# Write a program to find the common elements between two lists.

# x=[1,2,3,4,3,2,1,4]
# y=[]
# z=[]
# for i in x:
#     if i not in y:
#         y.append(i)
#     else:
#         z.append(i)
# print(z)

# x=[1,2,3,4,5,9,8,7]
# y=[1,2,3,4,5,6]
# z=[]
# for i in x:
#     if i in y:
#         z.append(i)
# print(z)

# Convert a list into a tuple.

# x=[1,2,3,4,5]
# print(tuple(x))

# x=tuple([1,2,3,4])
# print(x)

# Write a program to sort a list in descending order without using sort().

# x=[9,8,7,6,5,4,3]
# x.sort()
# print(x)

# x=[9,8,7,6,5,4,3]
# for i in range(len(x)):
#     for j in range(i+1,len(x)):
#         if x[i]>x[j]:
#             x[i],x[j]=x[j],x[i]
# print(x)


# 🔹 Dictionaries & Functions

# Write a function to count the frequency of characters in a string using a dictionary.

# x='vikatakavi'
# y={}
# for i in x:
#     if i not in y:
#         y[i]=1
#     else:
#         y[i]+=1
# print(y)


# Write a function that returns the square of all numbers in a given list.

# def sqr():
#     for i in range(1,6):
#         print(i**2)
# sqr()

# def sqr(x):
#     y=[]
#     for i in x:
#         y.append(i**2)
#     print(y)
# sqr([1,2,3,4])

# Create a dictionary of 5 items and print them in sorted order by keys.

# x={2:'a',4:'v',1:'w',3:'x'}
# for key in sorted(x.keys()):
#     print(key,':',x[key])

# x={2:'a',4:'v',1:'w',3:'x'}
# for i,j in sorted(x.items()):
#     print(i,j)

# x={2:'a',4:'v',1:'w',3:'x'}
# y=list(x)
# for i in range(len(y)):
#     for j in range(i+1,len(y)):
#         if y[i]>y[j]:
#             y[i],y[j]=y[j],y[i]
# # print(y)
# for i in y:
#     print(i,x[i])

# Write a program to check if a number is a perfect number (sum of divisors equals the number, e.g., 28 → 1+2+4+7+14 = 28).

# num=28
# x=0
# for i in range(1,num):
#     if num%i==0:
#         x+=i
# if num==x:
#     print('yes')
# else:
#     print('no')


# Find the LCM (Least Common Multiple) of two numbers.

# Convert a decimal number to binary (without using bin()).

# 🔹 Loops & Patterns

# Print the following pattern:

# * * * *
# * * *
# * *
# *
# for i in range(5,0,-1):
#     print(i*'* ')
# print()


# Write a program to calculate the sum of squares of first n natural numbers.

# n=int(input('enter a num:'))
# x=0
# for i in range(1,n+1):
#     x+=(i**2)
# print(x)

# Generate the first 15 numbers of the Fibonacci sequence.

# a=0
# b=1
# for i in range(15):
#     print(a)
#     a,b=b,a+b