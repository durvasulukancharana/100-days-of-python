# Write a program to check if a number is a neon number (e.g., 9 → 9²=81 → 8+1=9).

x=int(input('enter a num : '))
z=x*x
y=0
for i in str(z):
    y+=int(i)
print(y)
if y==x:
    print('neon')
else:
    print('not')


# Find the sum of squares of digits of a number.

x=int(input('enter a num :'))
y=0
for i in str(x):
    y+=int(i)**2
print(y)


# Print all prime numbers between 1 and 200.

def check(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
for i in range(1,200):
    if check(i):
        print(i)


# 🔹 Loops & Patterns

# Print this pattern:

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()


# Write a program to calculate the factorial of a number using recursion.

x=int(input('enter a num : '))
y=1
for i in range(1,x+1):
    y*=i
print(y)


# Print the first n triangular numbers (1, 3, 6, 10, …).

# Print first n triangular numbers

n = int(input("Enter how many triangular numbers: "))
for i in range(1, n + 1):
    triangular = i * (i + 1) // 2
    print(triangular, end=" ")



# 🔹 Strings

# Write a program to reverse each word in a sentence (not the sentence itself).

x='hello every one'
y=''
for i in x:
    y=i+y
print(y)

x='hello every one'
y=''
z=x.split()
for i in z:
    y=i+' '+y
print(y)


# Count the number of uppercase, lowercase, digits, and spaces in a string.

x='Heyy EvErY OnE !@#$ hOW ArE yoU 143'
upper=0
lower=0
digit=0
space=0
special=0
for i in x:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    elif i.isdigit():
        digit+=1
    elif i.isspace():
        space+=1
    else:
        special+=1
print(lower,upper,digit,space,special)


# 🔹 Lists & Tuples

# Write a program to rotate a list to the right by k positions.

x=[1,2,3,4,5]
k=2
z=x[-k:]+x[0:-k]
print(z)


# 🔹 Dictionaries, Sets & Functions

# Create a dictionary of countries and capitals, then allow the user to search for a capital by country name.

x={
    'india':'new_elhi',
    'nepal':'bhutan',
    'srilanka':'colombo',
    'bangladesh':'dhaka'
}
country = input("Enter country name: ")
if country in x:
    print(country,x[country])
else:
    print('there is no data')

x={'name':'vamsi','age':28,'village':'ongole'}
y={value:key for key,value in x.items()}
print(y)

x={'name':'vamsi','age':28,'village':'ongole'}
y={}
for i,j in x.items():
    y[j]=i
print(y)


# Write a function to find the common elements across three sets.

def set(a,b,c):
    return a & b & c
x={1,2,3}
y={3,2,1}
z={1,2,4}
n=set(x,y,z)
print(n)

# Write a function that takes a list of numbers and returns a dictionary with even and odd numbers separated.

x=[1,2,3,4,5,6]
y={'even':[],'odd':[]}
for i in x :
    if i%2==0:
        y['even'].append(i)
    else:
        y['odd'].append(i)
print(y)

