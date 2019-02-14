'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
import random

head = 0
tail = 0
i = 0

while i < 50:
    i += 1
    coin = random.randrange(2)

    if coin == 0:
        head += 1
        print("Heads!")
    else:
        tail += 1
        print("Tails!")

print("heads value:",head)
print("tails value:",tail)








