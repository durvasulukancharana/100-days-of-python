# 6.Check if two strings are anagrams.

a='dog'
b='god'
c=list(a)
d=list(b)
for i in c:
    if i in d and len(c)==len(d):
        print("anagram")

a='dog'
b='god'
c=list(a)
d=list(b)
c=sorted(c)
d=sorted(d)
print(c==d)

a='dog'
b='god'
c=list(sorted(a))
d=list(sorted(b))
print(c==d,'anagram')