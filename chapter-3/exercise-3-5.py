# Programming Exercise 3-5
#
# Program to convert a value in kilograms to Newtons, then check whether it is in range.
# This program will prompt a user for a mass in kilograms,
# convert it to Newtons and use constants to check if the weight is within range,
# then display the weight and a range message.



# Global constants for minimum, maximum and mass multiplier values
MINIMUM = 100
MAXIMUM = 500
MASS_MULTIPLIER = 100

# Variables for weight and mass initialized as floats   
weight = float()
mass = float()

# Get mass from user and convert it to a float
mass = int(input("Input the number: "))

# Calculate weight using the mass multiplier constant
weight = MASS_MULTIPLIER * mass

# Display the weight

# If weight > maximum or < than minimum display an appropriate message
if weight > MAXIMUM:
    print (str.format("Coolbeans!!! The weight is more than the maximum. The weight is {}N.", weight))
elif weight < MINIMUM:
    print (str.format("Wowza!!! The weight is less than the minimum. The weight is {}N.", weight))
else: print (str.format("Awesomsauce!!! The weight is {}N.", weight))
    






