# r=[1,2,3,4,] p=[10,20,30,40] output=[11,12,13,14]

r=[1,2,3,4,]
p=[10,20,30,40]
res=tuple(i+p[0] for i in r)
print(res)

r=[1,2,3,4,]
p=[10,20,30,40]
for i in r:
    print(i+10)

r=[1,2,3,4,]
p=[10,20,30,40]
for i in r:
    print(i+p[0])