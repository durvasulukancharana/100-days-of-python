# Check if 15 is in the list [10, 20, 15, 30].

# method 1:
a=[10, 20, 15, 30]
for i in a:
    if i==15:
        print("yes 15 is there.")
    else:
        ("no")

# method 2:
a=[10, 20, 15, 30]   
for i in range(0,len(a)):
    if a[i]==15:
        # print(i) 
        # print(a[i])
        print("yess") 
    else:
        print("noo")   

# method 3:
a=[10, 20, 15, 30]
if 15 in a:
    print("True")
else:
    print("no")