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
