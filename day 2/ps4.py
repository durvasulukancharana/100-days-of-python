# Delete the second and third items in a list.
# method 1:
a=[1,2,3,4,5,6,7,8]
a.pop(1) and a.pop(2)
print(a)

# method 2:
a=[1,2,3,4,5,6,7,8]
for i in range(0,len(a)):
    if i==1:
        a.pop()
    else:
        i==2
        a.pop()
print(a)