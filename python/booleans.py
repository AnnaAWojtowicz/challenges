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