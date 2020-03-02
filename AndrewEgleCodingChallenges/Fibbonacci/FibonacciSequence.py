###########################################################
#
# Name: Andrew Egle
#
# Class: Discrete Mathematics
#
# Date Created: 2/19/2020
#
# Program: Fibbonacci Sequence to 1000 digit number
#
###########################################################
import math
import time


def begin():
    print("\nHello, Welcome to the Fibbonacci Sequence!\n")

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
    begin()
    print(time.perf_counter())

main()