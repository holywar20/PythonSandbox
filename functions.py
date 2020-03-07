# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

def sayHello( name = 'Sam '):
	"""
	Prints and then a name.
	"""
	print("hello " + name )
sayHello()
sayHello('Beth')

def getSum( x , y ):
	total = x + y
	return total

sum = getSum( 4 , 5 )
print( sum )

def addOneToNum( x ):
	x += 1
	return x

num = 5
new_num = addOneToNum( num )
print( new_num )
# A lambda function is a small anonymous function. 
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda x, y : x + y
print( getSum( 1 , 3) )

