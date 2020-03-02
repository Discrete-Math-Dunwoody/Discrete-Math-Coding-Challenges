###########################################################
#
# Name: Andrew Egle
#
# Class: Discrete Mathematics
#
# Date Created: 2/21/2020
#
# Program: Collatz Sequence
#
# Edits:
#   2/25/2020 - Andrew Egle: Made the starting number customizable
#
###########################################################
import math
import time

def begin():
    userNumber = 999999 #Change this number to change where the sequence starts

    print("\nHello, Welcome to the Collatz Sequence Calculator")
    print("This sequence will start at", '{:,}'.format(userNumber), "and find the longest sequence chain\n")
    
    return userNumber

def calculations(numberSelect):

    oldLength = 0
    initialNumber = numberSelect

    # While loop to count down from initial number to 0
    while initialNumber != 0:

        newNumber = initialNumber
        i = 1
        # While loop to end the count once the sequnece hits 1
        while newNumber != -1:
           
            if newNumber  == 1:# Determining when the sequence hits 1
                newNumber = -1

            elif newNumber % 2 != 0:# Determining if the number is odd
                newNumber= (3*newNumber) + 1
                i = i + 1

            elif newNumber % 2 == 0:# Determinig if the number is even
                newNumber = newNumber/2
                i = i + 1

            else:
                print("Something went wrong")
                newNumber = -1
                
        newLength = i
        # Using if statement to find the greatest sequence length
        if newLength > oldLength:
            oldLength = newLength
            thisNumber = initialNumber
        
        initialNumber = initialNumber - 1 # Reducing the starting number by 1 for the while loop
        
    print('{:,}'.format(thisNumber), "has a sequence length of" ,oldLength, "numbers")

def runTime():
    a = time.perf_counter()
    print("This program took",'%.2f' %a, "\n")


def main():
    numberSelect = begin()
    calculations(numberSelect)
    runTime()

main()