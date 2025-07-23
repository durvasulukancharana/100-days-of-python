# 8.	words = ["level", "python", "madam", "world", "racecar"] print palindrome words  

words = ["level", "python", "madam", "world", "racecar"]
res=[i for i in words if i[::-1]==i]
print(res)

words = ["level", "python", "madam", "world", "racecar"]
res=["plindrome" if i[::-1]==i else "not a palindrome" for i in words]
print(res)
