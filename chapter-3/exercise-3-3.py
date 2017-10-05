# Programming Exercise 3-3
#
# Program to assign an age category to an numerical age.
# This program will prompt the user for an integer age value,
# and use it to choose an age category,
# then display that category on the screen.

# Variables to hold an age and a category.
# initialize age as an int and category as a string.
age = int()
category = str()
# Get the person's age.
# remember to convert the input to an int.
age = int(input("Input the person's age: "))

# Determine if the person is an infant, child, teenager, or adult and set the category.
# Use a series of if ... elif ... etc. statements.
if age > 18:
    category = "adult"
elif age > 12:
    category = "teenager"
elif age > 2:
    category = "child"
else:
    category = "infant"
    
# display a message with the age category.
print (str.format("This person is a {}.", category))


