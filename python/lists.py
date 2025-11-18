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


