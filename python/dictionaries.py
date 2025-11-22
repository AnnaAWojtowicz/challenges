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



 
