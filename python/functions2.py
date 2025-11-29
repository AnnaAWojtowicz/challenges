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

# Even after calling the function, the variable text still holds its original value.
# It seems like nothing changed, even though we assigned a new value to text inside the function.
# To understand what happened here, you need to know that we are dealing with two so-called scopes.
# A scope describes a region of code from which you can access certain variables or functions.
# When we first created the variable text, we were creating it in the global scope.
##### global scope #####
text = 'Hello World' # global variable
print(text)     # Hello world

# The global scope is the outermost scope in your program. Whenever you create a variable outside a function (or a class), you are defining a global variable within the global scope. 
# However, when you create a function, the code inside the function has its own scope, known as local scope.

#### global scope ####
...
 
def my_function():
  #### local scope ####
  ...


# You can access all global variables inside the local scope of a function. For example:

#### global scope ####
my_num = 10
 
def my_function():
  #### local scope ####
  print(my_num) # local variable    # 10
 
my_function()


# However, when we create a variable inside the function, we're defining a so-called local variable that can only be accessed in the local scope of that function.
# For example, here we create a local variable my_num inside the local scope of my_function. When we try to access that variable outside the function, we run into an error:
def my_function():
  #### local scope ####
  my_num = 10 # local variable
 
#### global scope ####
my_function()
 
#print(my_num)   # NameError: name 'my_num' is not defined



# 
# 
# 
# 
# 
# 
# 
# 
# #