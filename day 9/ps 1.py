# From a list of names, create a tuple of names that start with the letter 'A' or 'a'

names=["Atlee","arjun","anil"]
res=tuple(i for i in names if i.startswith ('a') or ('A'))
print(res)

names=["Atlee","arjun","anil"]
for i in names:
    if i.startswith ('a') or ('A'):
        print(i)