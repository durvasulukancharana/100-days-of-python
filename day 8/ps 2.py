# Find factors of 10 number using tuple comprehension? 

res=tuple(i for i in range(1,11) if 10%i==0)
print(res)

a=10
for i in range(1,a):
    if a%i==0:
        print(i)