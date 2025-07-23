# 7.	 Given a string "Python", create a tuple of ASCII values for each character.
# Input b=[[1, 2], [3, 4], [5, 6]]     out put=[1,2,3,4,5,6]
# r=[1,2,3,4,] p=[10,20,30,40]   output=[11,12,13,14]

name="Python"
for i in name:
    if i.isupper() or i.islower():
        print(ord(i),i)

res=tuple(ord(i) for i in 'Python' if i.islower or i.isupper)
print(res)

b=[[1, 2], [3, 4], [5, 6]]
out_put=[]
for i in b:
    out_put+=i
print(out_put)

r=[1,2,3,4,]
p=[10,20,30,40]
for i in r :
    for j in range(10,11):
        print(i+j)

r=[1,2,3,4,]
p=[10,20,30,40]
res=tuple(i+j for i,j in zip(r,p))
print(res)