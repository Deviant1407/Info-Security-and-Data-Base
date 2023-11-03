def Ex_1 (a: int):
    a1 = a // 1000
    a2 = (a // 100) % 10
    a3 = (a // 10) % 10
    a4 = (a // 1) % 10

    print(f'Цифра в позиции тысяц равна {a1}\n'
          f'Цифра в позиции сотен равна {a2}\n'
          f'Цифра в позиции десятков равна {a3}\n'
          f'Цифра в позиции единиц равна {a4}')

Ex_1(3281)
print("---")

def Ex_2 (True_Pasword: str, User_Pasword: str):
    if User_Pasword == True_Pasword:
        return "Пароль принят!"
    else:
        return "Пароль не принят!"

print(Ex_2("qwerty","qwerty"))
print("---")

def Ex_3 (a: int):
    if a % 2 == 0:
        return "Чётное"
    else:
        return "Нечётное"

print(Ex_3(10))
print("---")

def Ex_4 (a: int):
    a1 = a // 1000
    a2 = (a // 100) % 10
    a3 = (a // 10) % 10
    a4 = (a // 1) % 10

    if (a1 + a4) == (a2 - a3):
        return "Да"
    else:
        return "Нет"

print(Ex_4(1614))
print("---")

def Ex_5 (a: int):
    if a >= 18:
        return "Доступ разрещён!"
    else:
        return "Доступ запрещён!"

print(Ex_5(18))
print("---")

def Ex_6 (a: int, b: int, c: int):
    if ((a + 1) == b) and ((b + 1) == c):
        print("Да")
    else:
        print("Нет")

Ex_6(1, 2, 3)
print("---")

def Ex_7 (a: int, b: int):
    print(f'{min(a, b)}')

Ex_7(8, 11)
print("---")

def Ex_8 (a: int, b: int, c: int, d: int):
    print(f'{min(a,b,c,d)}')

Ex_8(1, 2, 3, 4)
print("---")

def Ex_9 (a: int):
    if a in range(0, 13):
        print("Детство")
    elif a in range(14, 24):
        print("Молодость")
    elif a in range(25, 59):
        print("Зрелось")
    else:
        print("Старость")

Ex_9(18)
print("---")

def Ex_10 (a: int, b: int, c: int):
    a1 = False
    a2 = False
    a3 = False

    List = []

    if a >= 0:
        a1 = True
    if b >= 0:
        a2 = True
    if c >= 0:
        a3 = True

    if a1 == True:
        List.append(a)
    if a2 == True:
        List.append(b)
    if a3 == True:
        List.append(c)

    summ = sum(List)
    print(summ)

Ex_10(1, -22, 5)
print("---")