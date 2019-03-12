
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
