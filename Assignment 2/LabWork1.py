import time
import random
import math
import matplotlib.pyplot as plt

# List Indexing - O(1)
def list_index(a):
    return a[len(a)//2]


# Binary Search - O(log n)
def binary_search(a, x):
    low = 0
    high = len(a)-1

    while low <= high:
        mid = (low+high)//2

        if a[mid] == x:
            return mid
        elif a[mid] < x:
            low = mid+1
        else:
            high = mid-1

    return -1


# Linear Search - O(n)
def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


# Merge Sort - O(n log n)
def merge_sort(a):
    if len(a) <= 1:
        return a

    mid = len(a)//2

    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result += left
    result += right

    return result


# Pair Counter - O(n^2)
def pair_counter(a):
    count = 0

    for i in range(len(a)):
        for j in range(i+1, len(a)):
            count += 1

    return count


# Subset Enumeration - O(2^n)
def subset_count(a):
    count = 0

    for i in range(2**len(a)):
        count += 1

    return count


# Function to calculate average time
def calculate_time(func, a, x=None):
    total = 0

    for i in range(5):
        start = time.time()

        if x is None:
            func(a)
        else:
            func(a, x)

        end = time.time()
        total += end-start

    return total/5


# Input sizes
sizes1 = [10000, 20000, 30000, 40000, 50000]
sizes2 = [1000, 5000, 10000, 50000, 100000]
sizes3 = [1000, 5000, 10000, 20000, 50000]
sizes4 = [100, 500, 1000, 2000, 3000]
sizes5 = [5, 8, 10, 12, 15]

# Store execution times
t1 = []
t2 = []
t3 = []
t4 = []
t5 = []
t6 = []

# List Indexing
for n in sizes1:
    a = list(range(n))
    t1.append(calculate_time(list_index, a))

# Binary Search
for n in sizes2:
    a = list(range(n))
    t2.append(calculate_time(binary_search, a, n-1))

# Linear Search
for n in sizes3:
    a = list(range(n))
    t3.append(calculate_time(linear_search, a, -1))

# Merge Sort
for n in sizes3:
    a = [random.randint(1, 10000) for i in range(n)]
    t4.append(calculate_time(merge_sort, a))

# Pair Counter
for n in sizes4:
    a = list(range(n))
    t5.append(calculate_time(pair_counter, a))

# Subset Enumeration
for n in sizes5:
    a = list(range(n))
    t6.append(calculate_time(subset_count, a))


# Display results
print("Algorithm       Input Size       Time")

for name, sizes, times in [
    ("List Indexing", sizes1, t1),
    ("Binary Search", sizes2, t2),
    ("Linear Search", sizes3, t3),
    ("Merge Sort", sizes3, t4),
    ("Pair Counter", sizes4, t5),
    ("Subset Enumeration", sizes5, t6)
]:
    print("\n", name)

    for n, t in zip(sizes, times):
        print(n, "          ", t)


# Plot execution time graphs
graphs = [
    ("List Indexing", sizes1, t1),
    ("Binary Search", sizes2, t2),
    ("Linear Search", sizes3, t3),
    ("Merge Sort", sizes3, t4),
    ("Pair Counter", sizes4, t5),
    ("Subset Enumeration", sizes5, t6)
]

for name, sizes, times in graphs:
    plt.figure()
    plt.plot(sizes, times, marker='o')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title(name)
    plt.grid()
    plt.show()


# Normalized graphs

plt.figure()
plt.plot(sizes3, [t/n for t, n in zip(t3, sizes3)], marker='o')
plt.title("Linear Search - T(n)/n")
plt.xlabel("Input Size")
plt.ylabel("Normalized Time")
plt.grid()
plt.show()


plt.figure()
plt.plot(sizes3, [t/(n*math.log2(n)) for t, n in zip(t4, sizes3)], marker='o')
plt.title("Merge Sort - T(n)/(n log n)")
plt.xlabel("Input Size")
plt.ylabel("Normalized Time")
plt.grid()
plt.show()


plt.figure()
plt.plot(sizes4, [t/(n*n) for t, n in zip(t5, sizes4)], marker='o')
plt.title("Pair Counter - T(n)/n²")
plt.xlabel("Input Size")
plt.ylabel("Normalized Time")
plt.grid()
plt.show()