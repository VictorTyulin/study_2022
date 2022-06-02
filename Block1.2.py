#Ввести произвольную строку в консоль
str = 'I am a student of Pskov State University'
print("Произвольная строка: " + str)
#Циклом пройтись по всем символам этой строки.
#Пропустить 3-й символ.
one_str = str.replace('a', '', 1)
print("Пропущен 3 символ в строке: " + one_str)
#Если есть символ "c", вывести сообщение об этом.
print("В строке есть символ c?: ", + str.find("c") !=-1)
#Функция вывода длины строк
str = 'I am a student of Pskov State University'
print("Длинна строки= ", + len(str))
#Не выводить последний символ в строке
str = 'I am a student of Pskov State University'
two_str =str[:-1]
print("В строке не показывать пследний символ: " + two_str)