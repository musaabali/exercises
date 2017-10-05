# Programming Exercise 3-2
#
# Program to find which of two rectangles has the greater area.
# This program will get two sets of lengths and widths from a user,
# use them to calculate and compare two area values,
# and display a message comparing those areas

# Local variables
# you need length, width and area for A and for B
# initialize these as floats
length_a = 0.0
length_b = 0.0
width_a = 0.0
width_b = 0.0
area_a = 0.0
area_b = 0.0

# Get length A from the user and convert it to a float
length_a = float(input("Give me Rectangle A's length: "))

# Get width A from the user and convert it to a float
width_a = float(input("Give me Rectangle A's length: "))

# Get length B from the user and convert it to a float
length_b = float(input("Give me Rectangle B's length: "))

# Get width B from the user and convert it to a float
width_b = float(input("Give me Rectangle B's length: "))

# Calculate area A
area_a = length_a * width_a

# Calculate area B
area_b = length_b * width_b

# Print each area, formatting the values to 2 decimal places
print (str.format("Rectangle A's area is {:.2f} Units", area_a))
print (str.format("Rectangle B's area is {:.2f} Units", area_b))
# if area A is greater, print "A is greater" message.
if area_a > area_b:
    print("A is greater")
# else if area B is greater, print "B is greater" message.
elif area_a < area_b:
    print("B is greater")
# else print "A and B are equal" message.
else:
    print("A and B are equal")