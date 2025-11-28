# Assigning Multiple Variables with Unpacking
# In this lesson, you'll learn how to assign multiple variables at once using unpacking. We'll demonstrate how you can extract values from various iterables like strings and lists and assign these values to multiple variables.

#So far, if we wanted to create multiple variables, we had to do this in multiple lines of code, like this:
x = 10
y = 20
z = 30

# But there's a more efficient way to do this!
# It's called unpacking. Unpacking is the process of extracting values from an iterable (like a list or tuple) and assigning them to multiple variables in a single statement.
# Let's see how this works:
coordinates = (10, 20, 30)
x, y, z = coordinates
print(x, y, z)      # 10 20 30

# We start with a tuple called coordinates, which contains 3 values. Then, we unpack each value from coordinates and assign them to the variables x, y, and z.
# We can shorten this even further into a single line of code:
x, y, z = (10, 20, 30)
print(x, y, z)      # 10, 20, 30

# Now, we are creating and assigning the variables all in one line.
# If you want to, you can even skip the parentheses of the tuple when assigning multiple variables, like this:
x, y, z = 10, 20, 30
print(x, y, z)      # 10, 20, 30

# In this case, Python implicitly treats the values 10, 20, and 30 as a tuple, allowing us to assign them directly to the variables.
# As you can see, with this unpacking technique, we have transformed our original multiline assignment into a more efficient one-liner:
# individual assignments
x = 10
y = 20
z = 30
 
# assignments with unpacking
x, y, z = 10, 20, 30

# extra examples: 

data = (1, 2)
a, b = data
print(b)    # 2

data = (1, 2)
b = data
print(b)    # (1, 2)

a, b = 1, 2
print(a)    # 1

# One thing to keep in mind when using this unpacking technique is that the number of variables must match the number of values being unpacked.
# For example, here we attempt to unpack a tuple with 3 values and assign them to only 2 variables:
# x, y = 10, 20, 30     # ValueError: too many values to unpack (expected 2)
# As you can see, we run into an error.

# An error is also triggered if your tuple contains fewer values than the number of variables you want to assign:
# x, y, z = 10, 20      # ValueError: not enough values to unpack (expected 3, got 2)

# So far, we've only been unpacking tuples, whether explicitly with parentheses or implicitly without them.
# But unpacking isn't limited to tuples—you can unpack all iterables in Python.
# An iterable is any Python object that can be iterated over, for example in a loop.
# Here are some examples of unpacking other types of iterables:
# unpacking a list
x, y, z = [10, 20, 30]
print(x, y, z) # 10, 20, 30
 
# unpacking a string
a, b, c, d, e = 'hello'
print(a, b, c, d, e) # h, e, l, l, o
 
# unpacking dictionary keys
k1, k2 = {'a': 1, 'b': 2}
print(k1, k2) # a, b
 
# unpacking dictionary values
v1, v2 = {'a': 1, 'b': 2}.values()
print(v1, v2) # 1, 2


# extra examples:

a, b = 'start', 'end'
a, b = b, a
print(a)        # end

a, b = 'hi'
print(b, a)       # i h

# a, b, c = 'code'
# print(c, b, a)    # ValueError: too many values to unpack (expected 3)



# EXERCISES:

# Here, we have a tuple containing personal information. Use unpacking to extract the values from the tuple and assign them to variables named name, age, and job.
data = ('John', 25, 'Developer')
# add your code here...
name, age, job = data

print(name) # expected: John
print(age) # expected: 25
print(job) # expected: Developer


# Use unpacking to swap the values of the variables one and two.
one = 1
two = 2
# add your code here...
one, two = two, one
 
print(one) # expected: 2
print(two) # expected: 1


#  The following code contains a mistake. Can you figure out how to extract the first name and last name in one line of code using unpacking? Hint: you'll need to use a string method to transform the string into a list containing two smaller strings.
name = 'Alice Johnson'
 
# adjust the following line of code
name_list= name.split()
first, last = name_list
 
print(first) # expected: Alice
print(last) # expected: Johnson




# Ignoring Values While Unpacking and the * Operator
# When unpacking values from an iterable, you might want to extract only certain values and ignore others or you might want to capture and combine a subset of the values. In this lesson, you'll learn to do so using the _ placeholder and the * operator.
# We've learned that unpacking is the process of extracting values from an iterable (like a list or tuple) and assigning them to multiple variables in a single statement, as shown below:
x, y, z = 10, 20, 30

# But now imagine we're only interested in the x and the z variable.
# In that case, we would have a variable y in our program that is never used.
# While this won't throw an error, it could confuse other developers reading your code, as it may not be obvious that y is irrelevant.
# To make it clearer that a value should be ignored, it is common practice to assign it to the character _:
x, _, z = (10, 20, 30)
print(x, z)     # 10 30
# This way, anyone reading your code knows that the middle value should be ignored.
# However, keep in mind that this is just a convenient syntax. Under the hood, you are simply creating a new variable called _:
x, _, z = (10, 20, 30)
print(_)    # 20

# It doesn't have to be the middle value; you can choose any value to ignore:
x, y, _ = (10, 20, 30)
print(x, y) # outcome: 10 20
 
_, y, z = (10, 20, 30)
print(y, z) # outcome: 20 30
 
x, _, _ = (10, 20, 30)
print(x) # outcome: 10



# extra examples:

_, b, c, d = [1, 2, 3, 4]
print(b, c, d)      # 2 3 4

a, _, b, _, c = 'coder'
print(a, b, c)      # c d r

# a, b, c, _ = (10, 20, 30)
#print(a, b, c)      # ValueError: not enough values to unpack (expected 4, got 3)


# Now consider the following tuple containing user data:
data = ('John Doe', 30, 'Engineer', 'NY', 'profile_picture.png')
# Let's say we want to extract the name and age from the tuple and aggregate the remaining values into a more general user_info list.
#  We can achieve this using the * operator:
data = ('John Doe', 30, 'Engineer', 'NY', 'profile_picture.png')
 
name, age, *user_info = data
 
print(f'{name} is {age} years old.')    # John Doe is 30 years old.
print(user_info)        # ['Engineer', 'NY', 'profile_picture.png']

# Here, we have assigned the first two values of data to the variables name and age. The * before the user_info variable instructs Python to pack all the remaining values into a list, which is then assigned to user_info.
# The values that are aggregated depend on the number and position of the other variables.
# For example, here we extract the name and the profile picture URL individually and assign the aggregated middle values to user_info:
data = ('John Doe', 30, 'Engineer', 'NY', 'profile_picture.png')
 
name, *user_info, picture = data
 
print(name)     # John Doe
print(picture)  # profile_picture.png
print(user_info)    # [30, 'Engineer', 'NY']

# If you use the asterisk operator when there are no remaining values, it will assign an empty list:
a, *b, c
print(a, b, c)      # 1 [] 2


# extra examples:

a, b, *c = 'coder'
print(a, b, c)  # c o ['d', 'e', 'r']

*a, b = (1, 2, 3, 4)
print(b)        # 4

a, b, c, *d = (1, 2, 3, 4)
print(d)    # [4]

a, b, *c = 1, 2
print(c)    # []

# Great! Last but not least, you can also combine the _ placeholder with the * operator.
# This is helpful if you want to ignore multiple values while unpacking.
# Consider the following example where we unpack only the first two values of data:
data = (1, 2, 3, 4, 5, 6)
first, second, _, _, _, _ = data

# This can be done more efficiently by using the * operator.
# In this example, we ignore all the remaining values at once without needing to match the exact number of values in data:
data = (1, 2, 3, 4, 5, 6)
first, second, *_ = data
print(first, second)    # 1 2


# extra examples:
*_, b = (1, 2, 3, 4)
print(b)        # 4

*a, _ = (1, 2, 3, 4)
print(a)        # [1, 2, 3]



# 
# 
# 
#  
#  #