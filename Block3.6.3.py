#Переделываем задачу номер 3(калькулятор) на функции.
import math
import random

def plus(number1, number2):
    return number1 + number2

def minus(number1, number2):
    return number1 - number2

def div(number1, number2):
    if number2 != 0:
        return number1 / number2
    else:
        print("на 0 делить нельзя")

def multi(number1, number2):
    return number1 * number2

def pow(number1, number2):
    return number1 ** number2

def rand(number1, number2):
    return random.uniform(number1, number2)

def mod(number1):
    return math.fabs(number1)

def factorial(number1):
    return math.factorial(number1)

def arccos(number1):
    return number1*math.pi/180

do = input("Введите символ операции ((+, -, /, *, **, mod, rand, fact, arcc): ")
while do != "exit":
    if do == "+":
        print(plus(number1=float(input("Введите 1 число: ")),number2=float(input("Введите 2 число: "))))

    elif do == "-":
        print(minus(number1=float(input("Введите 1 число: ")), number2=float(input("Введите 2 число: "))))

    elif do == "/":
        print(div(number1=float(input("Введите 1 число: ")), number2=float(input("Введите 2 число: "))))

    elif do == "*":
        print(multi(number1=float(input("Введите 1 число: ")), number2=float(input("Введите 2 число: "))))

    elif do == "**":
        print(pow(number1=float(input("Введите число: ")), number2=float(input("Введите степень: "))))

    elif do == "mod":
        print(mod(number1=float(input("Введите число: "))))

    elif do == "rand":
        print(rand(number1=float(input("Введите 1 число: ")), number2=float(input("Введите 2 число: "))))

    elif do == "fact":
        print(factorial(number1=int(input("Введите число: "))))

    elif do == "arcc":
        print(math.acos(arccos(number1=float(input("Введите число: ")))))

    do = input("Введите символ операции ((+, -, /, *, **, mod, rand, fact, arcc): ")

