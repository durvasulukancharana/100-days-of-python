# 9.	oTuple of product of pairs (i * j) where:
# •	i in [2, 4, 6]
# •	j in [1, 3, 5]

i = [2, 4, 6]
j = [1, 3, 5]
for a in i:
    for b in j:
        print((a*b))

i = [2, 4, 6]
j = [1, 3, 5]
for a,b in zip(i,j):
    print(a*b)

i = [2, 4, 6]
j = [1, 3, 5]
for a in range(len(i)):
    print(i[a]*j[a])