# Reverse a list without using .reverse().

# method 1:
y=[]
x=[1,2,3,4,5]
for i in range(len(x)-1,-1,-1):
    print(x[i])
    y.append(x[i])
print(y)

# method 2:
x=[1,2,3,4,5]
x.reverse()
print(x)