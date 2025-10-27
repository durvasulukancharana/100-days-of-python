
# Find all numbers divisible by both 3 and 5 in a list
# o Input: [10, 15, 20, 30, 45, 50]
# o Use a loop and if-else to create a new list of numbers divisible by both 3 and 5.

# x=[10, 15, 20, 30, 45, 50]
# for i in x:
#     if i%3==0 and i%5==0:
#         print(i)


# 2. Find duplicates in a list
# o Input: [1, 2, 3, 2, 4, 1, 5]
# o Write a program to print all elements that appear more than once.

# x=[1, 2, 3, 2, 4, 1, 5]
# y=[]
# z=[]
# for i in x:
#     if i not in y:
#         y+=[i]
#     else:
#         z+=[i]
# print(z)


# 3. Reverse a list without using built-in methods
# o Input: [5, 10, 15, 20]
# o Use a loop to create a reversed list manually.

# x=[5, 10, 15, 20]
# y=[]
# for i in x:
#     y=[i]+y
# print(y)

# x=[5, 10, 15, 20]
# y=[]
# for i in range(len(x)-1,-1,-1):
#     y+=[x[i]]
# print(y)


# 4. Find common elements between two lists
# o Input: list1 = [1, 2, 3, 4], list2 = [3, 4, 5, 6]
# o Use loops and if-else to find all elements present in both lists.

# x=[1,2,3,4]
# y=[3,4,5,6]
# for i in x:
#     for j in y:
#         if i==j:
#             print(i)


# 5. Replace all negative numbers with zero
# o Input: [4, -3, 7, -1, 0, 5]
# o Write a program using a loop to replace every negative number with 0.

# x=[4, -3, 7, -1, 0, 5]
# y=[]
# for i in x:
#     if i<0:
#         y+=[0]
#     else:
#         y+=[i]
# print(y)


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


