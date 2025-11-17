# FUNCTIONS

# In Python, you define a function using the def keyword, 
# followed by the function name, parentheses, and a colon. 
# The function body is then indented below.

def name():
	# function body
	print('Hi')
	
# After defining a function, we can call it using its name followed by a pair of parentheses.

# call the function
name()      # Hi

# The function body is only executed when the function is being called, 
# which is why, in the following example, the updated value of num is printed:

num = 0
def log_message():
   print(num)
 
num = 1
log_message()       # 1


# Another important aspect of functions is their ability to return values. 
# You can achieve this by using the return keyword.
# The value specified after the return keyword is passed back to 
# the caller of the function and can then be used for further operations:

def func():
   return 5
 
result = func()
print(result)       #5

# Note that if a return statement is encountered, the function immediately exits.
# Here, the print() function that follows the return statement is not executed:

def func():
  return 5
  print('I am not printed!')
 
print(func())       # 5

# You can use this approach to exit a function early if a certain condition is met. For example:

def func():
  if True:
    return 2
  return 5
 
print(func())   # 2

# So far, we've created very basic functions that consistently 
# perform the same task and return the same value when called. For example:

def square_of_two():
   return 2 * 2
 
print(square_of_two())      # 4

# square_of_two always returns the square of the value 2. 
# In programming jargon, we would say that the value 2 is hard-coded, meaning it does not change.

# To make the function more flexible, we can use function parameters. 
# Parameters enable the function to accept input values and use them within its body.
#For instance, rather than hard-coding the number 2, we can define a parameter x and pass 
# a different value whenever the function is invoked.

def square(x):
   return x * x

# This way we have a more flexible function that will return the square of 
# any number passed as input.

# To assign a value to parameter x, we must provide a value when calling the function. 
# These values passed to the function are referred to as arguments. For example:

square(5)

def square(x):
   return x * x
 
print(square(2))    # 4
print(square(5))    # 25
print(square(11))   # 121

# Functions can receive multiple arguments. To make them accessible, 
# you need to define multiple parameters when declaring the function.
# For example, here we declare the function subtract that defines two parameters x and y.

def subtract(x, y):
   return x - y

# When passing values to the function, you have two options:
# Either pass the values in the order of the defined parameters:

subtract(10, 5)

# Or assign the values to the parameter names:

subtract(y=5, x=10)

# As you can see, both approaches yield the same result:

def subtract(x, y):
   return x - y
 
print(subtract(10, 5))  # 5
print(subtract(y=5, x=10))  # 5

# Parameters can have any valid Python values such as integers or strings.
# You can specify default values when defining parameters:

def func(x='hello'):
   print(x)     # hi
                # hello
 
func('hi')
func()

# If we do not pass a value when calling the function, x is assigned the default value hello.


