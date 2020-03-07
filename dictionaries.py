# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

person = {
	'first'	: 'Justice' ,
	'last'	: 'Destroyer',
	'age'		: '9 million 1'
}

print( person['first'] )

# Add / Remove
person['phone'] = '555-555-5555'
del( person['age'] )
person.pop('phone')
person.clear()
print( len(person) )

# Keys
print( person.keys() )
# Values
print( person.values() )

# Copy
person2 = person.copy()

# List of dictionaries
people = [
	{'name' : 'justice' , 'age': '44'} , { 'name' : '23423' , 'age'  : 'Justice'}
]
print( people[1]['name'] )