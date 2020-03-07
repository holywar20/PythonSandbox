# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
	Variable names are case sensitive (name and NAME are different variables)
	Must start with a letter or an underscore
	Can have numbers but can not start with one
"""

x = 1				#int
y = 2.5			#float
name = "Bryan"	# string
is_cool = True	# bool

# Mupltiple assignment
x , y, name, isCool = ( 1, 2.5, 'Brad', True )
# Parens required for print on python3
print( x )

a = x + y
# Check type
# Basic math
print(type(x))

# Casting
a = str(a) # makes a string so you can concat it
y = int(y) # truncates

