# Create a tuple of (number, square) pairs for numbers from 5 to 10.

res=tuple((i,i**2)for i in range(5,10))
print(res)

for i in range(1,10):
    print(i,i**2)