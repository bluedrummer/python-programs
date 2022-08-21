#Hello thank you for using my program.
#By Bluedrummer or https://github.com/bluedrummer?tab=repositories at github.
#This works with python3
#What does this program do: This is a game called Guess The Number which there will be a random number you have to guess and everytime you get it wrong there will be a hint for the player. Good Luck!
#Thank you for using and hop you enjoy!

#Importing libraries
import random
import sys
import time
import os

#Definining a function that clears the console
def clear_console():
    os.system('clear')

#Clearing the console
clear_console()

#Printing
print("HELLO AND WELCOME TO GUESS THE NUMBER!")
time.sleep(3)
clear_console()
print("THERE IS A NUMBER AND YOU HAVE TO GUESS IT! EVERYTIME YOU DONT GET THE NUMBER CORRECT YOU WILL BE GIVEN A HINT.")
time.sleep(3)
clear_console()
print("HOPE YOU ENJOY!")
time.sleep(3)
clear_console()

#Starting game loop
while True:
    
