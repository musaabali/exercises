# Programming Exercise 6-4
#
# Program to count the number of lines in a text file.
# This program takes no user input, but requires the presence of a names.txt file,
# it opens this file and counts the lines, then closes it,
# and displays the count of lines.



# define the main function
def main():
    # Declare variables for line (string) and counter (int0
    line = ""
    counter = 0
    # Open names.txt file for reading
    filename = open("names.txt", "r")
    
    # Read the first line of the file to set up the while loop
    line = filename.readline()
    counter = 1
    # While line is not empty, process the loop
    while(line != ""):
        # increment the counter
        counter += 1
        # read the next line
        line = filename.readline()

    # Close the file
    filename.close()

    # Display the number of lines in the file
    print(str.format("There are {} lines", counter))


# Call the main function to start the program.
main()

