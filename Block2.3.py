import math
import random
#Написать мини калькулятор.
#
#В консоле ожидается ввод того символа, операцию которую мы будем выполнять.
#Операции: +, -, /, *, возведение в степень, модуль, рандомное число, факториал и арккосинус.
#Далее в консоль вводится столько значений, сколько требуется для операции. Для рандомного например 0.
#Выводим значение.

do = input("Введите символ операции (+, -, /, *, **, mod, rand, fact, arcc) : ")
while do != "exit":
    if do == "+":
        number1 = float(input("Введите 1 число: "))
        number2 = float(input("Введите 2 число: "))
        print(number1 + number2)
    elif do == "-":
        number1 = float(input("Введите 1 число: "))
        number2 = float(input("Введите 2 число: "))
        print(number1 - number2)
    elif do == "/":
        number1 = float(input("Введите 1 число: "))
        number2 = float(input("Введите 2 число: "))
        if number2 != 0:
            print(number1 / number2)
        else:
            print("На 0 делить нельзя!")
    elif do == "*":
        number1 = float(input("Введите 1 число: "))
        number2 = float(input("Введите 2 число: "))
        print(number1 * number2)
    elif do == "**":
        number1 = float(input("Введите число: "))
        number2 = float(input("Введите степень: "))
        print(number1**number2)
    elif do == "mod":
        number1 = float(input("ввести число: "))
        print(math.fabs(number1))
    elif do == "rand":
        print(random.randint(0, 1000))
    elif do == "fact":
        number1 = int(input("Введите  число: "))
        print(math.factorial(number1))
    elif do == "arcc":
        number1 = float(input("Введите число: "))
        number1 = number1*math.pi/180
        print(math.acos(number1))
    do = input("Введите символ операции ((+, -, /, *, **, mod, rand, fact, arcc) или введите exit, что бы закончить: ")