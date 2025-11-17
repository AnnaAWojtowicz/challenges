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


