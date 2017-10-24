# Programming Exercise 5-12
#
# Program to find the greater of two integers.
# This program accepts two integers,
# passes them to a function that compares them,
# and displays which one is greater.



# define the main function
def main():
    # Define local variables to hold two integers
    int1 = int(input("Enter your first interger: "))
    int2 = int(input("Enter your second integer: "))


    # print the return value from calling a function to find the greater of two integers
    # the two integers are passed as arguments
    ans = find_greater(int1, int2)
    print (ans)
 
# Define a function to compare integer values.
# This function accepts two integer parameters,
# compares them,
# and returns the value of the greater.
def find_greater(int1, int2):
	# if the first integer is greater, return the first integer
    if int1 > int2:
        return int1
	# else, return the second integer
    else:
        return int2


# Call the main function to start the program
main()




