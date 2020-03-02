#########################################
#
# Name: Andrew Egle
#
# Date Created: 1/15/2020
#
#########################################

def say_hi (name):
    print("Hello " + name.capitalize())

def madLib_inputs():
    color = input("\nEnter a color: ")
    noun = input("\nEnter a plural noun: ")
    celebrity = input("\nEnter a celebrity: ")
    cap_color = color.lower()
    cap_plural_noun = noun.capitalize()
    celebrity.capitalize()
    return(cap_color, cap_plural_noun, celebrity)

def madLib_creator(tuple):
    print("\n\nRoses are " + inputs[0] + 
    ",\n" + inputs[1] +" are blue," + 
    "\nI love " + inputs[2] + 
    ",\nHow about you?\n\n")


user_name = input("\nPlease enter your name: ")
say_hi(user_name)
inputs = madLib_inputs()
madLib_creator(inputs)