
def prefix_average1(X):
    n = len(X)
    A = [0] * n

    for i in range(n):
        total = 0

        for j in range(i + 1):
            total += X[j]

        A[i] = total / (i + 1)

    return A
