# Extend a list with another list of values.

# meyhod 1:
abc=[1,2,3,4,5]
xyz=[6,7,8,9,0]
xxx=abc+xyz
print(xxx)

# method 2:
abc=[1,2,3,4,5]
xyz=[6,7,8,9,0]
abc.extend(xyz)
print(abc)