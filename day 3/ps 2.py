# Print each index and value using a loop.

# method 1:
x=[1,2,3,4,5,6]
for i in range(0,len(x)):
    print(x[i],i)

# method 2:
y=[]
z=[]
x=[1,2,3,4,5,6]
for i in range(0,len(x)):
    z.append(x[i])
    y.append(i)
print(z)
print(y)

# method 3:
y=''
z=''
x=[1,2,3,4,5,6]
for i in range(0,len(x)):
    z+=str(x[i])
    y+=str(i)
print(z)
print(y)