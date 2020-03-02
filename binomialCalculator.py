##################################################################################################################
#
# Name: Andrew Egle
#
# Date Created: 2/3/2020
#
# Project: Coding Challenge
#
# Project Name: Binomial Calculator
#
# This code can be to contributed to the candidate solutions shared with future students.
# Please document: Name, Date, Changes made.
# 
# PLEASE COMMENT YOUR CODE
#   Changes:
#       2/5/2020 - Andrew Egle: Added while loops and try/catches for user functionality
#
##################################################################################################################

# Importing libraries
import math
import sys

# Getting user input for the type of equation to use
def calculator():
        # Setting the while loop to 0 until the user changes a selection
    user_select = 0
    while user_select == 0:
        # Getting user input for the type of binomial
        calculator_type = input("\n\nWill you be calculating a Combination or Permutation?\n"+
        "Please select a number:\n1) Combination\n2) Permutation\nZ) Quit\n")

        # Setting the calculator variable to the user selection
        if calculator_type == "1":
            user_select = 1

        elif calculator_type == "2":
            user_select = 2

        elif calculator_type.lower() == "z":
            user_select = 3

        else:
            print("\n\n\nINVALID SELECTION\n")
            user_select = 0
    # Returning the user selection for combination or permutation
    return(user_select)

# Getting user input determining if repeates are allowed
def repeats():
    #Setting while loop to 0 until user determines a selection
    repeating = 0
    while repeating == 0:
        # Getting the user input for repeats
        allow_repeats = input("\n\nAre repeats allowed?\n"+
        "Please select a number:\n1) Yes\n2) No\nZ) Quit\n")

        # Setting the allow repeats to the user selection
        if allow_repeats == "1":
            repeating = 1
        elif allow_repeats == "2":
            repeating = 2

        elif allow_repeats.lower() == "z":
            repeating = 3

        else:
            print("\n\n\nINVALID SELECTION\n")
            repeating = 0
    # Returning the user selection if repeats are allowed or not
    return(repeating)

# Calculating the user selections
def calculations(calculator_option, repeat_option):
    # Setting the variables to the user selections
    calc_selector = calculator_option
    repeat_selector = repeat_option
    # Getting user inputs for the set size and the number of options they can choose. Example: 6 chips, choose 3.
    first_valid = False
    while first_valid == False:
        full_set = input("Please enter the total amount you can choose from: ")
        try:
            max_options = int(full_set)
            first_valid = True
        except:
            if full_set.lower() == "z":
                sys.exit()
            else:
                print("Invalid Option")
                first_valid = False

    second_valid = False
    while second_valid == False:
        number_select = input("Please enter the number of selections you can make: ")
        try:
            total_choices = int(number_select)
            second_valid = True
        except:
            if number_select.lower() == "z":
                sys.exit()
            else:
                print("Invalid Option")
                second_valid = False

    #Taking user equation selection
    if calc_selector == 1:
        # Taking user repeat selection
        if repeat_selector == 1:
            # CR(n,r) = (n+r−1)! / r! * (n−1)!
            combination_Reapeat = int(math.factorial(max_options + total_choices - 1) / (math.factorial(total_choices) * math.factorial(max_options - 1)))
            print("\nNumber of combinations with repeats:", str(combination_Reapeat) + "\n")
        elif repeat_selector == 2:
            # C(n,r) = n! / (r! * (n−r)!)
            combination_noReapeat = int(math.factorial(max_options) / (math.factorial(total_choices) * math.factorial(max_options - total_choices)))
            print("\nNumber of combinations with no repeats: " + str(combination_noReapeat) + "\n")
    elif calc_selector == 2:
        if repeat_selector == 1:
            # P^R(n,r) = n^r
            permutation_Repeat = max_options ** total_choices
            print("\nNumber of permutations with repeats: " + str(permutation_Repeat) + "\n")
        elif calc_selector == 2:
            # P(n,r) = n! / (n−r)!
            permutation_noRepeat = int(math.factorial(max_options) / math.factorial(max_options - total_choices))
            print("\nNumber of permutations with no repeats: " + str(permutation_noRepeat) + "\n")
    else:
        print("Something went wrong")

# Main function 
def main():
    print("\nHello, welcome the the binomial calculator!\n Enter Z at any time to quit")
    wants_quit = 0
    while wants_quit == 0:

        # Calling funtion
        calculator_option = calculator()
        if calculator_option == 3:
            sys.exit() # Exits if user wants to quit

        # Calling function
        repeat_option = repeats()
        if repeat_option == 3:
            sys.exit() # Exits if user wants to quit

        # Calling function
        calculations(calculator_option, repeat_option)
        quit_plz = input("\nWould you like to continue?\n1) Yes\n2) No\n")
        if quit_plz == "1":
            wants_quit = 0
        
        elif quit_plz == "2":
            wants_quit = 1
        
        else:
            print("Invalid Option\nEnding Calulator")
            sys.exit()

main()