# From the string "TupleComprehension", create a tuple containing only the vowels.

name="TupleComprehension"
res=tuple(i for i in name if i in "aeiouAEIOU")
print(res)

name="TupleComprehension"
for i in name:
    if i in "aeiouAEIOU":
        print(i)