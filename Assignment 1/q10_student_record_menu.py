# Q10: Menu-driven student record management using a dictionary

students = {}  # {name: marks}


def add_student():
    name = input("Enter student name: ").strip()
    if name in students:
        print("Student already exists. Use 'Update marks' instead.")
        return
    try:
        marks = float(input("Enter marks: "))
    except ValueError:
        print("Invalid marks.")
        return
    students[name] = marks
    print(f"Student '{name}' added.")


def update_marks():
    name = input("Enter student name: ").strip()
    if name not in students:
        print("Student not found.")
        return
    try:
        students[name] = float(input("Enter new marks: "))
        print(f"Marks updated for '{name}'.")
    except ValueError:
        print("Invalid marks.")


def search_student():
    name = input("Enter student name to search: ").strip()
    if name in students:
        print(f"Found: {name} - {students[name]}")
    else:
        print("Student not found.")


def delete_student():
    name = input("Enter student name to delete: ").strip()
    if name in students:
        del students[name]
        print(f"Student '{name}' deleted.")
    else:
        print("Student not found.")


def display_all():
    if not students:
        print("No student records available.")
        return
    print(f"{'Name':<20}{'Marks':>8}")
    print("-" * 28)
    for name, marks in students.items():
        print(f"{name:<20}{marks:>8}")


while True:
    print("\n===== Student Record Menu =====")
    print("1. Add a student")
    print("2. Update marks")
    print("3. Search for a student")
    print("4. Delete a student")
    print("5. Display all student records")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        update_marks()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        display_all()
    elif choice == "6":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
