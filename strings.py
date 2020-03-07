# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = "Bryan"
age = 37

# Concatenate
print('Hello ' + name + " and I am " + str(age) )

# Arguments by position
print( '{1} , {2} , {0}'.format('a', 'b', 'c'))

# Arguments by name
print('My name is {name} and I am {age}'.format(name="Badass", age='999'))

# F-Strings ( only in 3.6+ )
print(f'My name is {name} and i am {age}')

# String Methods

s = 'hello there world'

# Capitalization of things
print( s.capitalize() )
print( s.upper() )
print( s.lower() )
print( s.swapcase() )

# Length
print( len(s) )

# Replace
print(s.replace('world', 'everyone') )

# Count
sub = "h"
print( s.count(sub) )
