# String and Text Manipulation – Interview Questions

# 1. Remove Spaces from Given Text
# Problem: Write a function to remove all spaces from the input string. Explanation: Remove any whitespace characters. Input: "he llo wor ld" Output: "helloworld"

x="he llo wor ld"
y=''
for i in x:
    if i.isspace():
        continue
    else:
        y+=i
print(y)


x="he llo wor ld"
y=''
for i in x:
    if i!=' ':
        y+=i
print(y)

# 3. Reverse a String After Removing Spaces
# Problem: Write a function to reverse a string after removing all spaces. Input: "he llo world" Output: "dlrowolleh"

x="he llo world"
y=''
for i in x:
    if i==' ':
        continue
    else:
        y=i+y
print(y)


# 4. Convert Snake Case to Camel Case
# Problem: Convert a string from snake_case to camelCase. Input: "my_variable_name" Output: "myVariableName"

x="my_variable_name"
y=''
for i in range(len(x)):
    if x[i-1]=='_':
        y+=x[i].upper()
    elif x[i]=='_':
        pass
    else:
        y+=x[i]
print(y)


# 5. Convert Snake Case to Pascal Case
# Problem: Convert a string from snake_case to PascalCase. Input: "my_variable_name" Output: "MyVariableName"

x="my_variable_name"
y=''
for i in range(len(x)):
    if x[i-1]=='_':
        y+=x[i].upper()
    elif x[i]=='_':
        continue
    else:
        y+=x[i]
print(y)

x="my_variable_name"
y=''
z=x.split('_')
for i in z:
    y+=i.capitalize()
print(y)

# 6. Convert Camel Case to Snake Case
# Problem: Convert a string from camelCase to snake_case. Input: "myVariableName" Output: "my_variable_name"

x="myVariableName"
y=''
for i in x:
    if i.isupper():
        y+='_'+i.lower()
    else:
        y+=i
print(y)

x="myVariableName"
y=''
for i in range(len(x)):
    if x[i].isupper():
        y+='_'+x[i].lower()
    else:
        y+=x[i]
print(y)


# 7. Convert Camel Case to Pascal Case
# Problem: Convert a string from camelCase to PascalCase. Input: "myVariable" Output: "MyVariable"

x="myVariable"
y=''
for i in range(len(x)):
    if i==0:
        y+=x[i].upper()
    else:
        y+=x[i]
print(y)

x="myVariable"
y=''
y+=x[0].upper()
for i in range(1,len(x)):
    y+=x[i]
print(y)


# 8. Convert Pascal Case to Camel Case
# Problem: Convert a string from PascalCase to camelCase. Input: "MyVariable" Output: "myVariable"

x="MyVariable"
y=''
for i in range(len(x)):
    if i==0:
        y+=x[i].lower()
    else:
        y+=x[i]
print(y)

x="MyVariable"
y=''
y+=x[0].lower()
for i in range(1,len(x)):
    y+=x[i]
print(y)


# 9. Convert Pascal Case to Snake Case
# Problem: Convert a string from PascalCase to snake_case. Input: "MyVariable" Output: "my_variable"

x="MyVariable"
y=''
z=''
for i in range(len(x)):
    if i==0:
        y+=x[i].lower()
    else:
        y+=x[i]
for i in range(len(y)):
    if x[i].isupper():
        z+='_'+x[i].lower()
    else:
        z+=x[i]
print(z)

x="MyVariable"
y=''
y+=x[0].lower()
for i in range(1,len(x)):
    if x[i].isupper():
        y+='_'+x[i].lower()
    else:
        y+=x[i]
print(y)


# 10. Convert Text to Camel Case
# Problem: Convert a space-separated sentence into camelCase. Input: "hello world example" Output: "helloWorldExample"

x="hello world example"
y=''
for i in range(len(x)):
    if x[i-1]==' ':
        y+=x[i].upper()
    elif x[i]==' ':
        continue
    else:
        y+=x[i]
print(y)


# 11. Convert Text to Snake Case
# Problem: Convert a space-separated sentence into snake_case. Input: "hello world example" Output: "hello_world_example"

x="hello world example"
y=''
for i in x:
    if i==' ':
        y+='_'
    else:
        y+=i
print(y)

x="hello world example"
y=''
for i in range(len(x)):
    if x[i]==' ':
        y+='_'
    else:
        y+=x[i]
print(y)


# 12. Convert Text to Pascal Case
# Problem: Convert a space-separated sentence into PascalCase. Input: "hello world example" Output: "HelloWorldExample"

x="hello world example"
y=''
z=x.split(' ')
for i in z:
    y+=i.capitalize()
print(y)

x="hello world example"
y=''
y+=x[0].upper()
for i in range(1,len(x)):
    if x[i-1]==' ':
        y+=x[i].upper()
    elif x[i]==' ':
        continue
    else:
        y+=x[i]
print(y)


# 13. Swap Upper and Lower Case
# Problem: Swap the case of each letter in a given string. Input: "HeLLo" Output: "hEllO"

x="HeLLo"
y=''
for i in x:
    if i.isupper():
        y+=i.lower()
    else:
        y+=i.upper()
print(y)


# 14. Separate Digits from Text
# Problem: Extract all digits from a given alphanumeric string. Input: "abc123d4" Output: "1234"

x="abc123d4"
y=''
for i in x:
    if i.isdigit():
        y+=i
print(y)


# 15. Print Uppercase, Lowercase, Digits, and Special Characters Separately
# Problem: Print each type of character separately from the string. Input: "Abc123!@#" Output:
# Uppercase: A
# Lowercase: b c
# Digits: 1 2 3
# Special Characters: ! @ #

x="Abc123!@#"
a=''
b=''
c=''
d=''
for i in x:
    if i.isupper():
        a+=i
    elif i.islower():
        b+=i
    elif i.isdigit():
        c+=i
    else:
        d+=i
print(a,b,c,d)

# 16. Count of Uppercase, Lowercase, Digits, and Special Characters
# Problem: Count each type of character in a string. Input: "AbC@123x!" Output:
# Uppercase: 2
# Lowercase: 1
# Digits: 3
# Special Characters: 2

x="Abc123!@#"
a=0
b=0
c=0
d=0
for i in x:
    if i.isupper():
        a+=1
    elif i.islower():
        b+=1
    elif i.isdigit():
        c+=1
    else:
        d+=1
print(a,b,c,d)

# 17. Check Password Strength
# Problem: Check if a password contains at least one uppercase, one lowercase, one digit, and one special character. Input: "Pass123!" Output: "Strong Password"
# 
x=(input('enter a num :'))
y=0
for i in x:
    if i.isupper():
        y+=1
    elif i.islower():
        y+=1
    elif i.isdigit():
        y+=1
    else:
        y+=1
if y>=4:
    print('strong passwprd')
else:
    print('not strong')

# 18. Remove Duplicates in a Given Input
# Problem: Remove duplicate characters from a string. Input: "aabbcc" Output: "abc"

x="aabbcc"
y=''
for i in x:
    if i not in y:
        y+=i
print(y)


# 19. Print Duplicates in a Given String
# Problem: Identify and print duplicate characters in a string. Input: "aabbccde" Output: a b c

x="aabbccde"
y=''
z=''
for i in x:
    if i not in y:
        y+=i
    else:
        z+=i
print(z)


# 20. Print Next Characters in a Given String
# Problem: Replace each character in the string with its next character. Input: "abc" Output: "bcd"

x=input('enter a char : ')
y=''
for i in x:
    y+=chr(ord(i)+1)
print(y)

print(chr(ord('A')+1))
print((chr(65)))

