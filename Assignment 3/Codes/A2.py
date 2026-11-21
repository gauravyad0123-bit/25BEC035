def factorial(n):
    if n < 0:
        raise ValueError('n must be non-negative')
    if n == 0:                 # base case
        return 1
    return n * factorial(n - 1)

def natural_sum(n):
    if n < 0:
        raise ValueError('n must be non-negative')
    if n == 0:                 # base case
        return 0
    return n + natural_sum(n - 1)

def power(x, n):
    if n < 0:
        raise ValueError('exponent must be non-negative')
    if n == 0:                 # base case
        return 1
    return x * power(x, n - 1)

print(factorial(5))       # 120
print(natural_sum(5))      # 15
print(power(2, 5))