# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

fruit_tuple = ('apple', 'orange', 'mango')
fruit_tuple_constrct = tuple( ('apple', 'orange', 'mango') )
print( fruit_tuple )
print( fruit_tuple[1] ) # get a single value

# Tuples with 1 value should have a trailing comma
fruit_tuple_2 = ('Apple' , )

# A Set is a collection which is unordered and unindexed. No duplicate members.

fruit_set = {'Apple', 'Orange', 'Mango'}
print(fruit_set)

# check if exists
print('Apple' in fruit_set )

# Add  / remove / clear to a set
fruit_set.add('Grape')
fruit_set.remove('Apple')

print( fruit_set )
fruit_set.clear()
print( fruit_set )
#fruit