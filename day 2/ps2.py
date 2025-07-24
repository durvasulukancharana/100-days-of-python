# Print the last 3 elements of a list.

# method 1:
list=[1,2,3,4,5,6,7]
b=list[-1:-4:-1]
print(b)

# method 2:
list=[1,2,3,4,5,6,7]
for i in range(-1,-4,-1):
    print(list[i])