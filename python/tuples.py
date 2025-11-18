# TUPLES

# Let's create our first tuple:

my_tuple = ('Evan', 2, False)
 
print(my_tuple)     # ('Evan', 2, False)

# Looks almost like a list don't you think?
my_tuple = ('Evan', 2, False)       # ('Evan', 2, False)
my_list = ['Evan', 2, False]        # ['Evan', 2, False]
 
print(my_tuple, my_list)

# So, besides the parentheses and square brackets, what's the difference?
# Tuples are immutable, meaning their elements cannot be changed after creation. Lists, on the other hand, are mutable.
# Let's see what happens if we try to update a tuple like we did with a list:

my_tuple = ('Evan', 2, False)
 
# attempt to change element at index 1
my_tuple[1] = 99
 
print(my_tuple)     # TypeError: 'tuple' object does not support item assignment

# Other than that, tauples are pretty similar to lists.
# You can access tuple elements using indices and slicing:
my_tuple = (1, 2, 3, 4, 5)
# print first and last element
print(my_tuple[0], my_tuple[-1])    # 1, 5
# print second and third element
print(my_tuple[1:3])        # (2,3)


# You can get the index of an element:
my_tuple = (1, 2, 3, 4, 5)
# print index of first occurrence of 3
print(my_tuple.index(3))        # 2


# You can get the length of a tuple:
my_tuple = (1, 2, 3, 4, 5)
# print length of tuple
print(len(my_tuple))    # 5


# But, why should you use tuples?
# First of all, the immutability of tuples can be advantageous.
# If you have a collection of constant elements that never change, it's better to use a tuple to store them. This way, you cannot accidently change the values.
# Using tuples for constant values also improves the readability of your code. When you encounter a tuple, you can be certain that its values remain unchanged.
# Most importantly, tuples improve the performance of your code. Due to their immutability, they use less memory and accessing tuple elements is generally faster than accessing list elements.
# That's why, whenever you have a collection of constant elements, store them in a tuple instead of a list.

