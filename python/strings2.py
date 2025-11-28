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



# 
#   # 
#

#
#