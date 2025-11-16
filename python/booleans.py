# PRINT(TYPE(STR))

# If you want to know the type of a specific value, you can use the built-in function type:

# text data
text = 'Hello World'
print(type(text))       # <class 'str'>
 
# whole number
num = 123
print(type(num))        # <class 'int'>



# BOOLEANS
# Booleans simply indicate if something is true or false.
# A Boolean can have only one of two possible values: True or False.
# Just like with integers or strings, you can assign a Boolean to a variable:

is_active = False

# print the type of is Active:
print(type(is_active))          # <class 'bool'>

# print the value of is Active:
print(is_active)            # False


#Comparing values also works with strings:
# Note that the comparison is case sensitive:
print('paris' == 'PARIS')           # False
 
print('Paris' == 'Paris')           # True

#Last but not least, you can even chain multiple Comparison Operators 
# together and combine them with other expressions.
# Here, we check if the sum of two numbers falls within the range of 0 to 10:

# is the sum of 2 and 5 in range?
print(0 < 2 + 5 < 10)           # True


# AND
# In Python, we can use the Logical Operator and to combine the 2 conditions:

is_favorite_color = True
is_within_budget = False
 
print(is_favorite_color and is_within_budget)       # False

# The result is False because and requires both conditions to be true.



# OR

# Another Logical Operator in Python is or. 
# or only requires one of the two conditions to be true.

# Let's what happens if we replace and with or:

is_favorite_color = True
is_within_budget = False
 
print(is_favorite_color or is_within_budget)        # True



# NOT

# The final Logical Operator in Python is not, which reverses the boolean value of an expression.

# For example, let's assume we have a traffic light. If the traffic light is not green, we must stop:

isGreen = False
 
mustStop = not isGreen
 
print(mustStop)         # True
# Here, isGreen is set to False, and we use not to reverse its value.


# You can even combine multiple Logical Operators. For example:

print(True and not False)       # True
# Here, we get True because not reverts False and both conditions are True.


#In Python, logical operators are evaluated from left to right. 
# The order of evaluation is determined by operator precedence, 
# with not having the highest precedence, followed by and, and then or.

# However, you can use parentheses to specify the order of evaluation explicitly, 
# making the code easier to read. For example:

print((True or False) and (True and False))     # False



