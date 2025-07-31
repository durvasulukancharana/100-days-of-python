# words = ["level", "python", "madam", "world", "racecar"] print palindrome words 

words = ["level", "python", "madam", "world", "racecar"]
rev=''
for i in words:
    if i==i[::-1]:
        print(i)