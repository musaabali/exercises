# Programming Exercise 2-6
#
# Program to calculate a total sale price using state and local sales tax.
# This program prompts a user for an amount of purchase,
# uses constants to calculate state, county and total sales tax, and a purchase total
# then displays the details of these calculations for the user.

# Variables for purchase amount, state tax, county tax, total tax and total sale
# all initialized as floats


# Constants for the state and county tax rates
STATE_TAX_RATE = .36
COUNTY_TAX_RATE = .09

# Get the amount of purchase from the user, casting it to a float.
ip = input("Enter the amount of purchase: ")
ip = float(ip)

# Calculate the state sales tax.
state_tax = STATE_TAX_RATE * ip

# Calculate the county sales tax.
county_tax = COUNTY_TAX_RATE * ip

# Sum the total tax.
sum = state_tax + county_tax

# Calculate the total of the sale.
total = sum + ip

# Print detailed information about the sale, formatting all values to two decimal places.

print (str.format("Amount of Purchase: {:.2f}, Tax total = {:.2f}, Full Total = {:.2f} ", ip, sum, total))



