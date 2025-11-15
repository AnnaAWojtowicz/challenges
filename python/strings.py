# As you can see, our final string is missing some spaces. Let's add them:
a = 'Code'
b = 'for'
c = 'fun'
 
text = a + ' ' + b + ' ' + c
print(text)

#Code for fun

#However, adding spaces like this is a bit cumbersome. 
# There's a more efficient way to do this using the join method: 
# 'separator'.join([a,b,c...])

#With the join method, we can specify a separator that separates the strings 
# that we put inside the square brackets. In our case it is an empty space:

a = 'Code'
b = 'for'
c = 'fun'
 
text = ' '.join([a,b,c])
print(text)

#ode for fun

#We can also specify a different separator:

a = 'Code'
b = 'for'
c = 'fun'
 
text = '+'.join([a,b,c])
print(text)

#Code+for+fun



#INDEX

# Note that each character in the string has its own index, including whitespaces. 
# Therefore, text[5] is just a blank space.

text = 'Hello World'
print(text[5])

# 

#We can also extract a range of characters from a string using the so called 
# slice syntax 'string'[start:end]. For example:

text = "Hello World"
print(text[1:3])

# el

#So, what happened here? By executing text[1:3], we extracted a range of text 
# starting from index 1 (included) to index 3 (excluded).

# When using the slice syntax 'string'[start:end], the start index has a default value of 0.
# Hence, if we do not include a number before the colon, 
# the extracted range starts at index 0. For example:

text = "Hello World"
print(text[:5])

#Hello

#The default value of the end index always equals the number of characters of the entire string, 
# in other words the index of the last character plus 1.
#Hence, if we do not include a number after the colon, 
# the extracted range ends with the last character. For example:

text = "Hello World"
print(text[3:])

#lo World


#If we don't include a start or end index, we get a copy of the entire string:

text = "Hello World"
print(text[:])

#Hello World


#Last but not least, you can also include negative numbers when working with indexes. 
# Negative numbers allow you to start counting from the end of a string.
#For example, with -1 you can extract the last character of a string:

text = "Hello World"
print(text[-1])

#d


#This also works with the slice syntax:

text = "Hello World"
print(text[-5:-1])

#Worl   <- without "d" because :-1 is exclusive!!!




# STRING METHODS

#Another helpful string method is str.find(). <- only the first one!!!

text = 'Hello World'
print(text.find('o'))
# 4 <- but not 4, 7


# It is used to locate the position of a single character or a sequence of characters 
# within a string.

#Here, we use the str.find() method to locate the position of the word 'the':

text = 'Without comments, the code becomes unreadable.'
print(text.find('the'))

#18

#We get 18, which is the index number of the first character of the first 
# (and only) occurrence of the word 'the' in our sentence.

#Now, we can use the result to extract the last part of the sentence using string slicing:

text = 'Without comments, the code becomes unreadable.'
index = text.find('the')
print(text[index:])

#the code becomes unreadable.

#Additionally, we have the str.replace() method, 
# which is used to replace certain characters or a sequence of characters within a string.

#Here, we use the str.replace() method to replace the word 'pizza' with 'burgers':
text = 'I like apples, but I love pizza more!'
print(text.replace('pizza','burgers'))

#I like apples, but I love burgers more!

#If there's more than one occurrence of the specified string, 
# str.replace() will change all of them.

#Here, we replace all occurrences of 'I' with 'you':

text = 'I like apples, but I love pizza more!'
# note that this method is case sensitive
# only capital I is replaced
print(text.replace('I','You'))

#You like apples, but You love pizza more!

#It's important to note that this method, like all string methods, creates a new adjusted copy of the original string, 
# while the original string remains unchanged.

#Here, you can see that the original string remains the same even after we apply str.replace():

text = 'I like apples, but I love pizza more!'
 
# print new adjusted copy of string
print(text.replace('I','You'))
# original string remains unchanged
print(text)

#You like apples, but You love burgers more!
#I like apples, but I love pizza more!



#Using str.replace(), you can also completely remove 
# specific characters or sequences from a string:

text = 'I like apples, but I love pizza more!'
 
# remove ' more'
print(text.replace(' more',''))
# remove all 'p'
print(text.replace('p',''))

# I like apples, but I love pizza!
#I like ales, but I love izza more!



#EX:
#Locate the position of the alphabet in this mysterious, lengthy string. 
# Utilize the str.find() method for this purpose, then extract the alphabet 
# from the gibberish with string slicing.

gibberish = 'absdqwjbasdbqwlabcdefghijklmnopqrstuvwxyz'
 
# use str.find() to find the alphabet
index = gibberish.find("abcdefghijklmnopqrstuvwxyz")
# index = gibberish.find('abc') <- this is a smart approach!!!
# use slicing str[:] to extract the alphabet
alphabet = gibberish[index:]

print(alphabet)
 


#Here, the text is even messier. E has been replaced by &, and S has been replaced by *. 
# Clean up the mess using str.replace().
#Hint: You have to use str.replace() twice, 
# but remember that the method does not change the original string 😉.

gibberish = '&L&PHANT* &AG&RLY &AT &NORMOU* AMOUNT* OF D&LICIO&* WAT&RM&LON*'

# use str.replace() to clean up string
# note that we have to use it twice

gibberish2 = gibberish.replace("&", "E")
text = gibberish2.replace("*", "S")
 
print(text)

# note: another way would be to chain the methods:
# text = gibberish.replace('&','E').replace('*','S')