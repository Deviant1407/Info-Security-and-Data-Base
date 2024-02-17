def Ex_1 (a, b):
    c = 3 * (a + b) ** 3 + 275 * b ** 2 - 127 * a - 41
    return c


print(Ex_1(5, 6))
print("-----")


def Ex_2 (a):
    print(f'Следующее чилсло за числом {a} число: {a + 1} \n'
          f'Для числа {a} предыдущее число: {a - 1}')


Ex_2(20)
print("-----")


def Ex_3 (mon, blok, keyb, mouse, quality):
    summ = mon + blok + keyb + mouse
    summ_n = summ * quality

    return summ_n


print(Ex_3(12000, 15000, 2000, 200, 3))
print("-----")


def Ex_4 (a, b):
    print(f'{a} + {b} + {a + b}\n'
          f'{a} - {b} = {a - b}\n'
          f'{a} * {b} = {a * b}')


Ex_4(10, 7)
print("-----")