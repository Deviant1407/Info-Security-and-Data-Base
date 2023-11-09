def Ex_1 (a: int):
    a_str = str(a)

    if len(a_str) == 4:
        a_P7 = a % 7
        a_P17 = a % 17

        if (a_P7 == 0) or (a_P17 == 0):
            print("Yes")
        else:
            print("No")
    else:
        print("No")

Ex_1(int(input("Введите число: ")))
print("---")

def Ex_2 (a: int, b: int, c: int):
    y1 = False
    y2 = False
    y3 = False

    if a + b > c:
        y1 = True

    if a + c > b:
        y2 = True

    if b + c > a:
        y3 = True

    if (y1 == True) and (y2 == True) and (y3 == True):
        print("Yes")
    else:
        print("No")

Ex_2(int(input("Введите A: ")), int(input("Введите B: ")), int(input("Введите C: ")))
print("---")

def Ex_3 (a: int):
    if ((a % 4 == 0) and (a % 100 != 0)) or (a % 400 == 0):
        print("Yes")
    else:
        print("No")

Ex_3(int(input("Введите год: ")))
print("---")