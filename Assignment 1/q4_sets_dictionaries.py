# Q4: Sets and Dictionaries

# ---- Sets ----
set_a = {1, 2, 3, 4, 5, 6}
set_b = {4, 5, 6, 7, 8, 9}

print("Set A:", set_a)
print("Set B:", set_b)
print("Union                :", set_a | set_b)
print("Intersection         :", set_a & set_b)
print("Difference (A - B)   :", set_a - set_b)
print("Symmetric difference :", set_a ^ set_b)

# ---- Dictionary ----
students = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 85,
    "Sneha": 67,
    "Kabir": 88,
}

print("\nStudent records:")
for name, marks in students.items():
    print(f"{name}: {marks}")

top_student = max(students, key=students.get)
print(f"\nStudent with highest marks: {top_student} ({students[top_student]})")
