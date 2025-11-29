# Introduction to Global and Local Scope

# In this lesson, you'll learn about about the concept of global and local scopes, how to access and modify global variables inside a function, and how to use the global keyword in Python.

# We have already learnt that variables store values for later use. To access the stored value, we just have to call a variable somewhere below in our code. For example:
text = 'Hello World'
print(text)

# We can even access that variable from within a function. Let's try it:
text = 'Hello World'
def my_function():
  print(text)       # Hello World
 
my_function()

# However, the rules change slightly when we want to modify the variable inside the function.
# Let's see what happens if we try to:
text = 'Hello World'
 
def my_function():
  text = 'Python'
 
my_function()
print(text)     # Hello World
# 
# 
# 
# #