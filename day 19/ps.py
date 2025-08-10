'''2nd highest'''
num=[1,2,9,1,4,1,9,5,6,7,8,6,5]
first=0
second=0
for i in num:
    if i>first:
        secon=first
        first=i
    elif first>i and second<i:
        second=i
print(second)


'''anagram'''
name1='listen'
name2='silent'
x=list(sorted(name1))
y=list(sorted(name2))
if x==y:
    print("yes it is anagram")
else:
    print("no it is not a anagram")


name1=input('enter a name :-')
name2=input('enter a name :-')
x=list(sorted(name1))
y=list(sorted(name2))
if x==y:
    print("yes it is anagram")
else:
    print("no it is not a anagram")


'''ascending'''
num=[1,3,5,8,5,4,9]
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]<num[j]:
            num[i],num[j]= num[i],num[j]
        else:
            num[i],num[j]= num[j],num[i]
print(num)


num=[2,4,1,5,6,9,3,2]
num.sort()
print(num)


'''fibonacci'''
a=0
b=1
a,b=b,a+b
print(a,b)


num=int(input('enter a num :-'))
a=0
b=1
for i in range(num):
    a,b=b,a+b
    print(a)


'''nonrepeating'''
x=[1,2,3,4,5,1,2,3,4,6,7,8]
y=[]
z=[]
for i in x:
    if i not in y:
        y.append(i)
    else:
        z.append(i)
for i in y:
    if i not in (z):
        print(i)