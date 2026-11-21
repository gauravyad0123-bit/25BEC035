# Q8: Exception Handling

try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    result = a / b
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")
else:
    print(f"Result: {a} / {b} = {result}")
finally:
    print("Program execution completed.")
