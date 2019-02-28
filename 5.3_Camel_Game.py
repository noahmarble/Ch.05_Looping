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
print("D. STOP for the night")
print("E. STATUS check")
print("F. HOPE for help")
print("Q. To quit\n")

print("the game is starting...\n")

#variables
done = False
milestraveled = 0
thirst = 0
gas = 10
brokenparts = 0
bigdude = -20

#command
while not done:
    print("A. do MAINTENANCE on the jeep")
    print("B. Ahead MODERATE SPEED")
    print("C. Ahead FULL SPEED")
    print("D. STOP for the night")
    print("E. STATUS check")
    print("F. HOPE for help")
    print("Q. To quit\n")

    #quit
    choice = input("What is your choice? ")
    if choice.lower() == ("q"):
        done = True


