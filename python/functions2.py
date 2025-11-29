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



# Back to our original example and to why the value of text does not change:
text = 'Hello World'
 
def my_function():
  text = 'Python'
 
my_function()
print(text)     # Hello World

# The reason is that we have actually created 2 versions of text: one in the global scope and another that exists only within the scope of my_function.
# Here, you can see that the string Python is only assigned to the local version of text, while the global version remains unchanged before and after we call my_function:

#### global scope ####
text = 'Hello World'
print(f"Global scope: '{text}'")    # Global scope: 'Hello World'
 
def my_function():
  #### local scope ####
  text = 'Python'
  print(f"Local scope: '{text}'")   # Local scope: 'Python'
 
#### global scope ####
my_function()
print(f"Global scope: '{text}'")    # Global scope: 'Hello World'

# To tell Python that you want to modify a global variable inside a function instead of creating a new one with the same name, you can use the global keyword.
# You can use the global keyword to declare a variable as global within a local scope:

def my_function():
  #### local scope ####
  # declare my_var as global
  global my_var

# This allows my_var to be accessed and modified globally.
# So, to modify the global variable text from our example, we need to declare it as global inside my_function:

#### global scope ####
text = 'Hello World'
print(f"Global scope: '{text}'")    # Global scope: 'Hello World'
 
def my_function():
  #### local scope ####
  # declare text as global:
  global text
  text = 'Python'
  print(f"Local scope: '{text}'")   # Local scope: 'Python'
 
#### global scope ####
my_function()
print(f"Global scope: '{text}'")    # Global scope: 'Python'

# Now, we have successfully modified text from within the scope of my_function.
# Using the global keyword, you can not only modify global variables from within local scopes, but also create new ones.
# For example, in the code below, we create a new global variable inside my_function and access it outside the function's scope:
def my_function():
  global num
  num = 10
 
my_function()
print(num)      # 10

# Be aware that the variable is only created when you call the function.
# It will not work if you try to access num before calling my_function:
def my_function():
  global num
  num = 10
 
#print(num)     # NameError: name 'num' is not defined
my_function()



# extra examples:

price = 10
def func():
  quantity = 2
  print(price * quantity)   # 20

func()



price = 10
def func():
  quantity = 2
 
func()
# print(price * quantity)     # NameError: name 'quantity' is not defined


price = 10
def func():
  price = 5
  print(price)      # 5
 
func()
print(price)        # 10



price = 10
def func():
  price = 5
  print(price)      # 5
 
print(price)        # 10
func()

# BUT! since this is before calling the function: print(price) # 10, this will be printed first



price = 10
def func():
  price = 5
 
print(price)
func()
print(price)
# 10 10



price = 10
def func():
  global price
  price = 5
 
print(price)
func()
print(price)
# 10 5


# EXERCISES:

# Adjust the code below so that it correctly prints the value of the local variable num.
def my_function():
   num = 100
   print(num)

my_function()
# expected output: 100


# Adjust the increment function so that it modifies the global variable counter. Every time you call increment, it should increment counter by 1.
counter = 0
 
def increment():
   global counter
   counter += 1

increment()
print(counter) # expected: 1
 
increment()
print(counter) # expected: 2



# Adjust the create_var function to create a global variable called my_var and assign a value to it.
def create_var():
   global my_var
   my_var = "a"
 
create_var()
print(my_var)



# Learn how to create and correctly call nested/inner functions.

# We've already learnt that functions have their own scope, the local scope.

#### global scope ####
...
 
def my_function():
  #### local scope ####
  ...



#  You can use the local scope to create variables that are accessible only within the function.

#### global scope ####
...
def my_function():
  #### local scope ####
  local_var = 10

# This is not limited to just variables.
# You can also create another function inside your function.
# In this example, we create a function called inner that is nested inside a function called outer:
def outer():
  #### nested function ####
  def inner():
    print('hi')

# When using nested functions, the same rules for global and local scope apply.
# Since inner is defined inside the local scope of outer, it cannot be called from outside of outer. If we try to do so, we will encounter an error:
def outer():
  #### nested function ####
  def inner():
    print('hi')
 
# inner()       # NameError: name 'inner' is not defined


# To execute a nested function, you must call it from within the outer function. After that, you call the outer function to run everything:
def outer():
  #### nested function ####
  def inner():
    print('hi')
  inner()
 
outer()     # Hi


# extra examples:

def outer():
  def inner():
    print('Hello World')
 
outer()     # (nothing is being printed since inner function is never called)



def outer():
  def inner():
    print('Hello World')
 
# inner()       # NameError: name 'inner' is not defined



def outer():
  def inner():
    print('Hello World')
  inner()
 
outer()     # Hello World


# Remember that you can use the global keyword to declare a variable as global within a local scope:
def my_function():
  global my_var
  my_var = 10

# This is only limited to variables and does not work for nested functions. Let's see what happens if we try:
def outer():
  global inner
  def inner():
    print('hi')
 
# inner()         # NameError: name 'inner' is not defined


# ERECISES:

# The following code contains a mistake. Fix it so the nested function is called correctly, and the message Hello World is displayed.
def outer_func():
  def print_msg():
    print('Hello World')
  print_msg()
outer_func()
# expected output: 'Hello World'



# The following code contains a mistake. Fix it so the nested function is called correctly, and the message Hello from inner_func is displayed.
def outer_func():
  def inner_func():
    print('Hello from inner_func')
  inner_func()
outer_func()
# expected output: 'Hello from inner_func'



# In the code below, my_func repeatedly calls the function inner. However, that function hasn't been created yet. Define the inner function and make it print a message each time it's called.
def my_func():
  def inner():
    print("Hi")
  for _ in range(5):
    inner()
my_func()




# In the code below, my_func repeatedly calls inner_func. Although the code runs without any issues, inner_func is currently defined as a global function. Adjust the code so that inner_func is nested inside my_func.
def my_func():
    def inner_func():
        print('Hello World')
    for _ in range(3):
        inner_func()
my_func()



# Learn about the enclosing scope, which allows nested functions to access variables defined in their outer (enclosing) function.
# We've already learnt that functions can access variables defined in their own local scope, as well as in the global scope.

#### global scope ####
...
 
def my_function():
  #### local scope ####
  ...


# When we are dealing with nested functions, there's an additional type of scope: the so-called enclosing scope.
# The enclosing scope refers to the region where the outer function's variables are accessible by the inner (nested) function.
# Even though the inner function has its own scope, it can still access variables from the outer function.
# From the perspective of the inner function, there are 3 different scopes:

#### global scope ####
...
 
def outer():
  #### enclosing scope ####
  ...
  def inner():
    #### local scope ####
    ...
#### global scope ####
...
 

# That means the inner function can access variables defined in the global scope...

#### global scope ####
global_var = 'global'
 
def outer():
  #### enclosing scope ####
  def inner():
    #### local scope ####
    print(global_var)           # global
  inner()
 
outer()


# And variables defined in the enclosing scope...

#### global scope ####
 
def outer():
  #### enclosing scope ####
  enclosing_var = 'enclosing'
  def inner():
    #### local scope ####
    print(enclosing_var)        # enclosing
  inner()
 
outer()


# And variables defined in its own local scope...

#### global scope ####
 
def outer():
  #### enclosing scope ####
  def inner():
    local_var = 'local'
    #### local scope ####
    print(local_var)        # local
  inner()
 
outer()


# In Python, the way variables are looked up follows a specific order, or hierarchy.
# This hierarchy determines where Python starts looking for variable names.
# The order goes from inside to outside:
# Local Scope > Enclosing Scope > Global Scope
# This order is important when multiple variables with the same name exist in different scopes.
# For example, in this case, the local version of x takes precedence over the others:
x = 'global'
 
def outer():
  x = 'enclosing'
 
  def inner():
    x = 'local'
    print(x)
 
  inner()
 
outer()

# local




# If there's no local version of x, the enclosing version takes precedence over the global one:
x = 'global'
 
def outer():
  x = 'enclosing'
 
  def inner():
    print(x)
 
  inner()
 
outer()

# enclosing



# extra examples:

x = 10
def outer():
  y = 20
  def inner():
    z = 30
    print(x, y, z)
  inner()
 
outer()
# 10 20 30


x = 10
def outer():
  x = 20
  def inner():
    x = 30
    print(x)
  inner()
 
outer()
# 30


x = 10
def outer():
  x = 20
  def inner():
    x = 30
  print(x)
  inner()
 
outer()
# 20    <- because print is before the inner finction is being called



x = 10
def outer():
  x = 20
  def inner():
    x = 30
  inner()
print(x)
 
outer()
# 10



x = 10
def outer():
  x = 20
  def inner():
    print(x)
  inner()
 
outer()
# 20



# EXERCISES: 

# In this exercise, the function outer returns the result of inner. x within inner from the enclosing function and multiply it with the local variable y.
def outer():
  x = 3
  def inner():
    y = 2
    result = x * y
    return result 
  return inner()
 
print(outer()) # output: 6



# In this exercise, the function outer returns the result of inner. Modify inner so that outer returns the expected result.
def outer(x):
  def inner():
    y = 2
    return x * y
  
  return inner()
 
print(outer(99)) # output: 198
print(outer(3)) # output: 6



#  Print the value of all three versions of x.
x = 10
def outer():
  x = 20
  def inner():
    x = 30
    print(x)    # 30
  inner()
  print(x)      # 20
print(x)        # 10
outer()
# but it gets printed in this order: 10 30 20



# Introduction to Closures
# Learn how to return functions from other functions and use this technique to create closures. Discover what closures are and how they can be used to create function factories and a kind of 'protected memory'.
# Let's begin with a simple example of a function nested inside another function.
def outer_function(message):
  def inner_function():
    print(message)
  inner_function()
 
outer_function('Hello')     # Hello

# outer_function takes the message paramter and defines a nested function called inner_function, which it immediately executes.
# The inner_function prints the value of message, which it can access through the enclosing scope of outer_function.
# I know it seems a bit overly complicated to use all this code just to print a simple message.
# Things get interesting when the outer_function doesn't just execute the inner_function, but instead returns it:
def outer_function(message):
  def inner_function():
    print(message)
  #### returning the nested function ####
  return inner_function

# Now we can assign the nested function to a new variable and execute it outside outer_function:
def outer_function(message):
  def inner_function():
    print(message)
  #### returning the nested function ####
  return inner_function
 
#### Storing the nested function in a new variable
greet = outer_function('Hello')
 
#### Calling the nested function ####
greet()     # Hello


# In this way, you could say that the nested function has "escaped" the outer_function.
# The key takeaway is that it still retains access to the original value of message from its enclosing scope even though outer_function has finished executing.
# This is what's called a closure.
# A closure is created when a nested function "remembers" the variables from its enclosing scope even after the outer function has finished executing.
# This means the inner function can still access and use those variables.
# In our example, we can now create different versions of the inner_function by passing different values to the outer_function:
def outer_function(message):
  def inner_function():
    print(message)
  return inner_function
 
#### create different versions of inner_function ####
greet = outer_function('Hello')
farewell = outer_function('Goodbye')
 
greet()     # Hello
farewell()  # Goodbye

# Now, we've used the outer_function as a function factory.
# A function factory is a function that produces other functions, allowing you to create specialized behavior based on input parameters.


# extra examples: 

def outer(x):
  y = 5
  def inner():
    print(x * y)
  return inner
 
func = outer(100)
func()      # 500



def outer(x):
  y = 5
  def inner():
    x = 10
    print(x * y)
  return inner
 
func = outer(100)
func()      # 50



# Function factories are just one of many use cases for closures.
# You can also use closures to manage a state that you want to keep hidden from the outside world.
# For example, here we create a create_counter function that manages the state of a count variable:
def create_counter():
  count = 0 # Protected state
 
  def increment():
    nonlocal count # Access the enclosing function's variable
    count += 1
    print(count)
  return increment
 
my_counter = create_counter()
 
my_counter()    # 1
my_counter()    # 2
my_counter()    # 3
# 1 2 3

# The nonlocal keyword allows the inner function to modify the count variable from the enclosing create_counter function.
# The moment we execute the create_counter function, we create a new instance of the count variable.
# This value is not directly accessible to us. It can only be modified by the nested function increment. 
# However, this nested function is available to use because the outer function returned it, and we assigned it to the my_counter variable.
# Be executing my_counter, we can indirectly modify the count.


# extra examples:

def create_counter():
  count = 0
  def increment():
    nonlocal count
    count += 1
    print(count)
  return increment
 
func = create_counter()
 
#print(count)   # NameError: name 'count' is not defined.


def create_counter():
  count = 0
  def increment():
    nonlocal count
    count += 2
    print(count)
  return increment
 
func = create_counter()
func()  # 2
func()  # 4
func()  # 6


# !!! SUPER IMPORTANT EXAMPLE!!!
def create_counter():
  count = 0
  def increment():
    nonlocal count
    count += 1
    print(count)
  return increment
 
func1 = create_counter()
func2 = create_counter()
func1()     # 1
func2()     # 1
func1()     # 2
func2()     # 2



def create_counter(step):
  count = 0
  def increment():
    nonlocal count
    count += step
    print(count)
  return increment
 
func = create_counter(5)
func()      # 5
func()      # 10



def create_counter(step):
  count = 0
  def increment():
    nonlocal count
    count += step
    print(count)
  return increment
 
func1 = create_counter(5)
func2 = create_counter(2)
func1()     # 5
func1()     # 10
func2()     # 2
func2()     # 4


# !!! ANOTHER IMPORTANT ONE!!!
def create_counter():
  count = 0
  def increment(step):
    nonlocal count
    count += step
    print(count)
  return increment
 
func = create_counter()
 
func(1)     # 1
func(2)     # 3
func(3)     # 6



# The function secret_keeper holds a secret that is only revealed by its inner function reveal. In other words, we are creating a closure. However, there's a small error. Fix the mistake to turn the code into a fully working closure.
def secret_keeper():
  secret = '🤫🎁'
  def reveal():
    return secret 
  return reveal
  
get_secret = secret_keeper() 
print(get_secret()) # expected: 🤫🎁



# We've created a counter using a closure. Adjust the code so that the print statement outputs True.
def create_counter():
  count = 0
  def increment():
    nonlocal count
    count += 1
    return count
  return increment
 
count = create_counter()
 
count() # count == 1
count() # count == 2
 
print(count() == 3) # output: True

