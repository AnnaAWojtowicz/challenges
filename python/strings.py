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

