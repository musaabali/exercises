# Programming Exercise 2-4
#
# Program to compute a final price for five items with tax.
# This program will prompt a user for a set of five prices,
# sum them to a subtotal and calculate sales tax with tax rate stored in a constant,
# then display the results on the screen.

# Variables to hold the prices of five items, the subtotal, and the total.
# All should be initialized as floats.


# Constant for the sales tax rate.
SALES_TAX_RATE = .06

# Get the price of each item by prompting the user.
# You will need to convert each input to a float.
first_item = input("Enter the first price: ")
first_item = float(first_item)
second_item = input("Enter the second price: ")
second_item = float(second_item)
third_item = input("Enter the third price: ")
third_item = float(third_item)
fourth_item = input("Enter the fourth price: ")
fourth_item = float(fourth_item)
fifth_item = input("Enter the fifth price: ")
fifth_item = float(fifth_item)

# Calculate the subtotal by adding up the item prices.
subtotal = first_item + second_item + third_item + fourth_item + fifth_item

# Calculate the sales tax by multiplying the subtotal by the tax rate.
sales_tax = subtotal * SALES_TAX_RATE

# Calculate the total by adding the subtotal and tax.
total = subtotal + sales_tax

# Print the values for the subtotal, tax and total.
# Label each value, and format them to display with two decimal places. 

print (str.format("Subtotal: {:.2f}, Tax = {:.2f}, Total = {:.2f} ", subtotal, sales_tax, total))



