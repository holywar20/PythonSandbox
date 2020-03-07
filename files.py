# Python has functions for creating, reading, updating, and deleting files.

myFile = open('myfile.txt' , 'w' )

# Get some info
print("Name: ", myFile.name )
print("closed? : " , myFile.closed )
print("Opening Mode" , myFile.mode )

# Write to file
myFile.write('I Love Python')
myFile.close()

# Appending
myFile = open('myFile.txt' , 'a')
myFile.write(", but it's got some annoying bits.")
myFile.close()