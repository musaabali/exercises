# Programming Exercise 4-2
#
# Program to output table of calories burned for different times.
# This program takes no input.
# It uses a constant for calories burned per minute to calculate the calories burned for a range of different times,
# then displays a table with the results for each time. 

# Declare a constant for the calories burned per minute.
CPM = 5
# Declare variables for calories burned and number of minutes.
# initialize calories burned as a float and minutes as an integer
calories_burned = 0.0
minutes = 0
# print the table header using two tabs between Minutes and Calories Burned
# print a line under the header using underscores
print("Minutes\t\tCalories Burned")
print("_______\t\t_______________")
# Use a for loop to calculate and display a display a line for each value of minutes
# set up the loop using a range of comma-separated minutes values 
for i in range(minutes):
    # calculate calories burned using the constant for calories burned per minute
    calories_burned = minutes * CPM
    # display the minutes and calories burned using two tabs between the values
    print(minutes + "\t\t" + calories_burned)