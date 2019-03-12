
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
total = 0

for i in range (7):
    if number1 >= 1:
        positive += 1
    elif number1 == 0:
        zero += 1
    else:
        negative += 1
    i+=1
print("number of positive:", positive)
print("number of zeros:", zero)
print("number f negatives:", negative)
