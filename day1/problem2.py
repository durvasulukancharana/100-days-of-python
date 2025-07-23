# 2.	Generate a tuple containing only even numbers from 50 to 100.

res=tuple(i for i in range(50,101) if i%2==0)
print(res)