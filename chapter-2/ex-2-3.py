# Programming Exercise 2-3
#
# Program to convert area in square feet to acres.
# This program will prompt a user for the size of a tract in square feet,
# then use a constant ratio value to calculate it value in acres
# and display the result to the user.

# Variables to hold the size of the tract and number of acres.
# be sure to initialize these as floats


# Constant for the number of square feet in an acre.
SQUARE_FEET_IN_ACRE = 43560

# Get the square feet in the tract from the user.
# you will need to convert this input to a float
int_square_feet = input("Enter the area in square feet: ")
f_square_feet = float(int_square_feet)

# Calculate the number of acres.
acres = f_square_feet / SQUARE_FEET_IN_ACRE

# Print the number of acres.
# remember to format the acres to two decimal places
print (str.format("That is {:.2f} Acres", acres))




