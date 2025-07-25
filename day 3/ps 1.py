# Print all odd numbers from a list.

# method 1:
a=[1,2,3,4,5,6,7,8,9]
for i in a:
    if i%2!=0:
        print(i)

# method 2:
for i in range(1,10,2):
    print(i)

# method 3:
a=[1,2,3,4,5,6,7,8,9]
b=a[0:10:2]
print(b)