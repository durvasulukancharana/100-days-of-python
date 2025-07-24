# Count how many times 0 appears in [1, 0, 2, 0, 3, 0].

a=[1, 0, 2, 0, 3, 0]
count=0
for i in a:
    if i==0:
        count+=1
print(count)