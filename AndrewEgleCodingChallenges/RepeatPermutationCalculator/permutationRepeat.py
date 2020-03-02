######################################
#
# Name: Andrew Egle
#
# Date Created: 1/29/2020
#
# Project: Coding Challenge
#
# Project Name: Permutation with repeats calculator
#
######################################

import math

# Getting user inputs and returning them as a tuple
def begin():
    print("This is strictly a binomial calculator for permutations that allow repeats")
    full_set = input("Enter the full set you can choose from: ")
    number_select = input("Enter the number of choices you can make: ")
    input_list = [full_set, number_select]
    return(input_list)

def calculations():
    #list turned into integers
    max_options = int(user_Inputs[0])
    total_choices = int(user_Inputs[1])

    # Binomial equation
    # P^R(n,r) = n^r
    permutation_Repeat = max_options ** total_choices
    print("\nUsing the permutation with repeat equation: " + str(permutation_Repeat))

    # User max selections multiplying itself to  the total choices number of times 
    total = max_options
    for i in range(1,total_choices):
        total = total * max_options

    print("Using " + str(max_options) + " multiplied itself " + str(total_choices) + " times: " + str(total))
    

user_Inputs = begin()
calculations()