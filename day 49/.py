# Write a program to take your name as input and print "Hello, <name>!".

x='virat'
print('hello,virat')

# Take two numbers as input and print their sum, difference, product, and division.

a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(b%a)

# Write a program to swap two numbers (without using a third variable).

a=20
b=30
a,b=b,a
print(a,b)

# 🔹 Conditions

# Write a program to check if a number is even or odd.

x=27
if x%2==0:
    print('even')
else:
    print('not')

# Take a number as input and check if it is positive, negative, or zero.

x=int(input('enter a num:'))
if x>0:
    print('+ve')
elif x<0:
    print('-ve')
else:
    print('zero')

# Write a program to find the largest of three numbers.

x=(1,2,3)
max=-float('inf')
for i in x:
    if i>max:
        max=i
print(max)

# 🔹 Loops

# Print numbers from 1 to 10 using a loop.

for i in range(1,11):
    print(i,end=' ')

# Print the multiplication table of 5.

for i in range(5,6):
    for j in range(1,11):
        print(i,'x',j,'=',i*j)
    print()

x=5
for i in range(1,11):
    print(x,i,x*i)

# Write a program to calculate the sum of the first 10 natural numbers.

sum=0
for i in range(1,11):
    sum+=i
print(sum)

# 🔹 Strings

# Take a string as input and print it in reverse.

x='vamsi'
y=''
for i in x:
    y=i+y
print(y)

x='vamsi'
for i in range(len(x)-1,-1,-1):
    print(x[i])

# Count the number of vowels in a string.
count=0
x='vamsi'
for i in x:
    if i in 'aeiou':
        count+=1
print(count)

# Check if a string is a palindrome (same forward and backward).

x='vamsi'
y=''
for i in range(len(x)-1,-1,-1):
    y+=x[i]
if y==x:
    print('palindrome')
else:
    print('not')

# 🔹 Lists & Dictionaries

# Write a program to find the largest element in a list.

x=['apple','banana','ball']
max=-float('inf')
for i in range(len(x)):
    if i>max:
        max=i
print(max)

# Write a program to remove duplicates from a list.

x=[1,2,1]
y=[]
for i in x:
    if i not in y:
        y.append(i)
print(y)

# Create a dictionary with 3 students’ names as keys and their marks as values, then print the student with the highest marks.

max=-float('inf')
max=-float('inf')
x={
    'vamsi':50,
    'ajay':90,
    'kumar':55
}
for i,j in x.items():
    if j>max:
        max=j
# print(max)
for i,j in x.items():
    if j==max:
        print(i,j)

max=-float('inf')
x={
    'a':'vamsi',
    'b':'ajay',
    'c':'kumar',
    'd':'ganesh'
}
for i,j in x.items():
    if len(j)>max:
        max=len(j)
print(max)
for i,j in x.items():
    if len(j)==max:
        print(i,j)


