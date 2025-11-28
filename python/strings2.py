# escape characters

# Let's talk about special characters in Python strings.
# Imagine you want to represent the sentence She said, "It's a beautiful day!" in a Python string.
# If you try that, you'll notice that Python interprets the second single quote as the end of your string and doesn't know what to do with the rest of your sentence.
# 'She said, "It's a beautiful day!"'

# In this case, we'll need to use of an escape character.
# Escape characters in Python allow you to insert special characters into strings that would otherwise be difficult or impossible to type or display directly.
# An escape character is represented by a backslash \ followed by another character.
# The escape character we'll need in our example is \'.
# The escape character \' allows us to include a single quote inside a string without breaking it.
# Let's try it:
print('She said, "It\'s a beautiful day!"')     # She said, "It's a beautiful day!"

# Great! Now, we can represent complex dialogues in Python strings.
# Instead of single quotes, you can also escape double quotes with \".
# This is useful if you prefer to enclose your strings with double quotes. For example:
print("She said, \"It's a beautiful day!\"")        # She said, "It's a beautiful day!"

# Another commonly used escape character is the newline character \n.
# As the name suggests, it inserts a new line within the string. For example:
print("Hi, how are you?\nI'm great!")

# Hi, how are you?
# I'm great!


#  But, what if you want to display a literal backslash \ in your string?
# Since the backslash is reserved for escape characters in Python, you need to escape it by using a double backslash \\:
print("Here's a backslash: \\")     #  Here's a backslash: \

# If you need to display a special character in a Python string and are unsure how, there's likely an escape character for it.

# EXERCISE
# The string below is not recognized by Python due to unescaped single and double quotes. Use escape characters to correctly display the dialogue.

# adjust the following line...
message = 'John said, "I can\'t believe it! It\'s finally happening!"'
 
print(message)
# expected: John said, "I can't believe it! It's finally happening!"



# EXERCISE

# The code below prints a list of ingredients on a single line. Use the newline escape character to format the list correctly into multiple lines. Add \n where needed to match the expected output.
ingredients = ['Spaghetti', 'Eggs', 'Parmesan Cheese', 'Bacon', 'Black Pepper']
message = 'Ingredients:'
 
for ingredient in ingredients:
  # adjust the following line...
  message += '\n- ' + ingredient
 
print(message)
 
#### expected: ####
# Ingredients:
# - Spaghetti
# - Eggs
# - Parmesan Cheese
# - Bacon
# - Black Pepper
 


#  string method str.split()

# Let's talk about the Python string method str.split().
# As the name suggests, it's used to split an existing string into multiple smaller strings.
# Here's a simple example:
text = 'hello world'
print(text.split())     # ['hello', 'world']

# As you can see, the original string is split by the whitespace character, and the resulting substrings are returned in a list.
# This is the default behavior of the str.split() method.
# You can also define the delimiter used to split the string by passing a custom separator as argument.
# str.split(separator)
# Let's split the string at the character o:
text = 'hello world'
print(text.split('o'))      # ['hell', ' w', 'rld']

# This time, we receive a list of three strings because the character o appears twice in the original string, causing it to split at both occurrences.
# Notice that the whitespace before the w is preserved.
# Only the character o has been removed, as it was the delimiter used for splitting the string.
# An example use case for str.split() is to break a text into individual words or sentences.

# extra examples:
text = 'a-b-c-d'
print(text.split('-'))      # ['a','b','c','d']


text = 'ab cd'
print(text.split())     # ['ab','cd']


text = 'a b c d'
print(text.split('b'))      # ['a ',' c d']


# Another characteristic of str.split() is that if you specify a separator that doesn't exist in the original string, the result will be a list containing the entire string as a single element.
# For example, here we try to split a string using the non-existing character Z:
text = 'programming'
print(text.split('Z'))      # ['programming']

# However, let's see what happens when we split the text at the letter m, which appears twice in a row:
text = 'programming'
print(text.split('m'))      # ['progra', '', 'ing']

# Since the function splits the original string at each occurence of the separator, we get three substrings. Because there's nothing between the two ms, one of the substrings is an empty string.

# extra examples:

text = 'abcd'
print(text.split('e'))      # ['abcd']

text = 'brilliant'
print(text.split('l'))      # ['bri', '', 'iant']


# Last but not least, str.split() has a second optional parameter called maxsplit:
# str.plit(separator, maxsplit)
# You can use it to determine the maximum number of split.
# By default, there's no limit, so the string splits at every occurrence of the separator.
# For example, here we limit the number of splits to 2, even though the separator - appears more than twice:
text = '1-2-3-4'
print(text.split('-', 2))       # ['1', '2', '3-4']

# extra examples:

text = 'brilliant'
print(text.split('i', 1))       # ['br', 'lliant']


# EXERCISES:

# Split the text variable using the appropriate separator to get a list containing four numbers.
text = 'one?two?three?four'
# complete the following line...
words = text.split("?")
print(words)
# expected: ['one', 'two', 'three', 'four']


# Extract the domain (example.com) from the email below. Use str.split() to divide the email at the appropriate position, and then use string indexing to select the domain part.
email = 'john@example.com' 
# complete the following line...
domain = email.split("@")
domain = domain[1]
# or: domain = email.split("@")[1]
print(domain)
# expected: example.com


# Complete the function counter to return the number of words in a given string.
# complete the following function...
def counter(text):
  words = text.split()
  return len(words)
 
print(counter('Python is a powerful programming language.'))
# expected: 6
print(counter('Learning new skills can be both challenging and rewarding.'))
# expected: 9


# Write a function called find_longest that returns the longest word from a given sentence.
# create function find_longest here...
def find_longest(str):
	longest = ""
	words = str.split()
	for word in words:
		if len(word) > len(longest):
			longest = word
	return longest
 
print(find_longest('To be or not to be.'))
# expected: 'not'
print(find_longest('The best way to predict the future is to invent it.'))
# expected: 'predict'



#  f-strings

# Sometimes, we need to create a string that includes information stored in variables. In this example, we use the + operator to achieve this.
name = 'Jane'
print('Hello, ' +  name +  '!')     # Hello, Jane!

# This works, but it can be a bit verbose.
# A more convenient and elegant way to embed variables into strings is using so called formatted string literals, or simply f-strings.
# Here's the same example, but this time we use an f-string instead of the + operator:
name = 'Jane'
print(f'Hello, {name}!')        # Hello, Jane!

# To create an f-string, simply add an f before the quotation mark of your string.
# To embed the value of a variable into the string, use curly braces {}.
# F-strings are are not only easier to read but also offer other useful features.
# One of these is automatic type conversion.
# Consider the following example.

#age = 43
#print('Jane is ' +  age +  ' years old.')      # TypeError: can only concatenate str (not "int") to str

# The code throws an error because the variable age is not a string. The + operator can only concatenate strings.
# In order to make this work, we need to convert age to a string before combining it with other strings.
# To do this, we can use the str() function. It converts the integer 43 into the string '43':
age = 43
print('Jane is ' +  str(age) +  ' years old.')      # Jane is 43 years old.

# Again, this approach can be a bit tedious. 
# An f-string simplifies this by automatically converting the type of our variable:
age = 43
print(f'Jane is {age} years old.')      # Jane is 43 years old.

# F-string are not limited to embedding variables. You can embed any Python expression.
# Here, the f-string includes a mathematical expression:
print(f'10 times 12 is {10 * 12}.')     # 10 times 12 is 120.

# You can even call a function within an f-string:
def add(a, b):
  return a + b
 
print(f'10 plus 12 is {add(10,12)}.')       # 10 plus 12 is 22.


# extra examples:

print('3 times 3 is {3 * 3}')       # 3 times 3 is {3 * 3}

print(f'3 times 3 is {3 * 3}')      # 3 times 3 is 9




# EXERCISES:

# Transform the message string into an f-string. Include the variables name and age in the message string.
name = 'Alice'
age = 30
  
# complete code here...
message = f'Hello, my name is {name} and I am {age} years old.'
 
print(message)
# expected: 'Hello, my name is Alice and I am 30 years old.'



# Transform the message string into an f-string and embed the necessary variables and Python expressions.
product = 'Laptop'
price = 999
quantity = 3
 
# Complete the following line...
message = f'Product: {product}, Price: {price}, Quantity: {quantity}, Total: {price * quantity}'
 
print(message)
# expected: 'Product: Laptop, Price: 999, Quantity: 3, Total: 2997'


# 
# # 
#

#
#