# DICTIONARIES

#We have already learned how to store multiple values using a list. For example:
tasks = [1, 2, 3, 4, 5]

# But, lists are not the only way to store multiple values. Another data structure that can be used for this purpose are dictionaries.
# Let's create out first Python dictionary:

person = {
  'age': 30,
  'name': 'John',
  'gender': 'male'
}

# We have created a dictionary called person that stores data about John. The data is stored in so called key-value pairs.
# The keys in the dictionary are: 'age', 'name', and 'gender'.
# Each key is associated with a specific value.
# Just as with lists and tuples, the values in dictionaries can be of any type, such as strings, integers, or even other dictionaries.
# Dictionaries are defined using curly braces { } with pairs separated by commas. Keys and values are separated by colons :
# It doesn't matter whether you create a dictionary in a single line or multiple lines. The following are all valid dictionaries:

# single line:
{ 'age': 12, 'name': 'John' }
 
# multiple lines:
{
  'age': 15,
  'name': 'Alice'
}
# indentation doesn't matter:
{
  'age': 6,
'name': 'Bob'
}

# To access a value in a dictionary, you need the key associated with that value.
# Two methods can be used to retrieve a value from a dictionary using its key: either by using square brackets or by using the dict.get(key) method:

person = { 'age': 12, 'name': 'John' }
 
# get age using square brackets:
print(person['age'])    # 12
 
# get age using dict.get() method:
print(person.get('age'))    # 12

# So, why should you use a dictionary instead of a list or a tuple to store multiple values?
# Let's compare our dictionary to a list that stores the same values:

person = [12, 'John']
 
print(person[0])    # 12

# This works, but you need to remember that our person's age is stored at index 0.
# Additionally, the index may change when we new values are added to the list.
# If you have values associated with specific keys and require quick access to those values based on their keys, a dictionary is the ideal choice.
# Here are some examples:

employee = {
  'id': 12345,
  'name': 'Bob',
  'department': 'IT',
  'salary': 70000
}
 
inventory = {
  'apple': 10,
  'banana': 15,
  'orange': 20
}

# However, when you simply need to store a collection of data without associating each element with a unique key, you should use a list or a tuple.
# Some examples:
scores = [85, 90, 75, 85, 80]
 
daily_steps = (8420, 11280, 4528, 16090)

# Dictionaries, unlike lists and tuples, are not ordered.
# This means you cannot use an index to access a value.

person = { 'age': 12, 'name': 'John' }
 
# print(person[0]) # KeyError: 0

# Python throws the error: KeyError: 0 if we try to access a value at index 0.
# This is because Python tried to find the key 0 in our dictionary, but couldn't find it.
# Yes, integers are valid keys in dictionaries. Like in this example:

my_dict = {
  'str': 10,
  # integer as key
  10: 'str'
}
 
print(my_dict[10])  # str

# The 10 in my_dict[10] has nothing to do with index 10. Instead, it refers to the key 10.
# You can use any immutable data type as key in dictionaries. For instance:

my_dict = {
  # string as key
  'str': 10,
  # integer as key
  10: 11,
  # tuple as key
  (5,10): 99
}
 
print(my_dict['str'])   # 10
print(my_dict[10])      # 11
print(my_dict[(5,10)])  # 99

 # However, keys have to be unique. They can not be used more than once in the same dictionary.
 # Let's see what happens if we don't follow this rule:

my_dict = {
  'key': 10,
  # use key again
  'key': 99
}
 
print(my_dict)  # {'key': 99}

# As you can see, Python simply overwrites the first value.
# Values, on the other hand, don't have to be unique:

my_dict = {
  'a': 10,
  # use same value again
  'b': 10
}
 
print(my_dict) # {'a': 10, 'b': 10}


