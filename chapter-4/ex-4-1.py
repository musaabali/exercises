# Programming Exercise 4-1
#
# Program to total the values of five integers.
# This program the user for an integer five times,
# and totals them up,
# then displays the total entered on the screen.

# Initialize variables for bugs collected and total bugs.
# be sure to initialize them as integers
bugs_col = 0
bugs_total = 0
# Get the number of bugs collected from the user
# use a for loop to get the number of bugs exactly five times, once for each day

for i in range(5):
    bugs_col = int(input("Give me the bugs for day " + str(i+1) + ": "))
    bugs_total += bugs_col

# Display the total number of bugs collected for all five days.
print("You have collected " + str(bugs_total) + " bugs in 5 days")


hehe = input("Did you find a golden stag? yes or no?: ")
if hehe == "yes":
    print("WHOA! You caught a golden stag! The light, the blinding light!")
else:
    print("git gud")
