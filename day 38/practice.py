# Write a program to find the HCF (GCD) of three numbers.

x=30
y=15
for i in x,y:
    if x%i==0 and y%i==0:
        print(i)


# Check if a number is a strong number (e.g., 145 → 1!+4!+5! = 145).

x=int(input('enter a num :'))
y=0
for i in str(x):
    y+=int(i)**3
if x==y:
    print('armstrong')
else:
    print('not a armstrong')

# 🔹 Loops & Patterns

# Print the following number triangle:

# 1
# 2 2
# 3 3 3
# 4 4 4 4

for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=' ')
    print()

# Print all prime numbers between 50 and 100.

for i in range(50,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)


# Write a program to find the sum of digits of all numbers from 1 to n.

x=int(input('enter a num :'))
y=0
for i in range(x+1):
    y+=i
print(y)


# 🔹 Strings

# Write a program to check whether a string is a pangram (contains all alphabets a–z).

x='qwertyuiopasdfghjklzxcvbnm'
y='the quick brown fox jumps over the lazy dog'
if x in y:
    print('yes')
else:
    print('no')


# Write a program to remove all vowels from a string.

x='vamsi'
y=''
for i in x:
    if i not in 'aeiou':
        y+=i
print(y)

# Find the most frequent character in a string.

x='durvasulu'
y={}
for i in x:
    if i not in y:
        y[i]=1
    else:
        y[i]+=1
print(y)


# 🔹 Lists & Tuples

# Write a program to find duplicate elements in a list.

x=[1,2,3,4,5,4,3,2]
y=[]
for i in x:
    if i not in y:
        y.append(i)
print(y)


# Write a program to find the sum of all elements in a 2D list.

a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
total = 0
for x in a:
    for j in x:
        total+=j
print(total)



# 🔹 Dictionaries, Sets & Functions

# Create a dictionary with numbers from 1–5 as keys and their squares as values.

x={}
for i in range(1,6):
    x[i]=i**2
print(x)


# Write a function to check if two sets are disjoint.

x={1,2,3,4,5}
y={6,7,8,9,0}
if x.isdisjoint(y):
    print('yes')
else:
    print('noo')


# Write a function to count how many unique words are in a given sentence.

x='this is a test this is only test'
y=x.lower().split()
z=set(y)
print(len(z))