# Q2: Lists and Tuples

numbers = [12, 45, 7, 23, 56, 89, 34, 21, 67, 10]
print("Original list:", numbers)

# Add an element (at the end)
numbers.append(99)
print("After adding 99:", numbers)

# Remove an element
numbers.remove(7)
print("After removing 7:", numbers)

# Insert an element at a specified position
numbers.insert(2, 100)
print("After inserting 100 at index 2:", numbers)

# Maximum and minimum
print("Maximum element:", max(numbers))
print("Minimum element:", min(numbers))

# Convert list into tuple
numbers_tuple = tuple(numbers)
print("List converted to tuple:", numbers_tuple)
print("Type:", type(numbers_tuple))
