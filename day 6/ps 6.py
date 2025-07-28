# Sort a list in descending order.

# method 1:
abc=[1,3,5,7,9,2,4,6,8]
abc.sort()
print(abc)

# method 2:
abc=[1,3,5,7,9,2,4,6,8]
x=abc[0]
y=[]
for i in range(0,len(abc)):
    for j in range (i+1,len(abc)):
        if abc[i]>abc[j]:
            abc[i],abc[j]=abc[j],abc[i]
        else:
            abc[i],abc[j]=abc[i],abc[j]
print(abc)