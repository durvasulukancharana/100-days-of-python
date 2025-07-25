# Find the average of numbers in a list.

# method 1:
num=[20,30,40]
sum=0
avg=0
for i in num:
    sum+=i
    avg=sum//(len(num))
print(sum)
print(avg)