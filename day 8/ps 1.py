# Tuple of cube of odd numbers from 1 to 15.

res=tuple(i**3 for i in range(1,15) if i%2!=0)
print(res)

for i in range(1,15):
    if i%2!=0:
        print(i**3)