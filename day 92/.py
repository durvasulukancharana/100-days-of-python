# 🔹 Lists & Dictionaries

# Write a program to find the largest element in a list.

# x=['apple','banana','ball']
# max=-float('inf')
# for i in range(len(x)):
#     if i>max:
#         max=i
# print(max)

# Write a program to remove duplicates from a list.

# x=[1,2,1]
# y=[]
# for i in x:
#     if i not in y:
#         y.append(i)
# print(y)

# Create a dictionary with 3 students’ names as keys and their marks as values, then print the student with the highest marks.

# max=-float('inf')
# max=-float('inf')
# x={
#     'vamsi':50,
#     'ajay':90,
#     'kumar':55
# }
# for i,j in x.items():
#     if j>max:
#         max=j
# # print(max)
# for i,j in x.items():
#     if j==max:
#         print(i,j)

# max=-float('inf')
# x={
#     'a':'vamsi',
#     'b':'ajay',
#     'c':'kumar',
#     'd':'ganesh'
# }
# for i,j in x.items():
#     if len(j)>max:
#         max=len(j)
# print(max)
# for i,j in x.items():
#     if len(j)==max:
#         print(i,j)

# Write a program to calculate the factorial of a number.

# x=5
# y=1
# for i in range(1,x+1):
#     y*=i
# print(y)


# Write a program to check if a number is prime or not.

# x=int(input('enter a num:'))
# count=0
# for i in range(1,x+1):
#     if x%i==0:
#         count+=1
# if count<=2:
#     print('prime')
# else:
#     print('no')

# Find the sum of digits of a given number (e.g., 123 → 1+2+3=6).

# x=123
# y=0
# for i in str(x):
#     y+=int(i)
# print(y)


# 🔹 Loops & Patterns

# Print the following pattern:

# *
# * *
# * * *
# * * * *

# for i in range(5):
#     print(i*'*')


# Print the Fibonacci series up to 10 terms.

# a=0
# b=1
# for i in range(10):
#     a,b=b,a+b
#     print(a)


# Write a program to find the reverse of a number (e.g., 123 → 321).

# num=123
# x=''
# for i in str(num):
#     x=i+x
# print(x)

# num=123
# x=str(num)
# for i in range(len(x)-1,-1,-1):
#     print(x[i])

# 🔹 Strings

# Write a program to count how many words are in a sentence.

# x='i love python world'
# y=x.split()
# print(y)
# print(len(y))

# Replace all spaces in a string with -.

# x='i love python world'
# y=''
# for i in x:
#     if i.isspace():
#         y+='-'
#     else:
#         y+=i
# print(y)

# Check if one string is a substring of another.

# x='i love python world'
# y='love'
# if y in x:
#     print('yes')
# else:
#     print('no')

# 🔹 Lists

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
