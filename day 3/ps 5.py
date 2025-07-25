# Print only those elements whose index is even.

num=[1,2,3,4,5,6,7,8,9,0]
for i in range(len(num)):
    # print(i)
    if i%2==0:
        print(i,num[i])