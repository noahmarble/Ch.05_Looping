print("this is a game of Roshambo")

#user input
userrps = int(input("\r\nenter 1 for rock, 2 for paper, and 3 for scissors. \r\n 'q' to quit"))
print("\r\nuser input:")
if userrps == 1:
    print("rock")
elif userrps == 2:
    print("paper")
else:
    print("scissors")

#computer input
print("comptuer input:")
import random
rps = random.randrange(1,4)

if rps == 1:
    print("rock")
elif rps == 2:
    print("Paper")
else:
    print("Scissors")

#result of match
print("\r\nresult:")

if userrps == 1:
    if rps == 2:
        print("you lost")
    else:
        print("you won")
elif userrps == 2:
    if rps == 3:
        print("you lost")
    else:
        print("you won")
elif userrps == 3:
    if rps == 1:
        print("you lost")
    else:
        print("you won")
else:
    print("Tie")