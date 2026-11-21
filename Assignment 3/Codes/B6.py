marks = [
    [78, 85, 90],
    [66, 72, 80],
    [91, 88, 95]
]

# Access row 0
print(marks[0])       # [78, 85, 90]

# Access one value: row 1, column 2
print(marks[1][2])    # 80

# Traverse a column
for row in marks:
    print(row[1])     # 85, 72, 88