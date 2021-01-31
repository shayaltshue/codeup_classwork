# 1. Read the contents of your last exercise file into a variable.
with open('4.6_import_exercises.py', 'r') as f:
    contents = f.readlines()
# Print out every line in the file
# Print out every line in the file, but add a line numbers
    for i, line in enumerate(contents, start=1):
        print(i, ': ', line)

# Write some python code to create a grocery list.
# Create a variable named grocery_list. 
    # It should be a list, and the elements in the list should be at 
    # least 3 things that you need to buy from the grocery store.
file_name = ''
grocery_list = ['Banana', 'Sugar', 'Steak']

# a. Create a function named make_grocery_list. 
    # When run, this function should write the contents of the grocery_list variable 
    # to a file named my_grocery_list.txt.
def make_grocery_list(items):
    file_name = 'my_grocery_list.txt'
    with open(file_name, 'w') as f:
        for item in items:
            f.writelines(f'{item}\n')
    return file_name

# b. Create a function named show_grocery_list. 
    # When run, it should read the items from the text file and show each item on the grocery list.
def show_grocery_list():
    with open('my_grocery_list.txt', 'r') as f:
        contents = f.readlines()
        for item in contents:
            print(item)
        return contents

# c. Create a function named buy_item. 
    # It should accept the name of an item on the grocery list, and remove that item from the list.
def buy_item(bought_item):
    grocery_list = show_grocery_list()
    for item in grocery_list:
        if bought_item in item:
            grocery_list.remove(item)
    make_grocery_list(grocery_list)
    show_grocery_list()

file_name = make_grocery_list(grocery_list)
buy_item('Banana')