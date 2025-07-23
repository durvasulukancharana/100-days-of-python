# 4.	Generate a tuple of prime numbers between 10 to 50 using comprehension.

num=int(input("enter a num"))
new=[]
for i in num:
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        new.append("prime")
    else:
        new.append("not a prime")
print(new)


for i in range(10,51):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i)