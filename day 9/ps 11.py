# 6) From ["cat", "dog", "parrot", "cow"], create a tuple of words with more than 3 letters.

name=["cat", "dog", "parrot", "cow"]
new=[]
for i in name:
    if len(i)>3:
        new.append(i)
news=tuple(new)
print(news)