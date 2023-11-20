import math

def Ex_1 (x: float):
	r = math.radians(x) #Получение радиан
	result = (math.sin(x) + math.cos(x) + math.tan(x) ** 2)
	print(result)

Ex_1(float(input("Введите число: ")))
print("---")

def Ex_2 (x: float):
	result = (math.ceil(x) + math.floor(x)) #Вычисление чисел...
	print(result)

Ex_2(float(input("Введите число: ")))
print("---")

def Ex_3 (a: float, b: float, c: float):
	Discr = b ** 2 - 4 * a * c #Дискриминант

	if (Discr > 0):
		Root_1 = ((-b + math.sqrt(Discr)) / (2*a)) #Первый корень
		Root_2 = ((-b - math.sqrt(Discr)) / (2*a)) #Второй корень
		print(Root_1, Root_2, sep="\n")
	elif (Discr == 0):
		Root = -b / (2*a) #Корень
		print(Root)
	else:
		print("Нет корней")

Ex_3(float(input("Введите число: ")), float(input("Введите число: ")), float(input("Введите число: ")))
print("---")

def Ex_4 (a: float, n: int):
	S = ((n * (a ** 2))/(4 * math.tan(math.pi/n)))
	print(S)

Ex_4(float(input("Введите число: ")), int(input("Введите число: ")))