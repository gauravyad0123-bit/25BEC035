# Q6: Functions and Iteration


def factorial(n):
    """Return factorial of n."""
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n):
    """Return a list with the first n terms of the Fibonacci series."""
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def is_prime(n):
    """Return True if n is prime."""
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


num = int(input("Enter a number for factorial: "))
result = factorial(num)
if result is None:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num} = {result}")

terms = int(input("Enter number of Fibonacci terms: "))
print("Fibonacci series:", fibonacci(terms))

p = int(input("Enter a number to check for prime: "))
if is_prime(p):
    print(f"{p} is a prime number.")
else:
    print(f"{p} is not a prime number.")
