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