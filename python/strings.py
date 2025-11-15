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

