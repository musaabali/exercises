# Programming Exercise 5-2
#
# Program to calculate final purchase details.
# This program takes a purchase amount from a user,
# then calculates state tax, county tax and total tax,
# 	and passes them to a function to be totaled
# and displayed



# Global constants for the state and county tax rates
STATE_RATE = .06
COUNTY_RATE = .05


# define the main function
def main():
    # Define local float variables for purchase, state tax and county tax
    purchase = 0.0
    state_tax = 0.0
    county_tax = 0.0
    # Get the purchase amount from the user
    purchase = float(input("Give me the purchase amount: "))
    # Calculate the state tax using the global constant for state tax rate
    state_tax = purchase * STATE_RATE
    # Calculate the county tax using the global constant for county tax rate
    county_tax = purchase * COUNTY_RATE
    # Call the sale details function, passing the purchase, state tax and county tax
    sales_details(purchase, state_tax, county_tax)


# define a function to display purchase details
# this function accepts purchase, stateTax, and countyTax as arguments,
# calculates the total tax and sale total,
# then displays the purchase details
def sales_details(purchase, state_tax, county_tax):
    # Define local float variables for total tax and sale total
    tax_total = 0.0
    sale_total = 0.0
	# Calculate the total tax
    tax_total = state_tax + county_tax
	# Calculate the total sale
    sale_total = tax_total + purchase
    # Display the purchase details, including purchase, state tax, county tax,
    #	total tax, and sale total, each on a line.  Format floats to 2 decimal places.
    print ("Purchase details")
    print ("----------------")
    print (str.format("Purchase: ${:.2f}", purchase))
    print (str.format("State Tax: ${:.2f}", state_tax))
    print (str.format("County Tax: ${:.2f}", county_tax))
    print (str.format("Total Tax: ${:.2f}", tax_total))
    print (str.format("Sale Total: ${:.2f}", sale_total))
# Call the main function to start the program.
main()
