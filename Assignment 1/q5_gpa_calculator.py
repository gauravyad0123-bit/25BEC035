# Q5: GPA Calculator
# GPA = sum(grade point * credit) / sum(credits)

# Standard 10-point grade scale
print('\nQuestion 5')
n = int(input('Enter no. of courses: '))
credit = 0
sum = 0
for i in range(n):
    c = int(input(f'Enter no. of credits for course {i+1}: '))
    points = int(input(f'Enter grade point for course {i+1}: '))
    credit += c
    sum += c*points
print('Your GPA for this semester is equal to',sum/credit)
