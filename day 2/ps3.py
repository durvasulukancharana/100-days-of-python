# Replace the middle element in a list with the number 100.

# method 1:
list=[1,2,3,4,5,6,7,8,9]
list[4]=100
print(list)
print(len(list))

# method 2:
list=[1,2,3,4,5,6,7,8,9]
print(len(list))
if len(list)%2!=0:
    list[len(list)//2]=100
else:
    list[len(list)//2]=100
print(list)

# method 3:
list=[1,2,3,4,5,6,7,8,9]
print(len(list))
if len(list)%2!=0:
    list[len(list)//2]=100
else:
    list[len(list)//2-1]=100
print(list)