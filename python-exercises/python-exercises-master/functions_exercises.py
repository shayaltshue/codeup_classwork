# 1. Define a function named is_two. 
# It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(num):
    return num == 2 or num == '2'

# 2. Define a function named is_vowel. 
# It should return True if the passed string is a vowel, False otherwise.
def is_vowel(letter):

    return len(letter) == 1 and letter.lower() in 'aeiou'
# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(string):
    return not is_vowel(string)

# 4. Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.
def capitalize_word(word):
    if is_consonant(word[0]):
        return word.capitalize()
    else:
        print("Word does not start with a consonant")

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, 
# and return the amount to tip.
def calculate_tip(tip_percentage, bill_total):
    return tip_percentage * bill_total

# 6. Define a function named apply_discount. 
# It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(original_price, discount_percentage):
    return original_price - (original_price * discount_percentage)

# 7. Define a function named handle_commas. 
# It should accept a string that is a number that contains commas in it as input, 
# and return a number as output.
def handle_commas(string):
    string = string = string.replace(',', '')
    string = float(string)
    return string

# 8. Define a function named get_letter_grade.
#  It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(num):
    if num > 100 or num < 0:
        print('Please provide a number between 0 and 100')
    else:
        if num >= 90:
            return 'A'
        elif num >= 80:
            return 'B'
        elif num >= 70:
            return 'C'
        elif num >= 60:
            return 'D'
        else:
            return 'F'

# 9. Define a function named remove_vowels that accepts a string and returns a string with  all the vowels removed.
def remove_vowels(string):
    for letter in string:
        if is_vowel(letter):
            string = string.replace(letter, '')
    return string

# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# What is a python identifier, and what are the restrictions on it?
    # Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) 
    # or digits (0 to 9) or an underscore _ . ...
    # An identifier cannot start with a digit. ...
    # Keywords cannot be used as identifiers. ...
    # We cannot use special symbols like !, @, #, $, % etc. ...
    # Identifier can be of any length.
from keyword import iskeyword

def normalize_name(string):
    symbols = [
        '@', '!', '#', '$', '%', '^', '&', '*',
        '(', ')', '<', '>', '?', '/', '\\', '|', '}', '{', '~', ':', ']' '\''
         ]
    string = string.strip()
    string = string.lower()
    for letter in string:
        if letter in symbols:
            string = string.replace(letter, '')
    if iskeyword(string):
        print('Please enter a string that is not a keyword')
    elif string[0].isdigit():
        print('Please enter a string that does not begin with a digit')
    else:
        string = string.replace(' ', '_')
        return string

# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed


# Write a function named cumsum that accepts a list of numbers
#  and returns a list that is the cumulative sum of the numbers in the list.
def cumsum(list_of_num):
    sum_list = []
    sum_stored = 0
    for num in list_of_num:
        sum_list.append(sum_stored + num)
        sum_stored += num
    return sum_list

# cumsum([1, 1, 1]) returns [1, 2, 3]
# cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# Bonus
# Create a function named twelveto24. 
# It should accept a string in the format 10:45am or 4:30pm
#  and return a string that is the representation of the time in a 24-hour format. 
# Bonus write a function that does the opposite.
def twelveto24(string):
    string = string.lower()
    # Run a check to veryify if the string is in proper format
    if 'am' in string or 'pm' in string:
        string = string.replace(':', '')
        if 'pm' in string:
            string = string.replace('pm', '')
            string = int(string) + 1200
            string = str(string)
            return string
        else:
            string = string.replace('am', '')
        return string
    else:
        print("Please enter am or pm into the input")
    
        
# Create a function named col_index. It should accept a spreadsheet column name, 
# and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27

def handle_commas_and_symbols(string):
    string = string.replace(',', '')
    string = string.replace('$', '')
    string_as_float = float(string)
    return string_as_float
