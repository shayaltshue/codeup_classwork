# 1. Conditional Basics
    
#     a. prompt the user for a day of the week, print out whether the day is Monday or not
day = input('What is the day today?').lower().strip()
if day == 'monday':
    print("It's monday") 
else:
    print("It's not monday")

#     b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
day = input('What is the day today?').lower().strip()
if day in ('saturday', 'sunday'):
    print("It's the weekend") 
else:
    print("It's not the weekend")

#     c. create variables and make up values for
#         - the number of hours worked in one week
#         - the hourly rate
#         - how much the week's paycheck will be
#         - write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

num_hours_worked_this_week = 70
hourly_rate = 18
paycheck = num_hours_worked_this_week * hourly_rate
overtime = num_hours_worked_this_week - 40
if overtime > 0:
    paycheck = (overtime * (hourly_rate * 1.5)) + ((num_hours_worked_this_week - overtime) * hourly_rate)
print(paycheck)

# 2. Loop Basics

#     a. While
#         - Create an integer variable i with a value of 5.
#         - Create a while loop that runs so long as i is less than or equal to 15
#         - Each loop iteration, output the current value of i, then increment i by one.

i = 5

while i <= 15:
    print(i)
    i += 1

#     Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
#     Alter your loop to count backwards by 5's from 100 to -10.
#     Create a while loop that starts at 2,
#      and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

i = 2
while i <= 1000000:
    print(i)
    i = i ** 2
    
    #     Write a loop that uses print to create the output shown below.
i = 100
while i >= 5:
    print(i)
    i -= 5

#     b. For Loops

# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
n = input('Please enter a number')

while n == '':
    n = input('please enter a number that is not a blank space')

for i in range(1, 11):
    print(f"{n} * {i} = ", str(int(n) * int(i)))

# Create a for loop that uses print to create the output shown below.
values = ''
for i in range(1, 11):
    values = str(i) * i
    print(values)
    i += 1
    
    if i >= 10:
        break
    continue

# Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
n = int(input('Please select an odd number between 1 and 50'))
while n % 2 == 0 or 1 > n < 50:
    n = int(input('please enter an odd number between 1 and 50'))
for i in range(1, 51):
    if i == n:
        continue
    print(i)    
    i += 2    

# The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, 
# also note that the input function returns a string, so you'll need to convert this to a numeric type.)
n = int(input('Please enter a positive number:  '))
while n < 0:
    n = int(input('Number you entered was not positive. Please enter a positive number:   '))
i = 0
while i <= n:
    print(i)
    i += 1

# Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1.
n = int(input('Please enter a positive number:  '))
while n < 0:
    n = int(input('Number you entered was not positive. Please enter a positive number:   '))
i = 1
while n >= 1:
    print(n)
    n -= 1

# Fizzbuzz

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.


# Write a program that prints the numbers from 1 to 100.
for i in range(1, 101):
    print(i)
    i += 1

# For multiples of three print "Fizz" instead of the number
def is_multiple_of_three(num):
    return num % 3 == 0

for i in range(1, 101):
    if is_multiple_of_three(i):
        print('Fizz')
    else:
        print(i)
    i += 1

# For the multiples of five print "Buzz".
def is_multiple_of_five(num):
    return num % 5 == 0

for i in range(1, 101):
    if is_multiple_of_three(i):
        print('Buzz')
    else:
        print(i)
    i += 1

# For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1, 101):
    if is_multiple_of_three(i) and is_multiple_of_five(i):
        print('FizzBuzz')

# Display a table of powers.
for i in range(1,10):
    print(i ** i)
    i = i ** i

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
i = 1
n = int(input('What number would you like to go up to?:   '))
while n < 0:
    n = int(input('please enter a number greater than zero:   '))
while i < n + 10:
    print(f"number: {i}, squared: {i ** 2}, cubed: {i ** 3}") 
    i += 1
    if i > n:
        cont = input("would you like to continue? Enter y to continue:   ")
        if cont != 'y':
            break
 
# Example Output

# What number would you like to go up to? 5

# Here is your table!

# number | squared | cubed
# ------ | ------- | -----
# 1      | 1       | 1
# 2      | 4       | 8
# 3      | 9       | 27
# 4      | 16      | 64
# 5      | 25      | 125
# Bonus: Research python's format string specifiers to align the table

# Convert given number grades into letter grades.
def get_letter_grade(num):
    if 100 >= num >= 96:
        return 'A+'
    if num == 95:
        return 'A'
    if 94 >= num >= 90:
        return 'A-'        
    elif 89 >= num >= 86:
        return 'B+'
    elif num == 85:
        return 'B'
    elif 84 >= num >= 80:
        return 'B-'
    elif 79 >= num >= 76:
        return 'C+'
    elif num == 75:
        return 'C'
    elif 74 >= num >= 70
        return 'C-'
    elif 69 >= num >= 66:
        return 'D+'
    elif num == 65:
        return 'D'
    elif 64 >= num >= 60
        return 'D-'
    else:
        return 'F'

# Prompt the user for a numerical grade from 0 to 100.
cont = "y"
while cont == 'y':
    grade = int(input('Please enter a number between 0 and 100:   '))
# Display the corresponding letter grade.
    letter_grade = get_letter_grade(grade)
    print(letter_grade)
# Prompt the user to continue.
    cont = input("Would you like to continue? Press 'y' then enter to continue:    ")
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0
# Bonus
# Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

# 6. Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author, and genre. 
# Loop through the list and print out information about each book.
my_books = [
    {'title': "Ender's Game", 'author': 'Orson Scott Card', 'genre': 'Sci-fi'},
    {'title': 'Eragon', 'author': 'Christopher Paoloni', 'genre': 'Fantasy'},
    {'title': 'Halo: Fall of Reach', 'author': 'Eric Nylund', 'genre': 'Sci-fi'},
    {'title': 'Sphere', 'author': 'Michael Criton', 'genre': 'Sci-fi'}
]
[book for book in my_books]

# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.
user_selected_genre = input("Please enter a genre of books you think I've read (hint: it's only sci-fi and fantasy):    ")
[book['title'] for book in my_books if book['genre'] == user_selected_genre]