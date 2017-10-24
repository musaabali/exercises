# Programming Exercise 5-11
#
# Program to quiz a user with a random addition problem.
# This program uses a random function to generate addends for an addition problem,
#   calls a function to display the problem, passing the operands as arguments,
#   calls a second function to prompt the user for an answer to the problem,
# it calculates the correct answer,
# then passes the user answer and correct answer to a third function to evaluate the results,
#   and display whether the user was correct or not.



# to generate random numbers, import random module
import random

# define the main function
def main():
	# Define constant values for min addend and max addend
    MIN = 0
    MAX = 10
    # Define local int variables for addend 1, addend 2, user answer and correct answer
    addend_one = 0
    addend_two = 0
    user_answer = 0
    correct_answer = 0
    # Generate random integers for addend 1 and addend 2, with values from min to max
    # constants defined above 
    addend_one = generate_random_int(MIN, MAX)
    addend_two = generate_random_int(MIN, MAX)
    
    # Call the function to display addition problem passing addend 1 and addend 2 
    display_addition_problem(addend_one, addend_two)
    # Assign the user answer to the result of calling the function to prompt for answer
    user_answer = prompt_for_answer()
    # Calculate correct answer
    correct_answer = addend_one + addend_two
    # Call the function to evaluate answer, passing correct answer and user answer
    evaluate_answer = (correct_answer, user_answer)

# Define a function to display addition problem
# This function accepts two integer parameters, the addends,
# performs no calculations,
# but displays them, one above the other, aligned.
def display_addition_problem(addend_one, addend_two):
    # print the first number in a field 5 characters wide
    line1 = format(addend_one, '5')
	# print a + sign, followed by the second number in a field 4 characters wide



def prompt_for_answer():
    user_entry = int(input("Enter your answer"))
    return user_entry

    
# Define a function to evaluate the user's answer and display the evaluation
# This function takes correct answer and user answer as parameters
# if compares them to see if they match
# and displays a success or failure message to the user

	# if correct answer equals user answer, display success message
	
	# else display failure message



# Call the main function to start the program




