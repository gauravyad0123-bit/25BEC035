def recursive_sum(a, i=0, total=0):
    if i == len(a):
        return total
    return recursive_sum(a, i + 1, total + a[i])

def iterative_sum(a):
    total = 0
    for value in a:
        total += value
    return total

print(recursive_sum([2, 4, 6]))  # 12
print(iterative_sum([2, 4, 6]))  # 12