# Create a tuple of squares of numbers from 1 to 15 using comprehension.

res=tuple(i**2 for i in range(1,15))
print(res)

for i in range(1,15):
    print(i**2)