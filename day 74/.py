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
