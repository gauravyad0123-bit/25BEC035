# Q3: Strings

text = input("Enter a string: ")

# Count characters
print("Number of characters:", len(text))

# Count vowels and consonants
vowels = 0
consonants = 0
for ch in text.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)

# Reverse the string
reversed_text = text[::-1]
print("Reversed string:", reversed_text)

# Palindrome check: compare the string with its reverse
if text == reversed_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
