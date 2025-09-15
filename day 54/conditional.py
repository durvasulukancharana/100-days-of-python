# Interview-Style Questions Based on Conditional Statements

# 1. Check Even or Odd
# Question: Determine whether a number is even or odd. Explanation: A number is even if it is divisible by 2. Otherwise, it’s odd. - Input: Number = 6 - Output: Even number

num=int(input('enter a num :'))
if num%2==0:
    print('even number')
else:
    print('odd number')


# 2. Divisible by 5 but Not by 10
# Question: Check if a number is divisible by 5 but not by 10. Explanation: Use modulo (%) to check if the number % 5 == 0 and number % 10 != 0. - Input: Number = 25 - Output: Satisfy

num=int(input('enter a num :'))
if num%5==0 and num%10 !=0:
    print('satisfy')
else:
    print('not satisfy')


# 3. Biggest Among Two Numbers
# Question: Find the biggest number among two. Explanation: Use comparison operators (>) to check which number is greater. - Input: A = 4, B = 7 - Output: Biggest is: 7

a,b=3,6
if a>b:
    print(a)
else:
    print(b)


# 4. Smallest Among Two Numbers
# Question: Find the smallest number among two. Explanation: Use comparison operators (<) to find the smaller value. - Input: A = 4, B = 7 - Output: Smallest is: 4

a,b=4,7
if a<b:
    print(a)
else:
    print(b)


# 5. Divisible by 2, 3, and 6
# Question: Check if a number is divisible by 2, 3, and 6. Explanation: If a number is divisible by both 2 and 3, it is also divisible by 6. - Input: Number = 18 - Output: Satisfy

x=int(input('enter a num:'))
if x%2==0 and x%3==0 and x%6==0:
    print('satisfy')
else:
    print('not satisfy')


# 6. Voting Eligibility
# Question: Check if a person is eligible to vote (age >= 18). Explanation: A person is eligible to vote if their age is 18 or above. - Input: Age = 19 - Output: Eligible to vote

age=int(input('enter your age :'))
if age >= 18:
    print('you are eligible for voting')
else:
    print('you are not eligible for voting')


# 7. Student Pass/Fail Based on All Subjects >= 35
# Question: Check if a student passed all subjects (maths, physics, chemistry). Explanation: Student passes only if marks in all subjects are 35 or more. - Input: Maths = 40, Physics = 36, Chemistry = 30 - Output: Fail

Maths = int(input('enter marks'))
Physics = int(input('enter marks'))
Chemistry = int(input('enter marks'))
count=0
if Maths>35:
    count+=1
elif Physics>35:
    count+=1
if Chemistry>35:
    count+=1

if count==3:
    print('yes')
else:
    print('noo')


# 8. Student Pass if Passed Any One Subject (>= 35)
# Question: Check if the student passed at least one subject. Explanation: Use logical OR to check if any one subject has marks >= 35. - Input: Maths = 20, Physics = 38, Chemistry = 25 - Output: Pass

Maths = int(input('enter marks'))
Physics = int(input('enter marks'))
Chemistry = int(input('enter marks'))
count=0
if Maths>35:
    count+=1
elif Physics>35:
    count+=1
if Chemistry>35:
    count+=1

if count>=1:
    print('yes')
else:
    print('noo')


# 9. Student Pass if Passed Any Two Subjects
# Question: Check if the student passed any two out of three subjects. Explanation: Use a counter or logical conditions to verify two subjects >= 35. - Input: Maths = 40, Physics = 20, Chemistry = 36 - Output: Pass

maths=int(input('enter a num : '))
physics=int(input('enter a num : '))
chemistry=int(input('enter a num : '))
count=0
if maths>=35:
    count+=1
if physics>=35:
    count+=1
if chemistry>=35:
    count+=1
if count>=2:
    print('pass')
else:
    print('fail')

# 10. Biggest Among Three Numbers
# Question: Find the biggest number among three. Explanation: Compare each pair of numbers using if-else conditions. - Input: A = 7, B = 4, C = 9 - Output: Biggest is: 9

x,y,z=5,3,7
if x>y and x>z:
    print(x)
elif y>x and y>z:
    print(y)
else:
    print(z)


# 11. Smallest Among Three Numbers
# Question: Find the smallest number among three. Explanation: Use comparison logic to determine the minimum value. - Input: A = 7, B = 4, C = 9 - Output: Smallest is: 4

x,y,z=5,3,7
if x<y and x<z:
    print(x)
elif y<x and y<z:
    print(y)
else:
    print(z)


# 12. Perfect Square or Not
# Question: Check if a number is a perfect square. Explanation: A number is a perfect square if the square of its square root equals the number. - Input: Number = 49 - Output: Perfect square

num=25
sqrt=int(num**0.5)
if sqrt**2==num:
    print('yes')
else:
    print('no')


# 13. Cars Required for Members (Max 5 per car)
# Question: Calculate how many cars are needed for a given number of people. Explanation: Divide total people by 5 and round up using ceiling logic. - Input: Members = 17 - Output: Cars needed = 4

persons=26
if persons%5==0:
    print(persons//5)
else:
    print(persons//5+1)

x=23
if x%3==0:
    print(x//3)
else:
    print(x//3+1)


# 14. Second Biggest Among Three Numbers
# Question: Find the second largest number among three inputs. Explanation: Use sorting or nested conditions to find the second largest value. - Input: A = 10, B = 25, C = 18 - Output: Second biggest: 18

x=int(input('enter a num x: '))
y=int(input('enter a num y: '))
z=int(input('enter a num z: '))
if (x>y and x<z) or (x<y and x>z):
    print(x)
elif (y>x and y<z) or (y<x and y>z):
    print(y)
else:
    print(z)
