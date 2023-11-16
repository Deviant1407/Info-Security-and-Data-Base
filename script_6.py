def Ex_1 (a: float):
    print(f'{a % 1}') #отделение дробной части от целой

Ex_1(float(input("Введите число: ")))
print("---")

def Ex_2 (a1: int, a2: int, a3: int, a4: int, a5: int):
    _min = min(a1, a2, a3, a4, a5) #Поиск минимального числа
    _max = max(a1, a2, a3, a4, a5) #Поиск максимального числа

    print(f'Наименьшее число: {_min}\n'
          f'Наибольшее число: {_max}')

Ex_2(int(input("Введите число: ")), int(input("Введите число: ")),
     int(input("Введите число: ")), int(input("Введите число: ")), int(input("Введите число: ")))
print("---")

def Ex_3 (a1: int, a2: int, a3: int):
    List = [a1, a2, a3] #Создание списка

    List.sort() #Сортировака от меньшего к большему
    List.reverse() #Переворот списка

    print(f'{List[0]}\n'
          f'{List[1]}\n'
          f'{List[2]}')

Ex_3(int(input("Введите число: ")), int(input("Введите число: ")), int(input("Введите число: ")))
print("---")

def Ex_4 (a: int):
    Str_a = str(a) #Изменение формата переменной

    Str_1 = int(Str_a[0]) #Первая цифра числа
    Str_2 = int(Str_a[1]) #Вторая цифра числа
    Str_3 = int(Str_a[2]) #Третья цифра числа

    _min = min(Str_1, Str_2, Str_3) #Поиск минимального числа
    _max = max(Str_1, Str_2, Str_3) #Поиск максимального числа
    _srd = 0

    if _min < Str_1 < _max: #Если первое число между минимальным и максимальным
        _srd = Str_1
    elif _min < Str_2 < _max: #Если второе число между минимальным и максимальным
        _srd = Str_2
    elif _min < Str_3 < _max: #Если третье число между минимальным и максимальным
        _srd = Str_3

    if (_max - _min == _srd):
        print("Интересное число")
    else:
        print("Неинтересное число")

Ex_4(int(input("Введите число: ")))
print("---")

def Ex_5 (a1: float, a2: float, a3: float, a4: float, a5: float):
    _sum = a1 + a2 + a3 + a4 + a5 #Общая сумма

    print(_sum)

Ex_5(float(input("Введите число: ")), float(input("Введите число: ")),
     float(input("Введите число: ")), float(input("Введите число: ")), float(input("Введите число: ")))
print("---")

def Ex_6 (x1: int, y1: int, x2: int, y2: int):
    M_rast = abs(x1 - x2) + abs(y1 - y2) #Вычисление расстояния

    print(M_rast)

Ex_6(int(input("Введите X1: ")), int(input("Введите Y1: ")), int(input("Введите X2: ")), int(input("Введите Y2: ")))
print("---")
