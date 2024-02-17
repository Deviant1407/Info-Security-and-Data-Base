import math

def Ex_1 (Name: str, Surname: str):
    print(f'Hello {Name} {Surname}! You have just delved into Python.') #Вставка имени и фамилии

Ex_1(input("Введите имя: "), input("Введите фамилию: "))
print("---")

def Ex_2 (Str: str):
    print(f'Футбольная команда {Str} имеет длинну {len(Str)} символов.') #Вставка строки и его длинны

Ex_2(input("Введите название команды: "))
print("---")

def Ex_3 (Sity_1: str, Sity_2: str, Sity_3: str):
    print(f'{min(Sity_1, Sity_2, Sity_3)}\n' #Поиск наименьшего названия
          f'{max(Sity_1, Sity_2, Sity_3)}') #Поиск наибольшего названия

Ex_3(input("Введите название города: "), input("Введите название города: "), input("Введите название города: "))
print("---")

def Ex_4 (Str_1: str, Str_2: str, Str_3: str):
    Str_1 = len(Str_1) #Получение длинны первого значения
    Str_2 = len(Str_2) #Получение длинны второго значения
    Str_3 = len(Str_3) #Получение длинны третьего значения

    R_Str_1 = Str_2 - Str_1 #Разница между вторым и первым значением
    R_Str_2 = Str_3 - Str_2 #Разница между третьем и вторым значением

    if R_Str_1 == R_Str_2:
        print("Yes")
    else:
        print("No")

Ex_4(input("Введите строку: "), input("Введите строку: "), input("Введите строку: "))
print("---")

def Ex_5 (Str: str):
    if Str in "синий": #Если в строке есть "синий"
        print("Yes")
    else:
        print("No")

Ex_5(input("Введите строку: "))
print("---")

def Ex_6 (Str: str):
    if Str in ("суббота", "воскресенье"): #Если в строке есть "суббота" или "воскресенье"
        print("Yes")
    else:
        print("No")

Ex_6(input("Введите строку: "))
print("---")

def Ex_7 (Email: str):
    if Email in ("@", "."):
        print("Yes")
    else:
        print("No")

Ex_7(input("Введите email: "))
print("---")

def Ex_8 (x1: float, y1: float, x2: float, y2: float):
    p = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) #Формула евклидового расстояния
    print(p)

Ex_8(float(input("Введите число: ")), float(input("Введите число: ")), float(input("Введите число: ")), float(input("Введите число: ")))
print("---")

def Ex_9 (R: float):
    print(f'{3.14 * R ** 2}\n' #Форула площади
          f'{2 * 3.14 * R}') #Формула периметра

Ex_9(float(input("Введите число: ")))
print("---")

def Ex_10 (a: float, b: float):
    print(f'{(a + b) / 2}\n' #Среднее орифмитическое
          f'{math.sqrt(a * b)}\n' #Среднее геометрическое
          f'{(2 * a * b) / (a + b)}\n' #Среднее гармоническое
          f'{math.sqrt((a ** 2 + b ** 2)/2)}') #Среднее квадратичное

Ex_10(float(input("Введите число: ")), float(input("Введите число: ")))
print("---")