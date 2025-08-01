# 4.Replace every vowel in a string with '@'.

name=input("enter a name:-")
vowels='aeiouAEIOU'
rev=''
for i in name:
    if i in vowels:
        rev+='@'
    else:
        rev+=i
print(rev)