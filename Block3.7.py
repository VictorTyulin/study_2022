#Сделать из функций калькулятора отдельный класс.
import math
import random

class Calculator:
    def plus(self, number1, number2):
        return number1 + number2

    def minus(self, number1, number2):
        return number1 - number2

    def div(self, number1, number2):
        if number2 != 0:
            return number1 / number2
        else:
            print("на 0 делить нельзя")

    def multi(self, number1, number2):
        return number1 * number2

    def pow(self, number1, number2):
        return number1 ** number2

    def rand(self, number1, number2):
        return random.uniform(number1, number2)

    def mod(self, number1):
        return math.fabs(number1)

    def factorial(self, number1):
        return math.factorial(number1)

    def arccos(self, number1):
        return number1*math.pi/180

calc = Calculator()
do = input("Введите символ операции ((+, -, /, *, **, mod, rand, fact, arcc): ")
while do != "exit":
    if do == "+":
        print(calc.plus(number1=float(input("Введите 1 число: ")),number2 = float(input("Введите 2 число: "))))

    elif do == "-":
        print(calc.minus(number1=float(input("Введите 1 число: ")), number2=float(input("Введите 2 число: "))))

    elif do == "/":
        print(calc.div(number1=float(input("Введите 1 число: ")), number2=float(input("Введите 2 число: "))))

    elif do == "*":
        print(calc.multi(number1=float(input("Введите 1 число: ")), number2=float(input("Введите 2 число: "))))
