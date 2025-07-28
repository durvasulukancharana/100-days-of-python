# Use .remove() to remove first occurrence of 3.

abc=[1,2,3,4,5]
abc.remove(3)
print(abc)

for i in range(0,3):
    for a in range(0,1):
        abc.remove(abc[a])
print(abc)