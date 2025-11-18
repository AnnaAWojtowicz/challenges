# LISTS

# Let's say you want to store a collection of names. Instead of creating a separate variable for each name, you can create one variable called names that contains a series of names:

names = ['John', 'Mike', 'Sara', 'Emma']

# In Python, this is called a list.
# You can put values of any type inside a list. It can even contain values of different types. All of the following are valid lists:

strings = ['a', 'b', 'c']
numbers = [1, 2, 3]
mixed = ['a', 2, True]

# You can also nest lists within other lists:

lists = [[1, 2, 3], ['a', 'b', 'c']]

# You can access elements in a list using their index, exactly like we did with the characters of a string:

nums = [1, 2, 3]
 
# get first element
print(nums[0])      # 1
# get second element
print(nums[1])      # 2
# get last element
print(nums[-1])     # 3

# Just like with strings, the first element of a list has index 0, the second index 1, and so on...
# If you want to get a range of elements from a list, use slicing:

nums = [1, 2, 3, 4, 5]
 
# range from second to third element
print(nums[1:3])    # [2, 3]
# exclude first element
print(nums[1:])     # [2, 3, 4, 5]
# exclude last element
print(nums[:-1])    # [1, 2, 3, 4]
# copy of the entire list
print(nums[:])      # [1, 2, 3, 4, 5]

# If you want to know how many elements a list has, you can use the len() function:

nums = [1, 2, 3]
 
# get length of list
print(len(nums))    # 3

# Last but not least, you can check if a specific element exists in the list using the in operator.
# value in list

# For example, here we check if the strings 'banana' and 'orange' are in the list. If found, the value in list syntax evaluates to True; otherwise, it returns False:

fruits = ['apple', 'banana', 'cherry']
 
# is 'banana' in fruits?
print('banana' in fruits)   # True
 
# is 'orange' in fruits?
print('orange' in fruits)   # False



# MODYFING LISTS

# Let's say you're planning a trip to the grocery store, and you create a list of items you need to buy:

shopping_list = ['eggs', 'bread', 'apples', 'milk', 'cheese']

# Imagine your partner wants you to specifically buy green apples and asks you to update the list.
# To update the string 'apple', we first need to identify its index in the list.
# The thrid element 'apple' is at index 2 (remember, indices start from 0).

# If you don't want to manually find the index, you can also use the list.index() method to get the index:

shopping_list = ['eggs', 'bread', 'apples', 'milk', 'cheese']
 
# what's the index of 'apple'?
print(shopping_list.index('apples'))    # 2

# Once you identified the index, you can use it to update the corresponding element in the list.

shopping_list = ['eggs', 'bread', 'apples', 'milk', 'cheese']
shopping_list[2] = 'green apples'
print(shopping_list)    # ['eggs', 'bread', 'green apples', 'milk', 'cheese']

# Note that we did not create a new list with updated values. Instead, we directly modified the existing list.
# This is called mutability.
# Remember, in contrast, strings are immutable, meaning they cannot be changed.

# If you want to update a string, you have to create a new one with the updated values. For example:

text = 'abc'
 
print('New string: ', text.replace('a', 'xxxxx'))   # New string:  xxxxxbc
print('Old string is the same: ', text)     # Old string is the same:  abc

# Back to our shopping list example.

shopping_list = ['eggs', 'bread', 'apples', 'milk', 'cheese']

# Looking at your list, you realize that you should switch the order of eggs and bread because you will stop at the bakery first.
# We can use slicing to update a sequence of elements in the list.

shopping_list = ['eggs', 'bread', 'apples', 'milk', 'cheese']
 
# update first and second element
shopping_list[:2] = ['bread', 'eggs']
print(shopping_list)    # ['bread', 'eggs', 'apples', 'milk', 'cheese']

#Note that you don't have to assign the same number of elements again.

# For example here, instead of just replacing the first and second elements, we can also add an additional grocery item:

shopping_list = ['eggs', 'bread', 'apples', 'milk', 'cheese']
 
# update first and second element
shopping_list[:2] = ['bread', 'croissant', 'eggs']
print(shopping_list)    # ['bread', 'croissant', 'eggs', 'apples', 'milk', 'cheese']

# Now imagine you forgot to add chocolate to your list.
#You add an element to a list using the list.append(value) method:

shopping_list = ['bread', 'green apples', 'milk', 'eggs', 'cheese']
shopping_list.append('chocolate')
print(shopping_list)    # ['bread', 'green apples', 'milk', 'eggs', 'cheese', 'chocolate']

# To extend the list with multiple elements at once, use the list.extend(new_list) method:

shopping_list = ['bread', 'cheese']
shopping_list.extend(['chocolate', 'crisps'])
print(shopping_list)    # ['bread', 'cheese', 'chocolate', 'crisps']

# Now, you also want to add bananas to your shopping list. You want to place them next to the apples because you will find both in the fruit section of the supermarket.
# To add an element at a specific position, you can use the list.insert(index, value) method:

shopping_list = ['bread', 'green apples', 'milk', 'eggs', 'cheese']
 
# insert bananas at index 2
shopping_list.insert(2, 'bananas')
print(shopping_list)    # ['bread', 'green apples', 'bananas', 'milk', 'eggs', 'cheese']

# Then, you are in the store and have filled your cart with the first items on your list. And you want to keep your list up-to-date.
# There are two methods to remove elements from a list.
# list.remove(value) removes the first occurence of a specified value:
shopping_list = ['bread', 'bananas', 'milk', 'eggs', 'cheese']
 
# remove 'bananas'
shopping_list.remove('bananas') # <- but this removes only the first instance of "babanas" (if there was another "bananas" it would stay) 
 
print(shopping_list)    # ['bread', 'milk', 'eggs', 'cheese']


# list.pop(index) removes an element at a specified position:
shopping_list = ['bread', 'bananas', 'milk', 'eggs', 'cheese']
 
# remove element at index 2
shopping_list.pop(2)
 
print(shopping_list)    # ['bread', 'bananas', 'eggs', 'cheese']

# If you don't specify an index, the last element is removed:

shopping_list = ['bread', 'bananas', 'milk', 'eggs', 'cheese']
 
# remove last element
shopping_list.pop()
 
print(shopping_list)    # ['bread', 'bananas', 'milk', 'eggs']


# You can also remove elements from a list using slicing:

shopping_list = ['bread', 'bananas', 'milk', 'eggs', 'cheese']
 
# remove element at index 2 and 3
shopping_list[2:4] = []
 
print(shopping_list)    # ['bread', 'bananas', 'cheese']






