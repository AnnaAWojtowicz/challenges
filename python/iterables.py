# Aggregate and Analyze Iterables

# This tutorial recaps what we've learned about Python iterables, such as strings and lists. We'll use built-in functions like min(), max(), and sum() to extract information from these iterables.

# Let's talk about iterables.
# An iterable is a Python object that can be iterated over, meaning you can traverse through all the elements in the object.
# You already know the most common Python iterables: strings, lists, and tuples:
str = 'iterable'
lst = [1, 2, 3]
tpl = (1, 2, 3)
dict = {'a': 1, 'b': 2, 'c': 3}

# Remember that you can loop through the elements in all of these iterables:
def traverse(iter):
  for item in iter:
    print(item)

traverse('iter')    # i t e r
traverse([1, 2, 3])     # 1 2 3
traverse((1, 2, 3))     # 1 2 3
traverse({'a': 1, 'b': 2, 'c': 3})      # a b c

# Sometimes, you'll need to get some general information about these iterables.
# For example, you might want to get the maximum value of a list of numbers.
# You could do this using a for-loop:
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max_value = 0
for number in numbers:
    if number > max_value:
        max_value = number
print('The maximum value is:', max_value)   # The maximum value is: 9

# While this approach works, it involves quite a bit of code. Fortunately, Python offers built-in functions that can simplify these tasks significantly.
# The max() function returns the largest item in an iterable.
# Here's how you can use it:
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max_value = max(numbers)
print('The maximum value is:', max_value)   # The maximum value is: 9


# Similarly, the min() function returns the smallest item in an iterable.
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_value = min(numbers)
print('The minimum value is:', min_value)   # The minimum value is: 1

# If we apply min() and max() to a string, we get the smallest and largest character based on their Unicode values.
# This behavior can be useful when you want to find the 'smallest' or 'largest' character in a string based on alphabetical order.
# Let's see how this works:
text = 'hello'
 
print('The minimum character is:', min(text))   # The minimum character is: e
print('The maximum character is:', max(text))   # The maximum character is: o

# extra examples:

nums = [10, 5, 20]
min_num = min(nums)
max_num = max(nums)
print(min_num, max_num)     # 5 20


text = 'abc'
min_char = min(text)
max_char = max(text)
print(min_char, max_char)   # a c



# The sum() function returns the sum of all items in an iterable, such as a list of numbers.
# Here's how you can use it:
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print('The total sum is:', total)   # The total sum is: 15

# However, while min() and max() work with strings, the sum() function is only for numerical iterables.

# extra examples:

numbers = (2, 4, 6, 8)
total = sum(numbers)
print(total)    # 20


mixed_values = [1, 'two', 3]
max_value = max(mixed_values)
print(max_value)    # TypeError: '>' not supported between instances of 'str' and 'int'


#  EXERCISES:

# Create a function called find_max that takes an iterable as an argument and returns its maximum value.
def find_max(sth):
	max_value = max(sth)
	return max_value

print(find_max([1, 2, 3])) # expected 3
print(find_max([1.3, 1.1, 1.0])) # expected 1.3
print(find_max('Python')) # expected y
 

# Use the max() function to get the maximum key in the dictionary.
dict = {
  'c': 3,
  'a': 1,
  'd': 5,
  'b': 2
}

max_key = max(dict)
 
print(max_key) # output d


# Use the min() function to get the minimum value in the dictionary. Hint: We don't want the minimum of the dictionary keys.
dict = {
  'apple': 3,
  'banana': 1,
  'cherry': 5,
  'strawberry': 2
}

min_val = min(dict.values())
 
print(min_val) # expected 1



# Create a function called get_sum that takes a tuple as an argument and returns the sum of its values.
def get_sum(sth):
	sum_sth = sum(sth)
	return sum_sth

print(get_sum((1, 3, 5, 7, 9))) # expected 25
print(get_sum((-3, 3, -3, 3, -3))) # expected -3


# Create a function called get_avg that takes a list of numbers as argument and returns the average of those numbers.
def get_avg(sth):
	average = sum(sth) / len(sth)
	return average
 
print(get_avg([10, 20, 30])) # expected 20
print(get_avg([-10, 0, 10])) # expected 0



#  Introduction to list comprehension
# This tutorial explores list comprehension in Python—a concise way to create lists from iterables. We’ll cover the basic syntax, usage, and show how list comprehension can often replace traditional for-loops.
# Let's talk about list comprehension in Python.
# List comprehension is a concise way to create lists in Python.
# It allows you to generate a new list by applying an expression to each item in an existing iterable.
# The basic syntax of list comprehension is:

# new_list = [expression for item in iterable]

# It's basically a for loop inside a list statement.
# For instance, let's say you want to create a list of squares for numbers from 0 to 9.
# In a traditional for-loop we would do it like this:
squares = []
for x in range(10):
  squares.append(x**2)
print(squares)      # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Using list comprehension, we can achieve the same result in a single line of code:
squares = [x**2 for x in range(10)]
print(squares)      # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Here, we loop through a range from 0-9. Each integer is temporarily assigned to the variable x.
# Next, we calculate x**2 and immediately save the result as a new item in the squares list.
# Now, let's look at another example. 
# Let's say we have a list of words and we want to create a new list that contains the length of each word.
words = ['apple', 'banana', 'cherry', 'date']
lengths = [len(word) for word in words]
print(lengths)      # [5, 6, 6, 4]

# First, we loop through words and temporarily assign each word to the variable word.
# Then, we use len to count the number of characters and assign the result as a new item in the lengths list.


# extra examples:

numbers = [1, 2, 3, 4, 5]
squared_numbers = [n**2 for n in numbers]
print(squared_numbers)      # [1, 4, 9, 16, 25]


sentence = 'Add a comment'
word_lengths = [len(word) for word in sentence.split()]
print(word_lengths)     # [3, 1, 7]


uppercase_chars = [char + char for char in 'abcd']
print(uppercase_chars)      # ['aa', 'bb', 'cc', 'dd']



# EXERCISES: 

#  Here, we use list comprehension to double the integers in the numbers list. However, there's something missing. Fix the code to get the correct output. Hint: The mistake is in the expression part of the list comprehension. Remember the syntax: [expression for item in iterable].
numbers = [10, 20, 30, 40, 50]
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers) # output [20, 40, 60, 80, 100]


# Here, we use list comprehension to extract the first character of each name in the names list. However, there's a small mistake. Fix the code to get the correct output.
names = ["Alice", "Bob", "Charlie", "David"]
first_characters = [name[0] for name in names]
print(first_characters) # output ['A', 'B', 'C', 'D']


# Use list comprehension to create a new list containing the length of each string in the words list.
words = ['moon', 'stars', 'galaxy']
lengths = [len(word) for word in words]
print(lengths) # output [4, 5, 6]


# Mastering the zip() Function in Python
# In this lesson, you will learn how to use Python's zip() function to pair elements from multiple lists or tuples, iterate through zipped results, and apply practical techniques for combining and processing data in parallel.
#  In this lesson, you'll master the zip() function for pairing items from multiple lists or tuples.
# Let's start by combining two lists of equal length with zip().
colors = ["red", "green", "blue"]
fruits = ["apple", "pear", "berry"]

# Use zip() to pair elements from both lists
paired_list = list(zip(colors, fruits))
print(paired_list)      # [('red', 'apple'), ('green', 'pear'), ('blue', 'berry')]

# zip() pairs items by their position, creating tuples of each matching element.
# Here's the syntax for using zip():

# Define two iterables (lists or tuples)
iterable_one = [1, 2, 3]
iterable_two = ['a', 'b', 'c']

# Use zip() to pair elements from both iterables
paired_items = zip(iterable_one, iterable_two)

# paired_items is an iterator of tuples like (1, 'a'), (2, 'b'), (3, 'c')
# To see the pairs, convert to a list or loop over it:
for number, letter in paired_items:
    # number and letter come from the paired tuples
    print((number, letter))


# You can also use zip() with tuples.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# zip() combines elements from both tuples into pairs
zipped_result = zip(tuple1, tuple2)

# Convert the zipped object to a list to display the pairs
result_list = list(zipped_result)
print(result_list)      # [(1, 4), (2, 5), (3, 6)]



# extra examples: 

fruits = ["apple", "banana"]
colors = ["red", "yellow"]
zipped = list(zip(fruits, colors))
print(zipped)   # [('apple', 'red'), ('banana', 'yellow')]


# What if your lists are different lengths? Let's see what happens. 
# zip() stops at the shortest list when lengths differ.
fruits = ['apple', 'banana', 'cherry']
colors = ['red', 'yellow']

paired = list(zip(fruits, colors))
print('Paired items:', paired)      # Paired items: [('apple', 'red'), ('banana', 'yellow')]


# extra examples: 

names = ["Alice", "Bob", "Charlie"]
pets = ["cat", "dog"]
zipped = list(zip(names, pets))
print(zipped)       # [('Alice', 'cat'), ('Bob', 'dog')]



# Here's how you might store zipped pairs in a variable:
list_one = [1, 2, 3]
list_two = ['a', 'b', 'c']

# Use zip() to pair elements from both lists
zipped_pairs = zip(list_one, list_two)

# Convert the zipped object to a list to inspect the pairs
zipped_pairs_list = list(zipped_pairs)

# zipped_pairs_list now holds the paired tuples
# Example content: [(1, 'a'), (2, 'b'), (3, 'c')]

# You can loop through a zipped result to process pairs.
names = ["Alice", "Bob", "Charlie"]
ages = [24, 30, 18]

zipped_list = zip(names, ages)

for pair in zipped_list:
    print("Name: " + str(pair[0]) + ", Age: " + str(pair[1]))
# Name: Alice, Age: 24
# Name: Bob, Age: 30
# Name: Charlie, Age: 18


# You can also unpack values from each zipped tuple directly in the loop.
list_one = [10, 20, 30]
list_two = ['a', 'b', 'c']

for number, letter in zip(list_one, list_two):
    # Unpack each pair from zip directly into 'number' and 'letter'
    print(number, letter)
# 
# 
# 
#  #