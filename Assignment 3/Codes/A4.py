def is_sorted(a, n=None):
    if n is None:
        n = len(a)
    if n <= 1:                 # base case
        return True
    if a[n - 2] > a[n - 1]:
        return False
    return is_sorted(a, n - 1)

print(is_sorted([1, 2, 2, 5]))  # True
print(is_sorted([1, 4, 3]))    # False