# Create a list from user input of 5 numbers.

# method 1:
num=int(input("enter a num:--"))
abc=str(num)
x=[]
for i in abc:
    x.append(i)
print(x)

# method 2:
x=[]
for i in range(1,6):
    a=int(input("enter num:--"))
    x.append(a)
print(x)