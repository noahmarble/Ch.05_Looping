'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''

print("this is a game of Roshambo")
win = 0
loss = 0
game = True
while game:
    #user input
    userrps = str(input("\r\ntype'q'to quit\r\nenter 1 for rock, 2 for paper, and 3 for scissors."))

    if userrps == "q":
        print("win/loss:", win, "/", loss)
        game = False
        break

    print("user input:")
    if userrps == "1":
        print("rock")
    elif userrps == "2":
        print("paper")
    else:
        print("scissors")

    #computer input
    print("comptuer input:")
    import random
    rps = str(random.randrange(1,4))

    if rps == "1":
        print("rock")
    elif rps == "2":
        print("Paper")
    else:
        print("Scissors")

    #result of match


    if userrps == "1":
        if rps == "2":
            print("\r\nresult:")
            print("you lost")
            loss+=1
        elif rps == "3":
            print("\r\nresult:")
            print("you won")
            win+=1
        else:
            print("tie")


    elif userrps == "2":
        if rps == "3":
            print("\r\nresult:")
            print("you lost")
            loss+=1
        elif rps == "1":
            print("\r\nresult:")
            print("you won")
            win+=1
        else:
            print("tie")


    elif userrps == "3":
        if rps == "1":
            print("\r\nresult:")
            print("you lost")
            loss+=1
        elif rps == "2":
            print("\r\nresult:")
            print("you won")
            win+=1
        else:
            print("tie")