# Programming Exercise 6-2
#
# Program to read up to five lines of a file and display them.
# This program prompts the user for a file name,
# attempts to open and read five lines of the file,
# then displays those lines and finally closes the file.



# define a main function
def main():
    # Declare local variables, line and filename as strings and counter as int
    line = ""
    filename = ""
    counter = 0
    # Prompt the user for a file name
    filename = input("Give me the filename: ")
    # Open the specified file for reading
    filename = open(filename, "r")
    # Read the first line of the file and increment the line counter to 1
    # this is needed to prepare conditions for the while loop to follow
    line = filename.readline()
    counter = 1
    # Use a while loop to read until counter is 5 or reading produces no data
    while(counter != 5 or line == ""):
	# remove carriage returns before display, as print() supplies its own
        line.rstrip()
        # print the current line
        print (line)
        # read the next line
        line = filename.readline()
        # Update counter when line is read
        counter += 1

    # Close file
    filename.close

# Call the main function to begin the program
main()

