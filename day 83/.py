# 1. Find the second largest and second smallest numbers in a list
# o Input: [12, 45, 2, 7, 23, 5]
# o Use loops (without sort()) to find both the second largest and second smallest
# numbers.

# x=[12, 45, 2, 7, 23, 5]
# first=float('inf')
# second=-float('inf')
# for i in x:
#     if i<first:
#         second=first
#         first=i
#     elif first<i<second:
#         second=i
#     if i>first:
#         second=first
#         first=i
#     elif first>i>second:
#         second=i
# print(second)
# print(first)

# nums = [12, 45, 2, 7, 23, 5]
# largest = second_largest = float('-inf')
# smallest = second_smallest = float('inf')
# for num in nums:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         second_largest = num
#     if num < smallest:
#         second_smallest = smallest
#         smallest = num
#     elif num < second_smallest and num != smallest:
#         second_smallest = num
# print("Second Largest:", second_largest)
# print("Second Smallest:", second_smallest)


# 2. Rotate a list to the right by one position
# o Input: [1, 2, 3, 4, 5]
# o Write a program to rotate the list so the last element becomes the first.
# o Output: [5, 1, 2, 3, 4]

# x=[1, 2, 3, 4, 5]
# y=1
# z=x[-y:]+x[0:-y]
# print(z)

# x=[1, 2, 3, 4, 5]
# # print(x[-1])
# y=[]
# z=[]
# for i in range(len(x)):
#     if x[i]==x[-1]:
#         y+=[x[i]]
#     else:
#         z+=[x[i]]
# print(y+z)


# 3. Rotate a list to the right by two positions
# o Input: [1, 2, 3, 4, 5]
# o Write a program to rotate the list so the last two elements move to the front.
# o Output: [4, 5, 1, 2, 3]

# x=[1, 2, 3, 4, 5]
# y=-2
# z=x[y:]+x[0:y]
# print(z)

# x=[1, 2, 3, 4, 5]
# y=[]
# z=[]
# for i in range(len(x)):
#     if x[i]==x[len(x)-1] or x[i]==x[len(x)-2]:
#         y+=[x[i]]
#     else:
#         z+=[x[i]]
# print(y+z)


# 4. Find all pairs with a given difference
# o Input: [1, 5, 2, 2, 3, 7], difference = 2
# o Write a program to find all unique pairs (a, b) such that a - b = 2.

# x=[1, 5, 2, 2, 3, 7]
# for i in x:
#     for j in x:
#         if i-j==2:
#             print(i,j)


# 5. Find all numbers in a list that are perfect squares
# o Input: [1, 2, 3, 4, 9, 16, 20]
# o Write a program to print all numbers which are perfect squares (e.g., 1, 4, 9, 16).

# x=[1, 2, 3, 4, 9, 16, 20]
# for i in x:
#     y= int(i)**0.5
#     if y*y==i:
#         print(i)

# nums = [1, 2, 3, 4, 9, 16, 20]
# for num in nums:
#     root = int(num ** 0.5)  
#     if root * root == num:  
#         print(num)


# num=25
# x=int(num**0.5)
# if num==x**2:
#     print('yes')
# else:
#     print('no')

# x=28
# count=0
# for i in range (1,x):
#     if x%i==0:
#         count+=i
# if count==x:
#     print('yes')
# else:
#     print('no')



# 6. Move all zeros to the end of a list
# o Input: [0, 1, 0, 3, 12]
# o Write a program to move all zeros to the end while keeping the order of non-zero
# elements.
# o Output: [1, 3, 12, 0, 0]

# x=[0, 1, 0, 3, 12]
# y=[]
# z=[]
# for i in x:
#     if i==0:
#         y+=[i]
#     else:
#         z+=[i]
# print(z+y)


# 1. Find all triplets with a given sum
# o Input: [1, 2, 3, 4, 5, 6], sum = 10
# o Write a program to find all unique triplets (a, b, c) such that a + b + c = 10.

# x=[1, 2, 3, 4, 5, 6]
# for i in range(len(x)):
#     for j in range(i,len(x)):
#         for k in range(j,len(x)):
#             if x[i]+x[j]+x[k]==10:
#                 print(x[i],x[j],x[k])


# 2. Longest increasing subsequence
# o Input: [10, 22, 9, 33, 21, 50, 41, 60]
# o Write a program to find the length of the longest strictly increasing subsequence in
# the list.

# 3. Rotate a list by n positions (both left and right)
# o Input: [1, 2, 3, 4, 5, 6], n = 3
# o Write a program to rotate the list by n positions to the left and to the right.

# x=[1, 2, 3, 4, 5, 6]
# y=3
# z=x[-y:]+x[0:-y]
# print(z)

# x=[1, 2, 3, 4, 5, 6]
# y=[]
# z=[]
# for i in range(len(x)):
#     if x[i]==x[-1] or x[i]==x[-2] or x[i]==x[-3]:
#         y+=[x[i]]
#     else: 
#         z+=[x[i]]
# print(y+z)


# 4. Merge k sorted lists into a single sorted list
# o Input: [[1, 4, 7], [2, 5, 8], [0, 3, 6]]
# o Write a program to merge all lists into one sorted list using loops (without sort() on
# the final list).

# x=[2,3,4,5,1,9,8,7,6]
# for i in range(len(x)):
#     for j in range(i+1,len(x)):
#         if x[i]>x[j]:
#             x[i],x[j]=x[j],x[i]
#         # else:
#         #     x[i],x[j]=x[j],x[i]
# print(x)



# 5. Find all sublists whose sum is zero
# o Input:[3, 4, -7, 1, 3, -1, 2, -2]
# o Write a program to find all contiguous sublists where the sum of elements is 0.

# x=[3, 4, -7, 1, 3, -1, 2, -2]
# for i in range (len(x)):
#     for j in range(i,len(x)):
#         if x[i]+x[j]==0:
#             print(x[i],x[j])


# 1. Count the number of characters in a string
# o Input: "Hello World"
# o Write a program to count the total number of characters in the string.
# o Output: 11

# x='hello world'
# count=0
# for i in x:
#     count+=1
# print(count)


# 2. Convert a string to uppercase and lowercase
# o Input: "Python"
# o Write a program to print the string in uppercase and lowercase.
# o Output:
# o Uppercase: PYTHON
# o Lowercase: python

# x='python'
# print(x.upper())
# print(x.lower())


# 3. Check if a string is a palindrome
# o Input: "madam"
# o Write a program to check whether the string reads the same forwards and
# backwards.
# o Output: True

# x='madam'
# y=''
# for i in range(len(x)-1,-1,-1):
#     y+=x[i]
# print(y)


# 4. Count the number of vowels in a string
# o Input: "Hello Python"
# o Write a program to count all vowels (a, e, i, o, u) in the string.
# o Output: 3

# x="Hello Python"
# count=0
# for i in x:
#     if i in 'aeiou':
#         count+=1
# print(count)


# 5. Reverse a string
# o Input: "Python"
# o Write a program to reverse the string.
# o Output: "nohtyP"

# x='python'
# y=''
# for i in x:
#     y=i+y
# print(y)


# 1. Count words in a string
# o Input: "Python is simple and easy to learn"
# o Write a program to count the number of words in the string.
# o Output: 7

# x="Python is simple and easy to learn"
# count=1
# for i in x:
#     if i==' ':
#         count+=1
# print(count)


# 2. Check if two strings are anagrams
# o Input: "listen" and "silent"
# o Write a program to check whether the two strings are anagrams of each other.
# o Output: True

# x='listen'
# y='silent'
# a=sorted(x)
# b=sorted(y)
# if a==b:
#     print(True)
# else:
#     print(False)

# name1='listen'
# name2='silent'
# x=list(sorted(name1))
# y=list(sorted(name2))
# if x==y:
#     print("yes it is anagram")
# else:
#     print("no it is not a anagram")


# s1 = "listen"
# s2 = "silent"
# if len(s1) != len(s2):
#     print("Not Anagrams")
# else:
#     freq1 = {}
#     freq2 = {}
#     for ch in s1:
#         if ch in freq1:
#             freq1[ch] += 1
#         else:
#             freq1[ch] = 1
#     for ch in s2:
#         if ch in freq2:
#             freq2[ch] += 1
#         else:
#             freq2[ch] = 1
#     if freq1 == freq2:
#         print("Anagrams")
#     else:
#         print("Not Anagrams")