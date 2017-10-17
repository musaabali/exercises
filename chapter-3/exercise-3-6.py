# Programming Exercise 3-6
#
# Program to check if a date is 'magic' (day * month = year).
# This program takes a month, day and year from the user as integers,
# Checks to see if each is in range, then checks whether month * day = year,
# then displays an appropriate message depending on the result

# Variables for month, day, year and message
# initialize month, day and year as integers, message as a string
month = 0
day = 0
year = 0
message = ""
# Get month and cast it to int
month = int(input("Input the month: "))

# Get day and cast it to int
day = int(input("Input the day: "))

# Get year and cast it to int
year = int(input("Input the year(last 2 numbers): "))

# This problem can be solved with if-else logic by the reducing the problem domain
# if month input is out of range
if month > 12:
	# set message to hold "invalid month" message
    print ("Invalid month")

# else if day input is out of range
elif day > 31:
    # set message to hold "invalid day" message
    print ("Invalid day")
# else if  year input is out of range (greater than 99 or less than 0)
elif year < 0 or year > 99:
    # set message to hold "invalid year" message
    print ("Invalid year - follow the instructions")
# else 
else:
    # set message to hold the date in 00/00/00 form
    message = str.format("The date is {}/{}/{}", month, day, year)
    # if day * month equals year, add " is a magic date" to message
    if day * month == year:
        message += " is a magic date"
    # else add " is not a magic date" to message
    else:
        message += " is not a magic date"
# print message for the user
print (message)

