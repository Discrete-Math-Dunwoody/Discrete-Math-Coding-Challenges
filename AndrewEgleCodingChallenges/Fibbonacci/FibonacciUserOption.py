###########################################################
#
# Name: Andrew Egle
#
# Class: Discrete Mathematics
#
# Date Created: 2/19/2020
#
# Program: Fibbonacci Sequence with user options
#
###########################################################

import math

def begin():
    print("Hello, Welcome to the Fibbonacci Sequence!\n")
    x=0
    # While loop to make sure user enters valid inputs
    while x == 0:
        # Trying to cast the users input to integer and will loop through if it fails
        try:
            choice = int(input("Would you like to do: \n1) Any number you want\n2) The first number with 1000 digits\n"))
            # Making sure the user selects a valid option and if not, loops through
            if choice == 1:
                choice = 0
                x = 1
                return choice
            elif choice == 2:
                choice = 1
                x = 1
                return choice
            else:
                print("Invalid Option\n")
                x = 0
            
        except:
            print("Invalid Option")

# Letting the user choose what number to stop at
def anyNymber(): 
    y = 0
    # Making sure the user enters a valid input
    while y == 0:
        try:
            numberSet = int(input("What digit would you like to stop at: "))
            if numberSet < 0:
                print("Can't go below zero, please enter another option\n")
                y = 0
            elif numberSet == 0:
                print("The number at 0 is 0 and is 1 digit long")
                y = 1
            elif numberSet == 1:
                print("The number at 1 is 1 and is 1 digit long")
                y = 1
            elif numberSet > 1:
                # Creating the beginning of the list and then for looping to the users selection
                fibList = [0,1]
                for i in range(2,numberSet+1):
                    newNumber = fibList[i-1] + fibList[i-2] # Creating a nuew number for the list based on the addition of the two numbers 
                                                            # before it
                    fibList.append(newNumber) # Adding the new number to the list
                    print(str(i) + ": " + str(fibList[i]))
            
                digits = int(math.log10(fibList[numberSet]))+1 # Finding how many digits the number is
                print("\nThe number at " + str(numberSet) + " is " + str(fibList[numberSet]) + " and is " + str(digits) + " digits long.\n")
                y = 1
            else:
                print("Invalid Option")
                y = 0
            
        except:
            print("Invalid Option")

    
# Finding the first number that has 1000 digits in it 
def thousandDigits():
    numberDigits = 1000
    x = 0
    a = 0
    b = 1
    i = 2
    while x != 1:
        newNumber = a + b
        a = b
        b = newNumber
        #fibList.append(newNumber)
        digits = int(math.log10(newNumber))+1
        if (digits == numberDigits):
            print("The first number with " + str(numberDigits) + " digits occurs at " + str(i) +"\n")
            x = 1
        else:
            i = i+1


def main():
    userOption = begin()
    if userOption == 0:
        anyNymber()
    elif userOption == 1:
        thousandDigits()
    else:
        print("Something went wrong")

main()