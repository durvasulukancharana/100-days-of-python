
name=input("enter :")
empty=''
for i in range(len(name)-1,-1,-1):
    # print(name[i])
    empty+=name[i]
print(empty)
if name==empty:
    print("pali")
else:
    print("no")

name=input("enter :")
empty=''
for i in name:
    empty=i+empty
print(empty)
if name==empty:
    print("palindrome")
else:
    print("not a palindrome")