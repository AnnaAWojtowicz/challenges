# In Python, you define a function using the def keyword, 
# followed by the function name, parentheses, and a colon. 
# The function body is then indented below.

def name():
	# function body
	print('Hi')
	
# After defining a function, we can call it using its name followed by a pair of parentheses.

# call the function
name()      # Hi

# The function body is only executed when the function is being called, 
# which is why, in the following example, the updated value of num is printed:

num = 0
def log_message():
   print(num)
 
num = 1
log_message()       # 1


