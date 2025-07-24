# Find the max and min number in a list.

# method 1:
a=[1,2,3,4,5]
min_num=float("inf")
for i in a:
    if i<=min_num:
        min_num=i
print(min_num)

max_num=-float("inf")
for i in a:
    if i>=min_num:
        max_num=i
print(max_num)

# method 2:
a=[1,2,3,4,5]
min=[]
max=[]
b=a[0]
for i in a:
    if i>=b:
        b=i
max.append(b)
print(max)
for i in a:
    if i<=b:
        b=i
min.append(b)
print(min)

# method 3:
a=[1,2,3,4,5]
max=a[0]
min=a[0]
for i in range(0,len(a)):
    if a[i]>=max:
        max=a[i]
print(max)
for i in range(0,len(a)):
    if a[i]<=min:
        min=a[i]
print(min)