# Programming Exercise 6-1
#
# Program to display the contents of a text file.
# This program takes no user input, but requires a numbers.txt file,
# opens the fine and reads the whole contents at once,
# and displays the contents.


# define the main function
def main():
    # Declare a local variable to hold the file contents
    # initialize it as an empty string
    contents = ""
    filename = ""
    # Open numbers.txt file for reading
    # that is, use a variable to hold the file handle created when opening the file
    filename = open("numbers.txt", "r")

    # Read in data and store its contents
    contents = filename.read()

    # Close file
    filename.close()

    # Print the contents
    print contents

# Call the main function.
main()

