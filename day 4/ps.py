# ***____lamba functions____***

res =lambda a,b:a+b
s=res
print(s(10,20))

a=lambda a,b,c:a*b+c
x=a
print(x(12,10,10))

# ___filter___

a=[1,2,3,4,5,6,7,8,9]
res=list(filter(lambda x:x%2==0 ,a))
a=res
print(a)

b=(1,2,3,4,5,6,7)
x=tuple(filter(lambda i:i%2!=0,b))
print(x)

# ___map___

# __list method :--__

x=[1,2,3,4,5,6,7,8,9]
a=list(map(lambda i:i*2,x))
print(a)

y=[1,2,3,4,5,6,7,8,9]
i=list(filter(lambda x:x%2==0,y))
print(i)
i2=list(map(lambda x:x+1,i))
print(i2)

z=[1,2,3,4,5,6,7,8,9]
res=list(filter(lambda i:i%2!=0,z))
print(res)
res2=list(map(lambda i:i+1,res))
print(res2)

# __tuple method:--__

y=[1,2,3,4,5,6,7,8,9]
i=tuple(filter(lambda x:x%2==0,y))
print(i)
i2=tuple(map(lambda x:x+1,i))
print(i2)

z=[1,2,3,4,5,6,7,8,9]
res=tuple(filter(lambda i:i%2!=0,z))
print(res)
res2=tuple(map(lambda i:i+1,res))
print(res2)

# ___reduce___

from functools import reduce
num=[1,2,3,4,5,6]
total=reduce(lambda x,y:x+y,num)
print(total)

from functools import reduce
num=[1,2,3,4,5,6]
total=reduce(lambda x,y:x-y,num)
print(total)

# __tuple method:--__

from functools import reduce
num=[1,2,3,4,5,6,7,8,9]
res1=tuple(filter(lambda x:x%2==0,num))
print(res1)
res2=tuple(map(lambda x:x+1,res1))
print(res2)
res3=reduce(lambda x,y:x+y,res2)
print(res3)

from functools import reduce
num=[1,2,3,4,5,6,7,8,9]
res1=tuple(filter(lambda x:x%2!=0,num))
print(res1)
res2=tuple(map(lambda x:x+1,res1))
print(res2)
res3=reduce(lambda x,y:x+y,res2)
print(res3)


# __ list method:-- __

from functools import reduce
num=[1,2,3,4,5,6,7,8,9]
res1=list(filter(lambda x:x%2==0,num))
print(res1)
res2=list(map(lambda x:x+1,res1))
print(res2)
res3=reduce(lambda x,y:x+y,res2)
print(res3)

from functools import reduce
num=[1,2,3,4,5,6,7,8,9]
res1=list(filter(lambda x:x%2!=0,num))
print(res1)
res2=list(map(lambda x:x+1,res1))
print(res2)
res3=reduce(lambda x,y:x+y,res2)
print(res3)

res="Python Developer"
new=""
for i in res:
    if i.isupper():
        new+='_'+i
    else:
        new+=i
print(new)

res="_Python _Developer"
new=''
for i in res:
    if i!='_':
        new+=i
print(new)