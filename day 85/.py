# Write a program to calculate the factorial of a number using recursion.

# x=int(input('enter a num : '))
# y=1
# for i in range(1,x+1):
#     y*=i
# print(y)


# Print the first n triangular numbers (1, 3, 6, 10, …).

# Print first n triangular numbers

# n = int(input("Enter how many triangular numbers: "))
# for i in range(1, n + 1):
#     triangular = i * (i + 1) // 2
#     print(triangular, end=" ")



# 🔹 Strings

# Write a program to reverse each word in a sentence (not the sentence itself).

# x='hello every one'
# y=''
# for i in x:
#     y=i+y
# print(y)

# x='hello every one'
# y=''
# z=x.split()
# for i in z:
#     y=i+' '+y
# print(y)


# Count the number of uppercase, lowercase, digits, and spaces in a string.

# x='Heyy EvErY OnE !@#$ hOW ArE yoU 143'
# upper=0
# lower=0
# digit=0
# space=0
# special=0
# for i in x:
#     if i.isupper():
#         upper+=1
#     elif i.islower():
#         lower+=1
#     elif i.isdigit():
#         digit+=1
#     elif i.isspace():
#         space+=1
#     else:
#         special+=1
# print(lower,upper,digit,space,special)


# Write a program to find the longest palindrome word in a sentence.




# 🔹 Lists & Tuples

# Write a program to find the median of a list of numbers.

# Merge two lists and remove duplicates.

# Write a program to rotate a list to the right by k positions.

# x=[1,2,3,4,5]
# k=2
# z=x[-k:]+x[0:-k]
# print(z)


# 🔹 Dictionaries, Sets & Functions

# Create a dictionary of countries and capitals, then allow the user to search for a capital by country name.

# x={
#     'india':'new_elhi',
#     'nepal':'bhutan',
#     'srilanka':'colombo',
#     'bangladesh':'dhaka'
# }
# country = input("Enter country name: ")
# if country in x:
#     print(country,x[country])
# else:
#     print('there is no data')

# x={'name':'vamsi','age':28,'village':'ongole'}
# y={value:key for key,value in x.items()}
# print(y)

# x={'name':'vamsi','age':28,'village':'ongole'}
# y={}
# for i,j in x.items():
#     y[j]=i
# print(y)


# Write a function to find the common elements across three sets.

# def set(a,b,c):
#     return a & b & c
# x={1,2,3}
# y={3,2,1}
# z={1,2,4}
# n=set(x,y,z)
# print(n)

# Write a function that takes a list of numbers and returns a dictionary with even and odd numbers separated.

# x=[1,2,3,4,5,6]
# y={'even':[],'odd':[]}
# for i in x :
#     if i%2==0:
#         y['even'].append(i)
#     else:
#         y['odd'].append(i)
# print(y)


# Even or Odd
# Write a program that checks whether a given number is even or odd.

# x=int(input('enter a num : '))
# if x%2==0:
#     print('true')
# else:
#     print('false')


# Factorial of a Number
# Write a program to find the factorial of a number without using recursion.

# x=int(input('enter a num : '))
# y=1
# for i in range(1,x+1):
#     y*=i
# print(y)


# Largest of Three Numbers
# Take three numbers as input and display the largest among them.

# x=int(input('enter a num : '))
# y=int(input('enter a num : '))
# z=int(input('enter a num : '))
# if x>=y and x>=z:
#     print(x)
# elif y>=x and y>=z:
#     print(y)
# else:
#     print(z)

# x=int(input('enter a num : '))
# y=int(input('enter a num : '))
# z=int(input('enter a num : '))
# if x>=y and x<=z:
#     print(x)
# elif y>=x and y<=z:
#     print(y)
# else:
#     print(z)


# Palindrome Check
# Write a program to check if a given string is a palindrome or not.

# x=input('enter a name : ')
# y=''
# for i in x:
#     y=i+y
# if x==y:
#     print('palindrome')
# else:
#     print('not a palindrome')


# x=int(input('enter a name : '))
# z=x
# y=0
# while x>0:
#     y=x%10+y*10
#     x//=10
# if z==y:
#     print('palindrome')
# else:
#     print('not a plindrome')


# Sum of Digits
# Write a program that finds the sum of digits of a given number.

# x=int(input('enter a num : '))
# y=0
# for i in str(x):
#     y+=int(i)
# print(y)


# Fibonacci Series
# Generate the first n terms of the Fibonacci sequence.

# x=int(input('enter a num : '))
# a,b=0,1
# while a<=x:
#     print(a,b)
#     a,b=b,a+b


# Count Vowels in a String
# Write a program that counts the number of vowels in a given string.

# x=input('enter a name : ')
# count=0
# for i in x:
#     count+=1
# print(count)


# Reverse a List
# Write a program to reverse a list without using built-in reverse functions.

# x=[1,2,3]
# y=[]
# for i in range(len(x)-1,-1,-1):
#     y.append(x[i])
# print(y)
