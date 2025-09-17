
# 1.Solid Square Pattern
# Problem: Print a solid square of stars of size n.
# Input: n = 4
# Output:
# * * * *
# * * * *
# * * * *
# * * * *

x=4
for i in range(1,5):
    print('* '*x)


# 2.Solid Rectangle Pattern
# Problem: Print a solid rectangle of m rows and n columns.
# Input: m = 3, n = 5
# Output:
# * * * * *
# * * * * *
# * * * * *

for i in range(1,4):
    print('* '*5)


# 3.Right-Angled Triangle (Left-Aligned)
# Problem: Print a left-aligned right-angled triangle.
# Input: n = 5
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1,6):
    for j in range(1,i+1):
        print('* ',end='')
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print('* ',end='')
    print()


# 4.Right-Angled Triangle (Right-Aligned)
# Input: n = 5
# Output:
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

x=5
for i in range(1,x+1):
    print(' '*(x-i)+'*'*i)
    
for i in range(1,6):
    for j in range(1,i+1):
        print(' '*(i-j)+'*'*j)


# 5.Inverted Triangle (Left-Aligned)
# Input: n = 5
# Output:
# * * * * *
# * * * *
# * * *
# * *
# *

x=6
for i in range(1,x):
    print('* '*(x-i))


# 6.Inverted Triangle (Right-Aligned)
# Input: n = 5
# Output:
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

x=6
for i in range(1,x+1):
    print(' '*i+'*'*(x-i))


# 7.Centered Pyramid Pattern
# Input: n = 4
# Output:
#       *
#     * * *
#   * * * * *
# * * * * * * *

x=6
for i in range(1,x):
    print(' '*(x-i)+'* '*i)


# 8.Diamond Pattern
# Input: n = 3
# Output:
#     *
#   * * *
# * * * * *
#   * * *
#     *

x=4
for i in range(1,x):
    print(' '*(x-i)+'*  '*i)
x=4
for i in range(1,x):
    print(' '*(i)+'* '*(x-i))


# 26.Increasing Number Triangle
# Problem: Print numbers from 1 to n in triangle form.
# Input: n = 5
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()


# 27.Repeating Row Number Triangle
# Input: n = 5
# Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for i in range (1,6):
    for j in range(1,i+1):
        print(i,end=' ')
    print()


# 28.Continuous Number Triangle
# Input: n = 4
# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10

x=1
for i in range(1,5):
    for j in range(1,i+1):
        print(x,end=' ')
        x+=1
    print()


# 29.Reverse Row Number Triangle
# Input: n = 5
# Output:
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

x=1
for i in range(1,6):
    y=x
    for j in range(1,i+1):
        print(y,end=' ')
        y-=1
    x+=1
    print()


# 30.Inverted Number Triangle
# Input: n = 5
# Output:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

for i in range(5,0,-1):
    x=5
    for j in range(1,i+1):
        print(x,end=' ')
        x-=1
    print()