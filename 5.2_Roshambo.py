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
print("enter 1 for rock, 2 for paper, and 3 for scissors.")

userrps = input("Rock, Paper, or Scissors?")

import random
rps = random.randrange(3)

if rps == 0:
    print("Rock")
elif rps == 1:
    print("Paper")
else:
    print("Scissors")

