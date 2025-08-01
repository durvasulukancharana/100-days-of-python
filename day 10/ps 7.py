# 7.Find the first non-repeating character in a string.

name='abcdefabcdefg'
new=''
new1=''
for i in name:
    if i not in new:
        new+=i
    else:
        new1+=i
print(new)
print(new1)
for j in new:
    if j not in new1:
        print(j)