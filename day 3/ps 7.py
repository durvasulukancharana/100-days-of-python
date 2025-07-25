# Create a new list of only positive numbers.

num=[1,2,3,4-1,-2,-3,5]
new_list=[]
for i in num:
    if i>=0:
        new_list.append(i)
    else:
        print('noo')
print(new_list)