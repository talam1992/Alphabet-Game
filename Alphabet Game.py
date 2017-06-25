__author__ = 'Timothy Lam'
###Alphabet Game###
#Desc: Game that test our speed by making you type out the alphabet#

#Import
import time

#Control Variable
start = "true"

#Instruction#
print("INSTRUCTIONS\n1. When the countdown get to 0 type the alphabet!\n2. That is that only rule")
input("Press Enter when ready.")
#While Loop#
while start == "true":
    #Name Stuff#
    name = input("What is your name?: \n")
    name = name.split(" ")

    #Countdown#
    print("Game will start in: ")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

    #Start Time#
    startTime = time.time()

    #Alphabet Input
    alphabet = input("Go! Go! Go! Type in the Alphabet: \n")
    alphabet = alphabet.lower()

    #Validation#
    if alphabet == "abcdefghijklmnopqrstuvwxyz":
        #End Time#
        endTime = time.time()

        #Score#
        score = endTime =startTime
        score = round(score,1)

        #Output Score#
        print("Congratulations!!!" + name[0] + "\nYou Time was " + str(score) + "s")
    else:
        print("You made a mistake!")


    #Restart#
    restart = input("Input 'YES' to restart: \n")
    if restart == "YES":
        start ="true"
    else:
        start = "false"
