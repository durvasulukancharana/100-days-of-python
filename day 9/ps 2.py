# Generate a tuple of prime numbers between 10 to 50 using comprehension.

primes = tuple(
    num for num in range(10, 51)
    if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)))
print(primes)

for i in range(10,50):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)