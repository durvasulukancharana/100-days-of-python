# 2.Check if a string is a palindrome.

name=input("enter a name:-")
new=''
for i in range(len(name)-1,-1,-1):
    new+=(name[i])
print(new)
if name==new:
    print("palinrome")
else:
    print("not a palindrome")