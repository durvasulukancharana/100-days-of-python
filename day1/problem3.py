# 3.	 From a list of names, create a tuple of names that start with the letter 'A' or 'a' 

res=["arjun","aravind","rajamouli","atlee"]	
tupl=[]
for i in res:
    if i[0]=='a':
        tupl.append(i)
print(tuple(tupl))

names=["arjun","aravind","rajamouli","Atlee"]
res=tuple(i for i in names if i[0]=='a' or i[0]=='A')
print(res)
