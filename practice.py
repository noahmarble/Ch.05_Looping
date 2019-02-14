import random
coin = random.randrange(2)
head = 0
tail = 0
if coin == 0:
    head += 1
    print("Heads!")
else:
    tail += 1
    print("Tails!")