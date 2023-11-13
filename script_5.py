def Ex_1 (a1: int, b1: int, a2: int, b2: int):
    if a2 < a1:
        if b2 < a1:
            print("Пустое множество")

        elif b2 == a1:
            print(b2)

        elif a1 < b2 <= b1:
            print(a1, b2)

        elif b2 > b1:
            print(a1, b1)

    elif a2 == a1:
        if b2 <= b1:
            print(a2, b2)

        else:
            print(a2, b1)

    elif a2 < b1:
        if b2 <= b1:
            print(a2, b2)

        else:
            print(a2, b1)

    elif a2 == b1:
        print(a2)

    else:
        print("Пустое множество")

Ex_1(int(input("Введите A1: ")), int(input("Введите B1: ")), int(input("Введите A2: ")), int(input("Введите B2: ")))
print("---")

def Ex_2 (a: int, b: int):
    S = 0.5 * a * b
    print(S)

Ex_2(int(input("Введите A: ")), int(input("Введите B: ")))
print("---")

def Ex_3 (S: float, V1: float, V2: float):
    T = S / (V1 + V2)

    print(T)

Ex_3(float(input("Введите расстояние: ")), float(input("Введите скорость первой старушки: ")), float(input("Введите скорость второй старушки: ")))
print("---")

def Ex_4 (a: int):
    print(f'{a ** -1}')

Ex_4(int(input("Введите A: ")))
print("---")

def Ex_5 (F: float):
    print(f'{(5/9) * (F - 32)}')

Ex_5(float(input("Введите темпиратуру в форенгейтах: ")))
print("---")

def Ex_6 (Age: int):
    print(f'{Age * 10.5}')

Ex_6(int(input("Введите возраст: ")))
print("---")

def Ex_7 (a: float):
    print(f'{round(((a * 10) % 10), 0)}') #Я хз как это решить (

Ex_7(float(input("Введите число: ")))
print("---")