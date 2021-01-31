# 1. Import and test 3 of the functions from your functions exercise file.
    # Your functions exercise are not currently in a file with a name that can be easily imported. 
    # Copy your functions exercise file and name the copy functions_exercises.py.
    # Import each function in a different way:
        # import the module and refer to the function with the . syntax
import functions_exercises

functions_exercises.is_two(3)
        # use from to import the function directly
from functions_exercises import is_two

is_two(2)
        # use from and give the function a different name
from functions_exercises import is_two as t

t(2)

# For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.
import itertools as it
    # 1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
    #Use itertools. permutations() and zip() to get all unique combinations of two lists. 
    # Call itertools. permutations(iterable, r) with the longer list as iterable and the length
    # of the shorter list as r to return all r-length permutations of the longer list.
len(list(it.product('abc', [1, 2, 3])))

    # 2. How many different ways can you combine two of the letters from "abcd"?
len(list(it.combinations('abcd', 2)))

# Save this file as profiles.json inside of your exercises directory. 
# Use the load function from the json module to open this file, it will produce a list of dictionaries. 
# Using this data, write some code that calculates and outputs the following information:
import json

data = json.load(open("profiles.json"))

    # Total number of users: 19
total_num_users = len(data)
total_num_users
    
    # Number of active users: 9
len([user for user in data if user['isActive']])
    
    # Number of inactive users: 
len([user for user in data if not user['isActive']])

    # Grand total of balances for all users
from functions_exercises import handle_commas_and_symbols

balances = [user['balance'] for user in data]
balances_to_float = []
[balances_to_float.append(handle_commas_and_symbols(balance)) for balance in balances]
sum_of_all_balances = sum(balances_to_float)
sum_of_all_balances
    
    # Average balance per user
avg_balance_per_user = sum_of_all_balances / len(data)
avg_balance_per_user

    # User with the lowest balance
[(user['name'], user['balance']) for user in data if user['balance'] == min([user['balance'] for user in data])]
    # User with the highest balance
[(user['name'], user['balance']) for user in data if user['balance'] == max([user['balance'] for user in data])]
    # Most common favorite fruit
from collections import Counter

favorite_fruits = [user['favoriteFruit'] for user in data]
occurrence_counter = Counter(favorite_fruits)
max(occurrence_counter)

    # Least most common favorite fruit
from collections import Counter

favorite_fruits = [user['favoriteFruit'] for user in data]
occurrence_counter = Counter(favorite_fruits)
min(occurrence_counter)
   
    # Total number of unread messages for all users
# step 1, extract all of the greetings from the users in profiles (aka data)
greetings = [user['greeting'] for user in data]

total_unread_messages = 0
for greeting in greetings:
    greeting = greeting.split()
    for x in greeting:
        if x.isdigit():
            total_unread_messages += int(x)
total_unread_messages