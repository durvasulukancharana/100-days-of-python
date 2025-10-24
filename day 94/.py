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


# 🔹 Strings

# Write a program to check if a string contains only alphabets (no numbers/special characters).

# x='helloeveryone'
# if x.isalpha():
#     print('yes')
# else:
#     print('no')

# Count how many uppercase and lowercase letters are in a string.

# x='VAMSI enduri'
# y=0
# z=0
# for i in x:
#     if i.isupper():
#         y+=1
#     elif i.islower():
#         z+=1
# print(y)
# print(z)

# Write a program to find the longest word in a sentence.

# x='i love my india'
# y=x.split()
# z=''
# for i in y:
#     if len(i)>len(z):
#         z=i
# print(z)


# 🔹 Lists

# Write a program to find the average of numbers in a list.
# x=[1,2,3,4,5]
# y=0
# for i in x:
#     y+=i
# print(y/len(x))


# Write a program to remove all negative numbers from a list.

# x=[1,2,3,4,-1,-2,-3,-4]
# y=[]
# for i in x:
#     if i > 0:
#         y.append(i)
# print(y)

# Flatten a 2D list into a 1D list.
# Example: [[1,2],[3,4]] → [1,2,3,4]

# 🔹 Dictionaries, Sets & Functions

# Write a function to merge two lists into a dictionary (keys from one list, values from another).
# x=[1,2,3]
# y=['a','b','c']
# z=dict(zip(x,y))
# print(z)


# Write a program to find the union, intersection, and difference of two sets.
# a={1,2,3,4,5}
# b={3,4,5,6,7,8}
# print(a.union(b))

# a={1,2,3,4,5}
# b={3,4,5,6,7,8}
# print(a.intersection(b))

# a={1,2,3,4,5}
# b={3,4,5,6,7,8}
# print(b.difference(a))


# Write a function that checks if a given word is a pangram (contains all letters a–z).

# y= 'Vamsi'
# x= "abcdefghijklmnopqrstuvwxyz"

# for i in x.lower(): 
#     if i not in y:
#         print("no")
#         break
# else:
#     print("yes")

# sum=0
# for i in range(100,50,-1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)
#         sum+=i
# print(sum)
