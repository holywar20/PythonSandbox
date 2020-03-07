# A List is a collection which is ordered and changeable. Allows duplicate members.

numbers = [1 , 2, 3, 4, 5]
numbers = list( (1,2,3,4,5 ) ) # IDentical to above

print( type(numbers) )
print( numbers )

fruits = ['apples', 'oranges', 'grapes', 'pears'  ] # Zero indexed
fruits.append( 'Mangos' )
fruits.remove( 'grapes' )
fruits.insert(2 , 'Strawberries' )
fruits.pop( 3 ) # should remove pairs

print( fruits )

# Reverse a list
fruits.reverse()
print(fruits)

fruits.sort( reverse = True )
print(fruits)
