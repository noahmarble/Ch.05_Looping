'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
# introductip and controls
print("Welcome to JEEP. The object is to travel 200 miles across MOAB Utah.")
print("You will be avoiding broken parts, running ot of gas, and the big dude on a harley")
print("You will be asked for commands every so often.")
print("C O M M A N D S :\n")
print("A. do MAINTENANCE on the jeep")
print("B. Ahead MODERATE SPEED")
print("C. Ahead FULL SPEED")
print("D. STOP AND REFUEL")
print("E. STATUS check")
print("F. HOPE for help")
print("Q. To quit\n")

print("the game is starting...\n")

import random
#variables
done = False
milestraveled = 0
gas = 6             #your thirst
brokenparts = 0      #camel tierdness
bigdude = -20        #natives
tools = 3
#command
while not done:
    print("A. do MAINTENANCE on the jeep") #drink from canteen
    print("B. Ahead MODERATE SPEED")
    print("C. Ahead FULL SPEED")
    print("D. STOP AND REFUEL")
    print("E. STATUS check")
    print("F. HOPE for help")
    print("Q. To quit\n")

    #quit
    choice = input("What is your choice? ")
    if choice.lower() == "q" or choice.lower() == "quit":
        done = True

    #status
    elif choice.lower() == "e" or choice.lower() == "status":
        print("miles traveled:", milestraveled)
        print("gas:", gas)
        print("the big dude on the harley is", -bigdude, "miles behind you\n")

    #stop and refuel
    elif choice.lower() == "d" or choice.lower() == "stop and refuel":
        gas = 10
        randomseventofourteen = random.randrange(7,15)
        bigdude+= randomseventofourteen

    #full speed
    elif choice.lower() == "c" or choice.lower() == "full speed":
        randomtetotwenty = random.randrange(10, 21)
        milestraveled+= randomtetotwenty
        gas-=1
        randomonetothree = random.randrange(1, 4)
        brokenparts+= randomonetothree
        randomseventofourteen = random.randrange(7, 15)
        bigdude += randomseventofourteen
        print("miles traveled:", milestraveled)

    #moderate speed
    elif choice.lower() == "b" or choice.lower() == "moderate speed":
        randomfivetotwelve = random.randrange(5, 12)
        milestraveled += randomfivetotwelve
        gas-= 1
        brokenparts+=1
        randomseventofourteen = random.randrange(7, 15)
        bigdude += randomseventofourteen
        print("miles traveled:", milestraveled)

    #maitnance
    elif choice.lower() == "a" or choice.lower() == "maitnence":
        if tools >= 1
            tools-= 1
            broken parts = 0
        else
            print("error, no drinks")


    #gas
    elif gas <= 0:
        print("you have ran out of gas")
        break
    elif gas <= 2:
        print ("you are low on gas")

    #broken parts








