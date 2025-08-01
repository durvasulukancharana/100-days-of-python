# 5.Remove all ($)  punctuation from a string.

name="vamsi$enduri$"
# new=''
for i in name:
    if i.isalpha():
        print(i,end='')