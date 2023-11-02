def Ex_1 (b: int, q: int, n: int):
    b_n = b * q ** (n - 1)
    return b_n

print(Ex_1(1, 2, 5))
print("---")

def Ex_2 (a: int):
    return a // 100

print(Ex_2(345))
print("---")

def Ex_3 (n: int, k: int):
    K = n // k

    return K

print(Ex_3(3, 6))
print("---")

def Ex_4 (a: int):
    A = a % 2
    if A == 0:
        return a // 2
    else:
        return (a // 2) + 1

print(Ex_4(99))
print("---")

def Ex_5 (a: int):
    return a // 4 + 1

print(Ex_5(5))
print("---")

def Ex_6 (a: int):
    Hour = a // 60
    Min = a % 60

    print(f'{a} мин - это {Hour} часов {Min} минут.')

Ex_6(150)
print("---")

def Ex_7 (a: int):
    b = a % 10
    c = (a % 100) // 10
    d = (a % 1000) // 100

    print(f'Cумма цифр = {b + c + d}\n'
          f'Произведение цифр = {b * c * d}')

Ex_7(123)
print("---")

def Ex_8 (a: int):
    a = str(a)

    a1 = a[0]
    a2 = a[1]
    a3 = a[2]

    print(f'{a1}{a2}{a3}\n'
          f'{a1}{a3}{a2}\n'
          f'{a2}{a1}{a3}\n'
          f'{a2}{a3}{a1}\n'
          f'{a3}{a1}{a2}')

Ex_8(123)
print("---")