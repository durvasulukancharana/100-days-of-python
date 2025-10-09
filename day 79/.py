# 1. Find the Largest Element in a List
# x=[1,2,3]
# print(max(x))

# x=[1,2,3]
# max=-float('inf')
# for i in x:
#     if i>max:
#         max=i
# print(max)


# 2. Count Even and Odd Numbers in a List

# x=[1,2,3,4,5,5]
# y=0
# z=0
# for i in x:
#     if i%2==0:
#         y+=1
#     else:
#         z+=1
# print(y,z)


# 3. Reverse a String

# x='string'
# print(x[::-1])

# x='string'
# for i in range(len(x)-1,-1,-1):
#     print(x[i],end='')


# 5. Calculate Power Without Using ** Operator

# base = int(input("Enter base: "))
# exp = int(input("Enter exponent: "))
# result = 1

# for i in range(exp):
#     result *= base

# print(f"{base} to the power {exp} is:", result)


# armstrong number

# x=int(input('enter a num : '))
# z=x
# count=0
# while x>0:
#     count+=1
#     x//=10
# x=z
# y=0
# while x>0:
#     y+=(x%10)**count
#     x//=10
# if z==y:
#     print('yes')
# else:
#     print('noo')


# palindrome

# x=int(input('enter a num : '))
# y=0
# while x>0:
#     y=(x%10)+(y*10)
#     x//=10
# print(y)

# x=int(input('enter a num : '))
# y=0
# while x>0:
#     y=(x%10)+(y*10)
#     x//=10
# print(y)


# 6. Check if String Contains Only Digits

# x='123'
# if x.isdigit():
#         print('yes')
# else:
#         print('no')


# 8. Find Common Elements Between Two Lists

# x=[1,2,3,4,5]
# y=[1,2,3,4,5,6]
# for i in x:
#     if i in y:
#         print(i)


# Sum of Natural Numbers
# Write a program to calculate the sum of the first n natural numbers.

# n=int(input('enter a num : '))
# x=0
# for i in range(1,n+1):
#     x+=i
# print(x)


# Leap Year Check
# Write a program that checks if a given year is a leap year or not.

# year=int(input('enter a year here : '))
# if year %4 ==0 and year %100 !=0:
#     print('leap year')
# else:
#     print('not a leap year')


# Find Minimum in a List
# Write a program to find the smallest number in a list.

# x=[1,2,3]
# min=float('inf')
# for i in x:
#     if i<min:
#         min=i
# print(min)


# Character Frequency
# Write a program to count the frequency of each character in a string.

# x={'a':'vamsi','b':'ajay','c':'raviteja'}
# max=-float('inf')
# for key,values in x.items():
#     if len(values)>max:
#         max=len(values)
# for key,values in x.items():
#     if len(values)==max:
#         print(key,values)




# Prime Numbers in Range
# Write a program to print all prime numbers between 1 and 100.

# def check(num):
#     if num<2:
#         return False
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
# for i in range(1,100):
#     if check(i):
#         print(i)

# for i in range(1,100):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)


# Matrix Addition
# Write a program to add two 2D lists (matrices).

# Check Anagram
# Write a program to check if two strings are anagrams of each other.

# x='listen'
# y='silent'
# if sorted(x)==sorted(y):
#     print('anagram')
# else:
#     print('not')


# Find Unique Elements
# Write a program to find elements that appear only once in a list.
# x=[1,2,3,4,5,6,4,3,2,1]
# y=[]
# z=[]
# for i in x:
#     if i not in y:
#         y.append(i)
#     else:
#         z.append(i)
# for i in y:
#     if i not in z:
#         print(i)


# x='i love python'
# y=1
# for i in x:
#     if i==' ':
#         y+=1
#     else:
#         pass
# print(y)

# x='i love python'
# y=x.split()
# z={}
# for i in y:
#     z[i]=len(i)
# print(z)


# Swap keys and values in a dictionary.
# x={'a':1,'b':2,'c':3}
# swap={value:key for key,value in x.items()}
# print(swap)


# x={'a':1,'b':2,'c':3}
# y={}
# for i,j in x.items():
#     y[j]=i
# print(y)
