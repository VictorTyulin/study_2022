#Вводим 3 произвольных слова. Например, название овощей.
#Выводим все 3 слова в нижнем регистре, в верхнем регистре, потом только первый символ в верхнем (есть отдельная функция для этого)
#Далее вводим кол-во каждого овоща.
#С помощью метода format выводим все данные в читаемом виде.

vegetable1 = input("первый овощ: ")
vegetable2 = input("второй овощ: ")
vegetable3 = input("третий овощ: ")
vegl1 = vegetable1.lower()
vegl2 = vegetable2.lower()
vegl3 = vegetable3.lower()
vegu1 = vegetable1.upper()
vegu2 = vegetable2.upper()
vegu3 = vegetable3.upper()
vegt1 = vegetable1.title()
vegt2 = vegetable2.title()
vegt3 = vegetable3.title()
print(vegl1, vegu1, vegt1)
print(vegl2, vegu2, vegt2)
print(vegl3, vegu3, vegt3)
vegetables1 = int(input("количество " + vegetable1 + ": "))
vegetables2 = int(input("количество " + vegetable2 + ": "))
vegetables3 = int(input("количество " + vegetable3 + ": "))
print("{} {} ({}, {})".format(vegetables1, vegl1, vegu1, vegt1))
print("{} {} ({}, {})".format(vegetables2, vegl2, vegu2, vegt2))
print("{} {} ({}, {})".format(vegetables3, vegl3, vegu3, vegt3))