# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

class User:
	# constructor
	def __init__( self , name, email, age ):
		self.name = name
		self.email = email
		self.age = age
	
	def greeting( self ):
		return f'My name is {self.name}'
	
	def testGreeting( self ):
		return 'wut'

class Customer(User):

	def __init__( self , name, email, age ):
		self.name = name
		self.email = email
		self.age = age
		self.balance = 0

	def set_balance( self, balance ):
		self.balance = balance

brad = User('test', 'test' , 36 )
janet = User('test', 'test' , 38 ) 

print( brad.greeting() )
print( janet.testGreeting() )

john  = Customer('John', 'idiot', '99')
print( john.name )

