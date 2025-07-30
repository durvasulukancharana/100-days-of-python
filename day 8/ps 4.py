# From ["cat", "dog", "parrot", "cow"], create a tuple of words with more than 3 letters.

abc=["cat", "dog", "parrot", "cow"]
res=tuple(i for i in abc if len(i)>3)
print(res)

abc=["cat", "dog", "parrot", "cow"]
for i in range(len(abc)):
    if len(abc[i])>3:
        print(abc[i])

abc=["cat", "dog", "parrot", "cow"]
for i in abc:
    if len(i)>3:
        print(i)