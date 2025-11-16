# CONDITIONALS

# IF STATEMENTS

#Imagine we have the following variable:

temperature = 75

# The value of this variable will most likely change over time.
# Assume that we want to print a message if's is warm outside – 
# let's say if the temperature is above 70.
# That's where we use our first if statement. Run the code to see what happens:

temp = 75
print('The temperature is ', temp)      # The temperature is  75
 
if temp > 70:
	print("It's warm outside")          # It's warm outside
	
# That's right, because the temperature is above 70, our program prints that it's warm outside.

# Now, the temperature has changed. Let's see what happens:

temp = 60
print('The temperature is ', temp)      # The temperature is  60
 
if temp > 70:
	print("It's warm outside")
	
# Since the temperature is not above 70, the print statement is not executed.

# But how does it work?
# The if-statement executes a block of code if a certain condition is true. 
# It starts with the if keyword followed by a condition and a colon, and finally, 
# an indented block of code.

# if condition:
	# indented block of code
	
# Note that the indentation is crucial. The code inside the if block must be 
# indented consistently. Typically, four spaces are used for indentation. 
# I personally prefer to just hit the tab button once to indent a line of code.



# ELIF

#Let's go back to our temperature example. 
# We already know that the program will log that it's warm outside if the temperature is above 70.

temperature = 75
 
if temperature > 70:
	print("It's warm outside")      # It's warm outside
	
# But what if we also want to inform the user if it's cold outside, say if the temperature is below or equal to 70?
# We could add another if-statement.

temperature = 60
 
if temperature > 70:
	print("It's warm outside")
 
if temperature <= 70:
	print("It's cold outside")      # It's cold outside
	
# That works, but it feels a bit tedious. We have to write another condition for the exact opposite of the first one.
# Fortunately, there is a better way to write this in Python: the else-statement.

temperature = 60
 
if temperature > 70:
	print("It's warm outside")
else:
	print("It's cold outside")      # It's cold outside
	
# The code does exactly the same as before, but without the need to write another condition. Instead, we are using an else-statement.
# The else-statement provides a fallback option to execute a block of code when the preceding condition of the if-statement evaluates to false.
# Let's check if it also works for warm weather:

temperature = 75
 
if temperature > 70:
	print("It's warm outside")      # It's warm outside
else:
	print("It's cold outside")

# Since the condition of the if-statement is met, the else block is ignored.

# Suppose that temperatures between 51 and 70 degrees are neither cold nor warm. 
# We can use a so called elif-statement for this scenario.

temperature = 60
 
if temperature > 70:
	print("It's warm outside")
elif temperature > 50:
	print("It's neither cold nor warm outside")     #It's neither cold nor warm outside
else:
	print("It's cold outside")
	
# Great! In this scenario, the first condition that is fulfilled triggers its respective code block, and all other code blocks are not executed.
# elif, short for 'else if', checks another condition if the previous ones are false.
# You can have multiple elif-statements.

temperature = 45
 
if temperature > 70:
	print("It's warm outside")
elif temperature > 50:
	print("It's neither cold nor warm outside")
elif temperature > 40:
	print("It's a bit chilly outside")      # It's a bit chilly outside
else:
	print("It's cold outside")
	
