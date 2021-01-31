
import pandas as pd
import matplotlib as plt

# 1a. Create a fruit variable to hold a series of data (see data below)
fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple",
            "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", 
            "blackberry", "gooseberry", "papaya"])

# 1b. Run Describe() on the fruits series
print(fruits.describe())

# 1c. Run the code necessary to produce only the unique fruit names.
print(fruits.unique())

# 1d. Determine how many times each value occurs in the series.
print(fruits.value_counts())

# 1e. Determine the most frequently occurring fruit name from the series.
print(fruits.mode())

# 1f. Determine the least frequently occurring fruit name from the series.
print(fruits.value_counts().sort_values(ascending=True).head(1))

# 1g. Write the code to get the longest string from the fruits series.
print(fruits[fruits.str.len() == fruits.str.len().max()])

# 1h. Find the fruit(s) with 5 or more letters in the name.
print(fruits[fruits.str.len() >= 5])

# 1i. Capitalize all the fruit strings in the series.
print(fruits.str.capitalize())

# 1j. Count the letter "a" in all the fruits (use string vectorization)
print(fruits.str.count('a').sum())

# 1k Output the number of vowels in each and every fruit.
def count_vowels(string):
    vowels = 'aeiou'
    vowel_count = 0
    for v in string:
        if v in vowels:
            vowel_count += 1
    return vowel_count

print(fruits.apply(count_vowels))

# 1i. Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.
print(fruits[fruits.apply(lambda f: True if f.count('o') >= 2 else False)])

# 1m. Write the code to get only the fruits containing "berry" in the name
print(fruits[fruits.str.contains('berry')])

# 1n. Write the code to get only the fruits containing "apple" in the name
print(fruits[fruits.str.contains('apple')])

# 1o. Which fruit has the highest amount of vowels?
print(fruits[fruits.apply(count_vowels).sort_values().tail(1)])


# 2. 
values = pd.Series(['$796,459.41', '$278.60', '$482,571.67','$4,503,915.98', '$2,121,418.3', 
        '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', 
        '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', 
        '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])

# 2a. What is the data type of the series?
print(values)
# Answer: Object

# 2b. Use series operations to convert the series to a numeric data type.
values = values.str.strip('$')
values = values.str.replace(',', '')
values = values.astype(float)
print(values)

# 2c. What is the maximum value? The minimum?
print(values.max())
print(values.min())

# 2d. Bin the data into 4 equally sized intervals and show how many values fall into each bin.
cut_values = pd.cut(values, 4).value_counts()
print(cut_values)

# 2e. Plot a histogram of the data. Be sure to include a title and axis labels.
cut_values.plot.hist()

# 3. 
scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])

# 3a. What is the minimum exam score? The max, mean, median?
print(scores.describe())

# 3b. Plot a histogram of the scores.
scores.plot.hist()

# 3c. Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.
def apply_grades(n):
    if n > 90:
        return 'A'
    elif n > 80:
        return 'B'
    elif n > 70:
        return 'C'
    elif n > 60:
        return 'D'
    else:
         return 'F'

print(scores.apply(apply_grades))

# 3d. Write the code necessary to implement a curve. 
# I.e. that grade closest to 100 should be converted to a 100, 
# and that many points should be given to every other score as well.
curve = 100 - scores.max()
scores += curve
print(scores)

# 4. 
letters = 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
letters = list(letters)
letters = pd.Series(letters)


# 4a. What is the most frequently occuring letter? Least frequently occuring?
print(letters.mode())

# 4b. How many vowels are in the list?
print(letters.apply(count_vowels).sum())

# 4c. How many consonants are in the list?
def count_constants(string):
    vowels = 'aeiou'
    constant_count = 0
    for v in string:
        if v not in vowels:
            constant_count += 1
    return constant_count

print(letters.apply(count_constants).sum())

# 4d. Create a series that has all of the same letters, but uppercased
print(letters.str.upper())

# 4e. Create a bar plot of the frequencies of the 6 most frequently occuring letters.
top_six_repeating_values = letters.value_counts().head(6)
top_six_repeating_values.plot.bar()