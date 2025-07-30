# Extract vowels from the string "comprehension" into a tuple.

name="comprehension"
res=tuple(i for i in name if i in "aeiouAEIOU")
print(res)