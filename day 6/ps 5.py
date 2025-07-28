# Use .count() to count how many times 1 appears.

# method 1:
abc=[1,1,1,1,2,3,4,1]
count=0
for i in abc:
    if i==1:
        count+=1
print(count)

# method 2:
abc=[1,1,1,1,2,3,4,1]
a=abc.count(1)
print(a)