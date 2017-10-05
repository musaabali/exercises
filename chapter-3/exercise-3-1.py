# Programming Exercise 3-1
#
# Program to display the name of a week day from its number.
# This program prompts a user for the number (1 to 7)
# and uses it to choose the name of a weekday
# to display on the screen.

# Variables to hold the day of the week and the name of the day.
# Be sure to initialize the day of the week to an int and the name as a string.
day_of_the_week = int()
day_name = str()

# Get the number for the day of the week.
# be sure to format the input as an int
inferior_object_type = input("Enter the number of the day of the week: ")
day_of_the_week = int(inferior_object_type)

# Determine the value to assign to the day of the week.
# use a set of if ... elif ... etc. statements to test the day of the week value.

if day_of_the_week == 1:
    day_name = "Sunday"
elif day_of_the_week == 2:
    day_name = "Monday"
elif day_of_the_week == 3:
    day_name = "Tuesday"
elif day_of_the_week == 4:
    day_name = "Wednesday"
elif day_of_the_week == 5:
    day_name = "Thursday"
elif day_of_the_week == 6:
    day_name = "Friday"
elif day_of_the_week == 7:
    day_name = "Saturday"
else:
    day_name = "Number out of range"




# use the final else to display an error message if the number is out of range.


# display the name of the day on the screen.

print(day_name)


