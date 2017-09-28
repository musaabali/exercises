# Programming Exercise 2-2
#
# Program to compute expected profit from sales.
# This program will prompt a user for a sales projection
# and use it to calculate expected profit from a predefined profit margin
# then display the result.

# Variables to hold the sales total and the profit
# initialize them as float values

salesTotal = 0.0
profit = float(0)
# Get the amount of projected sales.
# be sure to convert the input to a float
projectedSales = input("Enter projected sales amount: ")
projectedSales = float(projectedSales)

# Calculate the projected profit using a 23% profit margin.
projected_profit = projectedSales * .23

# Print the projected profit.
# be sure to format the output to two decimal places
print (str.format("The projected profit is {:.2f}", projected_profit))




