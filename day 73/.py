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


# 1. Check Prime Number

# def check(num):
#     if num<2:
#         return False
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
# print(check(5))


# x=int(input('enter a num : '))
# for i in range(1,x+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
# else:
#     print('prime')


# x=int(input('enter a num : '))
# count=0
# for i in range(1,x+1):
#     if x%i==0:
#         count+=1
# if count==2:
#     print('prime')
# else:
#     print('not prime')


# 2. Find GCD (Greatest Common Divisor)

# x=10
# y=23
# z=0
# for i in range(1,min(x,y)+1):
#     if x%i==0 and y%i==0:
#         z=i
# print(z)

# a=10
# b=23
# while b:
#     a,b=b,a%b
# print(a)    


# 3. Count Words in a Sentence

# x='hello how are you'
# y=x.split()
# count=0
# for i in y:
#     count+=1
# print(count)


# p="hello world example"
# count=0
# for i in range(1,len(p)):
#     if p[i-1]==" ":
#         count+=1
#     # elif p[i]==" ":
#     #     pass
#     else:
#         # o+=p[i]
#         pass
# print(count)


# 4. Find Second Largest Number in a List

# x=[1,4,2,1]
# x.sort()
# print(x[-2])

# x=[1,2,3]
# first=0
# second=0
# for i in x:
#     if i>first:
#         second=first
#         first=i
#     elif first>i>second:
#         second=i
# print(second)

# x=[1,2,3]
# first=0
# second=0
# for i in x:
#     if i>first:
#         second=first
#         first=i
#     elif first<i<second:
#         second=i
# print(second)


# 5. Check Armstrong Number

# x=153
# y=0
# for i in str(x):
#     y+=int(i)**3
# if x==y:
#     print('arm')
# else:
#     print('not')


# num=int(input('enter a number:'))
# temp=num
# s=0
# count=0
# while temp>0:
#     count+=1
#     temp//=10
# temp=num
# while temp>0:
#     s+=(temp%10)**3
#     temp//=10
    
# if s==num:
#     print('arm')
# else:
#     print('not')