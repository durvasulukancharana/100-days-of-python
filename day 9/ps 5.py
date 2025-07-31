# Given a string "Python", create a tuple of ASCII values for each character.

res=tuple(ord(i) for i in "python")
print(res)

for i in "python":
    print(ord(i))