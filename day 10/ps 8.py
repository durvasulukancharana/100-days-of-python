# 8.Count the frequency of each character in a string.

name='pythonpython'
new={}
for i in name:
    if i not in new:
        new[i]=1
    else:
        new[i]+=1
print(new)