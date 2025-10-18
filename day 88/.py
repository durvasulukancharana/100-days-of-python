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




# 3. Replace all vowels in a string with *
# o Input: "Hello World"
# o Write a program to replace all vowels (a, e, i, o, u) with *.
# o Output: "H*ll* W*rld"

# x='hello world'
# y=''
# for i in x:
#     if i in 'aeiou':
#         y+='*'
#     else:
#         y+=i
# print(y)


# 4. Find the most frequent character in a string
# o Input: "programming"
# o Write a program to find the character that occurs most frequently in the string.
# o Output: 'g'

# x='programming'
# y={}
# for i in x:
#     if i not in y:
#         y[i]=1
#     else:
#         y[i]+=1
# print(y)


# 5. Remove duplicate characters from a string
# o Input: "banana"
# o Write a program to remove duplicate characters while keeping the original order.
# o Output: "ban"

# x='banana'
# y=''
# z=''
# for i in x:
#     if i not in y:
#         y+=i
#     else:
#         z+=i
# print(y)


# Substring & Manipulation
# 1. Extract substring between two words
# o Input: "I love Python programming"
# o Extract the substring between "love" and "programming".
# o Output: " Python "




# 2. Count occurrences of each character
# o Input: "hello world"
# o Count how many times each character appears.
# o Output: {'h':1, 'e':1, 'l':3, 'o':2, ' ':1, 'w':1, 'r':1, 'd':1}

# x="hello world"
# y={}
# for i in x:
#     if i not in y:
#         y[i]=1
#     else:
#         y[i]+=1
# print(y)


# 3. Find all indices of a substring
# o Input: "banana", substring = "a"
# o Find all positions where "a" appears.
# o Output: [1, 3, 5]

# x='banana'
# y=[]
# for i in range(len(x)):
#     if x[i]=='a':
#         y.append(i)
# print(y)


# 4. Capitalize first letter of every word
# o Input: "python is easy"
# o Output: "Python Is Easy"

# x='python is easy'
# y=''
# y+=x[0].upper()
# for i in range(1,len(x)):
#     if x[i-1] ==' ':
#         y+=' '+x[i].upper()
#     elif x[i]==' ':
#         pass
#     else:
#         y+=x[i]
# print(y)    


# Palindrome & Reversal
# 1. Check if a string is a palindrome ignoring spaces and case
# o Input: "A man a plan a canal Panama"
# o Output: True

# x="A man a plan a canal Panama"
# z=x.split()
# a=''.join(z)
# print(a)
# y=''
# for i in range(len(x)-1,-1,-1):
#     y+=x[i]
# if x==y:
#     print(True)
# else:
#     print(False)


# x='i','love','my','parents'
# y=' '.join(x)
# print(y)

# x='i','love','my','parents'
# print(' '.join(x))

# x='hi hello how are you'
# y=x.split()
# print(y)
# # z=''.join(y)
# # print(z)
# a='-'.join(y)
# print(a)





# 2. Reverse words in a string
# o Input: "Python is fun"
# o Output: "fun is Python"

# x="Python is fun"
# y=x.split()
# z=''
# for i in range(len(y)-1,-1,-1):
#     z+=y[i]+' '
# print(z)


# 3. Reverse each word in a string but keep word order
# o Input: "Python is fun"
# o Output: "nohtyP si nuf"

# text = "Python is fun"
# words = text.split()
# reversed_words = [word[::-1] for word in words]
# result = " ".join(reversed_words)
# print(result)
