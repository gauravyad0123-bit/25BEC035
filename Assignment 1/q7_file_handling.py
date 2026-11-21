# Q7: File Handling

filename = "students.txt"
students = [
    ("101", "Aarav Sharma", "Computer Science", 78),
    ("102", "Diya Verma", "Information Technology", 92),
    ("103", "Rohan Patel", "Electronics", 85),
]

with open(filename, "w") as f:
    f.write("Roll No | Name | Branch | Marks\n")
    for roll, name, branch, marks in students:
        f.write(f"{roll} | {name} | {branch} | {marks}\n")

print(f"Student details written to '{filename}'.\n")
with open(filename, "r") as f:
    contents = f.read()

print("Contents of the file:")
print(contents)
