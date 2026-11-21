# Q1: Basic Python Operations
# Accept two numbers and display sum, difference, product, quotient, remainder.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Sum        :", a + b)
print("Difference :", a - b)
print("Product    :", a * b)

if b != 0:
    print("Quotient   :", a / b)
    print("Remainder  :", a % b)
else:
    print("Quotient   : Cannot divide by zero")
    print("Remainder  : Cannot divide by zero")
