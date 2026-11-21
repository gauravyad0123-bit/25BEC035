def fib(n):
    if n < 0:
        raise ValueError('n must be non-negative')
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(5))  # 5