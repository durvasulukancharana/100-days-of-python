# random.choice module:-
import random
print(random.choice('python'))

import random
i='helloworld'
for a in range(10):
    print(random.choice(i))

# creating a password using random.choice by user input:--
import random
a="abcdefg"
b='123456789'
c='~!@#$%^&'

password=''
 
x=int(input("enter alphabet num:-"))
y=int(input("enter digit num:-"))
z=int(input("enter special char num:-"))

for i in range(x):
    data=random.choice(a)
    password+=data

for j in range(y):
    data=random.choice(b)
    password+=data

for k in range(z):
    data=random.choice(c)
    password+=data
print(password)