
def prefix_average2(X):
    n = len(X)
    A = [0] * n

    total = 0

    for i in range(n):
        total += X[i]
        A[i] = total / (i + 1)

    return A
