def Ex_1 (x1: int, y1: int, x2: int, y2: int):
    if x1 == x2 or y1 == y2:
        print("Yes")
    else:
        print("No")

Ex_1(int(input("Введите X1: ")), int(input("Введите Y1: ")), int(input("Введите X2: ")), int(input("Введите Y2: ")))
print("---")

def Ex_2 (x1: int, y1: int, x2: int, y2: int):
    if (((x1 + 1 == x2) and (y1 + 1 == y2)) or #1;1
        ((x1 - 1 == x2) and (y1 - 1 == y2)) or #-1;-1
        ((x1 + 1 == x2) and (y1 == y2)) or #1;0
        ((x1 == x2) and (y1 + 1 == y2)) or #0;1
        ((x1 - 1 == x2) and (y1 == y2)) or #-1;0
        ((x1 == x2) and (y1 - 1 == y2)) or #0;-1
        ((x1 - 1 == x2) and (y1 + 1 == y2)) or #-1;1
        ((x1 + 1 == x2) and (y1 - 1 == y2))): #1;-1
        print("Yes")
    else:
        print("No")

Ex_2(int(input("Введите X1: ")), int(input("Введите Y1: ")), int(input("Введите X2: ")), int(input("Введите Y2: ")))
print("---")

def Ex_3 (n: int, k: int):
    if n > k:
        print("No")
    else:
        print("Yes")

Ex_3(int(input("Введите скорость Зума: ")),int(input("Введите скорость Флеша: ")))
print("---")

def Ex_4 (a: int, b: int, c: int):
    if a == b == c: #Все стороны равны
        print("Равносторонний")
    elif a == b != c: #Только 2 стороны равны
        print("Равнобедренный")
    elif a != b != c: #Никакая сторона не равна
        print("Разносторонний")

Ex_4(int(input("Введите длинну A: ")), int(input("Введите длинну B: ")), int(input("Введите длинну C: ")))
print("---")

def Ex_5 (a: int, b: int, c: int):
    List = [a, b, c]

    Min = min(List)
    Max = max(List)

    List.pop(List.index(Min))
    List.pop(List.index(Max))

    medium = List[0]

    print(medium)

Ex_5(int(input("Введите A: ")), int(input("Введите B: ")), int(input("Введите C: ")))
print("---")

def Ex_6 (m: int):
    if (m % 2 != 0 and 0 < m < 7) or (m % 2 == 0 and 8 <= m <= 12):
        print("31")
    elif (m % 2 == 0 and 2 < m <7) or (m % 2 != 0 and 8 < m < 12):
        print("30")
    elif m == 2:
        print("28")

Ex_6(int(input("Введите месяц: ")))
print("---")

def Ex_7 (mass: int):
    if mass <= 60:
        print("Лёгкий вес")
    elif 60 < mass < 64:
        print("Первый полусредний вес")
    elif 64 <= mass < 69:
        print("Полусредний вес")

Ex_7(int(input("Введите вес: ")))
print("---")

def Ex_8 (one_color: str, two_color: str):
    if (one_color in ("красный", "синий", "жёлтый")) and (two_color in ("красный", "синий", "жёлтый")):
        if one_color == "красный" and two_color == "синий":
            print("фиолетовый")
        elif one_color == "красный" and two_color == "жёлтый":
            print("оранжевый")
        elif one_color == "синий" and two_color == "жёлтый":
            print("зелёный")
    else:
        print("Ошибка!!!!")

Ex_8(input("Введите первый цвет: "), input("Введите второй цвет: "))
print("---")

def Ex_9 (number: int):
    if number <= 36:
        if number == 0:
            print("зелёный")

        elif number in range(1, 10):
            if number % 2 != 0:
                print("чёрный")
            else:
                print("красный")

        elif number in range(11, 18):
            if number % 2 != 0:
                print("красный")
            else:
                print("чёрный")

        elif number in range(19, 28):
            if number % 2 != 0:
                print("чёрный")
            else:
                print("красный")

        elif number in range(29, 36):
            if number % 2 != 0:
                print("красный")
            else:
                print("чёрный")
    else:
        print("Ошибка ввода!")

Ex_9(int(input("Введите число от 0 до 36: ")))
print("---")