# Replace all negative numbers in a list with 0.

num=[1,2,3,4,-1,-2,-3,-4]
y=[]
for i in num:
    if i<=0:
        y.append(0)
    else:
        y.append(i)
print(y)