# Tuple of numbers between 1 to 20 divisible by both 3 and 5.

res=tuple(i for i in range(1,20) if i%3==0 and i%5==0)
print(res)

for i in range(1,20):
    if i%3==0 and i%5==0:
        print(i)
