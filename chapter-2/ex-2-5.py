# Programming Exercise 2-5
#
# Program to calculate distances traveled over time at a speed.
# This program uses no input.
# It will calculate the distance traveled for 6, 10 and 15 hours at a constant speed,
# then display all the results on the screen.

# Variables to hold the three distances.
# be sure to initialize these as floats.
a = 0.0
b = 0.0
c = 0.0

# Constant for the speed.
CONSTANT_SPEED = 5

# Calculate the distance the car will travel in
# 6, 10, and 15 hours.
a = CONSTANT_SPEED * 6
b = CONSTANT_SPEED * 10
c = CONSTANT_SPEED * 15

# Print the results for all calculations.
print(str.format("{}", a))
print(str.format("{}", b))
print(str.format("{}", c))




