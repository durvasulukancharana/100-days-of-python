# 10.	 From ["cat", "dog", "parrot", "cow"], create a tuple of words with more than 3 letters

a=["cat", "dog", "parrot", "cow"]
# new=[]
for i in range (0,len(a)):
    if len(a[i])>3:
        print(a[i])

a=["cat", "dog", "parrot", "cow"]
for i in a:
    if len(i)>3:
        print(i)