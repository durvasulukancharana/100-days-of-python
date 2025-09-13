# Interview-Style Programming Questions: Loops, Strings, and Number Operations

# 1. Print Numbers from 1 to n
# Question: Write a program to print numbers from 1 to n. Explanation: Use a loop starting from 1 to n and print each number. - Input: n = 5 - Output: 1 2 3 4 5

x=int(input('enter a num :'))
for i in range(1,(x)+1):
    print(i)


# 2. Print Numbers from m to n
# Question: Write a program to print numbers from m to n. Explanation: Loop from m to n and print values. - Input: m = 3, n = 7 - Output: 3 4 5 6 7

x=int(input('enter a num :'))
y=int(input('enter a num :'))
for i in range(x,y+1):
    print(i)


# 3. Print Numbers from n to 1 in Reverse
# Question: Write a program to print numbers in reverse from n to 1. Explanation: Use a loop starting from n and decrement to 1. - Input: n = 5 - Output: 5 4 3 2 1

x=int(input('enter a num :'))
for i in range((x+1)-1,0,-1):
    print(i)


# 4. Print Numbers from n to m in Reverse
# Question: Write a program to print numbers from n to m in reverse. Explanation: Start from n and go down to m. - Input: n = 10, m = 6 - Output: 10 9 8 7 6

m=int(input('enter a num :'))
n=int(input('enter a num :'))
for i in range(n,m-1,-1):
    print(i)


# 5. Sum of n Natural Numbers
# Question: Write a program to calculate the sum of first n natural numbers. Explanation: Use formula or loop to sum from 1 to n. - Input: n = 5 - Output: 15

x=int(input('enter a num:'))
sum=0
for i in range(1,x+1):
    sum+=i
print(sum)


# 6. Factorial of a Number
# Question: Write a program to find the factorial of a number. Explanation: Multiply all numbers from 1 to n. - Input: n = 5 - Output: 120

x=int(input('enter a num:'))
y=1
for i in range(1,x+1):
    y*=i
print(y)


# 7. Sum of m to n Numbers
# Question: Write a program to find the sum of all numbers from m to n. Explanation: Loop from m to n and add values. - Input: m = 3, n = 6 - Output: 18

x=3
y=6
z=0
for i in range(x,y+1):
    z+=i
print(z)


# 8. Product of m to n Numbers
# Question: Write a program to find the product of numbers from m to n. Explanation: Loop from m to n and multiply values. - Input: m = 2, n = 4 - Output: 24

x=2
y=4
z=1
for i in range(x,y+1):
    z*=i
print(z)


# 9. Print Factors of a Number
# Question: Write a program to print all factors of a given number. Explanation: Check divisibility of number from 1 to n. - Input: n = 6 - Output: 1 2 3 6

x=int(input('enter a num:'))
for i in range(1,x+1):
    if x%i==0:
        print(i)


# 10. Count of Factors
# Question: Write a program to count how many factors a number has. Explanation: Increment count when divisible. - Input: n = 6 - Output: 4

x=int(input('enter a num:'))
count=0
for i in range(1,x+1):
    if x%i==0:
        count+=1
print(count)


# 11. Prime Number Check
# Question: Check if a number is prime. Explanation: A number is prime if it has exactly 2 factors. - Input: n = 7 - Output: Prime

x=int(input('enter a num :'))
count=0
for i in range(1,x+1):
    if x%i==0:
        count+=1
if count==2:
    print('prime')
else:
    print('not')

def check(num):
    if num<2:
        return False
    for i in range(2,num):
        if num % i==0:
            return 'not prime'
    return 'prime'
print(check(8))

# 12. Even Numbers from m to n
# Question: Print all even numbers between m and n. Explanation: Use loop and check if divisible by 2. - Input: m = 3, n = 10 - Output: 4 6 8 10

m=int(input('enter a num :'))
n=int(input('enter a num :'))
for i in range(m,n+1):
    if i % 2==0:
        print(i)


# 13. Odd Numbers from m to n
# Question: Print all odd numbers between m and n. Explanation: Check if number % 2 != 0. - Input: m = 3, n = 10 - Output: 3 5 7 9

m=int(input('enter a num :'))
n=int(input('enter a num :'))
for i in range(m,n+1):
    if i % 2!=0:
        print(i)


# 14. Count of Even and Odd Numbers
# Question: Count how many even and odd numbers are in the range m to n. Explanation: Use counters for even and odd. - Input: m = 3, n = 7 - Output: Even = 2, Odd = 3

m=int(input('enter a num :'))
n=int(input('enter a num :'))
x=0
y=0
for i in range(m,n+1):
    if i%2==0:
        x+=1
    else:
        y+=1
print(x)
print(y)


# 15. Reverse a String
# Question: Reverse a given string. Explanation: Use slicing or loop. - Input: “hello” - Output: “olleh”

x='hello'
print(x[::-1])

x='hello'
y=''
for i in x:
    y=i+y
print(y)

x='hello'
for i in range(len(x)-1,-1,-1):
    print(x[i],end='')


# 16. Check for Palindrome String
# Question: Check if a string is a palindrome. Explanation: Compare string with its reverse. - Input: “madam” - Output: Palindrome

x=input('enter a name :')
y=''
for i in range(len(x)-1,-1,-1):
    y+=x[i]
if x==y:
    print('yes')
else:
    print('no')


# 17. Sum of Digits
# Question: Calculate the sum of digits of a number. Explanation: Use loop and % 10 to extract digits. - Input: 123 - Output: 6

x=int(input('enter a num :'))
y=0
for i in str(x):
    y+=int(i)
print(y)


# 18. Product of Digits
# Question: Calculate the product of digits. Explanation: Multiply digits extracted from number. - Input: 123 - Output: 6

x=int(input('enter a num :'))
y=1
for i in str(x):
    y*=int(i)
print(y)


# 19. Armstrong Number Check
# Question: Check if a number is an Armstrong number. Explanation: Sum of cube of digits equals the number. - Input: 153 - Output: Armstrong number

x=int(input('enter a num :'))
y=0
for i in str(x):
    y+=int(i)**3
print(y)


# 20. Reverse a Number
# Question: Reverse the digits of a number. Explanation: Use loop with % and // to reverse. - Input: 123 - Output: 321

x=123
y=0
while x>0:
    y=x%10+y*10
    x//=10
print(y)

num=123
x=0
while num>0:
    x=num%10+x*10
    num//=10
print(x)