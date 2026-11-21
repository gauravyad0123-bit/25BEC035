# Q9: List Comprehension

squares = [x ** 2 for x in range(1, 21)]
print("Squares of numbers from 1 to 20:")
print(squares)

evens = [x for x in range(1, 51) if x % 2 == 0]
print("\nEven numbers from 1 to 50:")
print(evens)

div_3_and_5 = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print("\nNumbers from 1 to 100 divisible by both 3 and 5:")
print(div_3_and_5)
