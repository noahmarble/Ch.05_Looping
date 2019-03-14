'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: ______________________
 1. Make the following program work.
   '''
print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
    x = int(input("Enter a number: "))
    total += x
print("The total is:", total)



'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for i in range(2,101,2):
    print(i)


'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
i = 10
while i > -1:
    print (i)
    i-=1
print("Blast Off!")


'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''

import random
number = random.randrange(1,11)
print(number)




'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the number entries equal to zero,
     and the number of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''


'''
number1 = int(input("give me a number:"))
number2 = int(input("give me a number:"))
number3 = int(input("give me a number:"))
number4 = int(input("give me a number:"))
number5 = int(input("give me a number:"))
number6 = int(input("give me a number:"))
number7 = int(input("give me a number:"))

sumofnumbers = number1+number2+number3+number4+number5+number6+number7
print("sum of numbers", sumofnumbers)

positive = 0
zero = 0
negative = 0

if number1 >= 1:
    positive += 1
elif number1 == 0:
    zero += 1
else:
    negative += 1

if number2 >= 1:
    positive += 1
elif number2 == 0:
    zero += 1
else:
    negative += 1

if number3 >= 1:
    positive += 1
elif number3 == 0:
    zero += 1
else:
    negative += 1

if number4 >= 1:
    positive += 1
elif number4 == 0:
    zero += 1
else:
    negative += 1

if number5 >= 1:
    positive += 1
elif number5 == 0:
    zero += 1
else:
    negative += 1

if number6 >= 1:
    positive += 1
elif number6 == 0:
    zero += 1
else:
    negative += 1

if number7 >= 1:
    positive += 1
elif number7 == 0:
    zero += 1
else:
    negative += 1
print("number of positive:", positive)
print("number of zeros:", zero)
print("number f negatives:", negative)
'''
positive = 0
zero = 0
negative = 0
sumofnumbers = 0
for i in range (7):
    number1 = int(input("give me a number:"))
    if number1 >= 1:
        positive += 1
    elif number1 == 0:
        zero += 1
    else:
        negative += 1
    i+=1
    sumofnumbers += number1
print("sum of numbers", sumofnumbers)
print("number of positive:", positive)
print("number of zeros:", zero)
print("number of negatives:", negative)