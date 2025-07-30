# Tuple of ASCII values of characters in "Python".

name="Python"
res=tuple(ord(i) for i in name)
print(res)

name="Python"
for i in name:
    print(ord(i))