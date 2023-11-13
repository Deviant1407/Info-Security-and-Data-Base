# Контрольная работа 13.11.2023
def K_Ex_10(a: int, b: int):
    print("*" * b, sep="\n")
    for i in range(a - 2):
        print("*" + " " * (b - 2) + "*")
    print("*" * b, sep="\n")

K_Ex_10(int(input("Введите A: ")), int(input("Введите B: ")))
print("---")

def K_Ex_11(a: int, b: int):
    print(f'Квадрат суммы {a} и {b} равен {(a + b) ** 2}')
    print(f'Сумма квадратов {a} и {b} равна {(a ** 2) + (b ** 2)}')

K_Ex_11(int(input("Введите A: ")), int(input("Введите B: ")))
print("---")

def K_Ex_12(a: int, b: int, c: int, d: int):
    print(((a ** b) + (c ** d)))

K_Ex_12(int(input("Введите A: ")), int(input("Введите B: ")), int(input("Введите C: ")), int(input("Введите D: ")))
print("---")

def K_Ex_13(n: int):
    if 1 <= n <= 9:
        print(f'{n}{n+n}{n+n+n}')
    else:
        print("Ошибка! Число не находится в диапазоне от 1 до 9!")

K_Ex_13(int(input("Введите N: ")))