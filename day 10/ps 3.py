# 3.Count the number of vowels in a string.

name=input("enter a name:-")
vowels="aeiouAEIOU"
count=0
for i in name:
    if i in vowels:
        count+=1
print(count)