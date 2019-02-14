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