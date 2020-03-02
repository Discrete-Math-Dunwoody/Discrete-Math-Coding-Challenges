##################################################################################################################
#
# Name: Andrew Egle
#
# Date created: 2/13/2020
#
# Project Name: Surjection Calculator
#
##################################################################################################################

import math

# Receiving user input for sets sizes and returning the info
def userInputs():
    print("\n\n\n\nThis is strictly a surjection calculator with no limits")

    # While loop and try/catch to make sure user inputs are integers
    invalid_input1 = 1
    while invalid_input1 == 1:
        try:
            full_set = int(input("\nWhat is the cardinality of the first set: "))
            invalid_input1 = 0
        except:
            print("Invalid Option")
    
    # While loop and try/catch to make sure user inputs are integers
    invalid_input2 = 1
    while invalid_input2 == 1:
        try:
            map_set = int(input("\nWhat is the cardinality of the set you are trying to map onto: "))
            invalid_input2 = 0
        except:
            print("Invalid Option")
    
    input_list = [full_set, map_set]
    return(input_list)

# Creating lists to hold variables for powers, combinations, and those two multiplied against eachother.
# This then returns a list that has variables based on the power list variable multiplied against its respective
# combination list variable
def listGenerator(userList):
    mapSet = userList[1]
    firstSet = userList[0]

    # For loop to create a list of powers for a surjection equation 
    # to multiply against its correct combination variable
    powerList = []
    for i in range(mapSet - 1, -1, -1):
        powers = i ** firstSet
        powerList.append(powers)

    # For loop to create a list of combination for a surjection equation 
    # to multiply against its correct power variable
    fact = math.factorial
    combinationList = []
    for j in range(1, mapSet + 1):
        combos = fact(mapSet) // (fact(j) * fact(mapSet - j))
        combinationList.append(combos)

    # For loop multiplying the variables in the powers list against 
    # the variables in the combinations list
    multipliedList = []
    for k in range(0, len(combinationList)):
        multipliers = combinationList[k] * powerList[k]
        multipliedList.append(multipliers)

    return(multipliedList)

# Creating the formula based on the cardinality of the user's inputs and finally calculating it
def calculations(multiplied, userList):
    mainPower = userList[1] ** userList[0]

    subNumber = multiplied[0]
    # For Loop alternating addition and subtraction based on the inputs from the user
    for m in range(1,len(multiplied)):
        if (m % 2) == 0:
            subNumber = subNumber + multiplied[m]

        else:
            subNumber = subNumber - multiplied[m]

    print("\nThe number of surjective functions is: " + str(mainPower - subNumber)+"\n")

def main():
    userList = userInputs()
    multiplied = listGenerator(userList)
    calculations(multiplied, userList)
    
main()