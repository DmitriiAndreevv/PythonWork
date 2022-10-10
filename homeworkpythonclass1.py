

# 1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет


# a = int (input(f'Введите день недели: '))
# if a > 7 or a < 1:
#     print('ввод неверный')
# elif a == 6 or a == 7:
#     print('да')
# else:
#     print('нет')


# 1.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# from cgitb import reset
# from turtle import right
# from unittest import result


# def inputNumbers(b):
#     predicat = ["x", "y", "z"]
#     a = []
#     for i in range(b):
#         a.append(input(f"Введите число {predicat[i]}: "))
#     return a

# def predicatCheck(b):
#     left = not(b[0] or b[1] or b[2])
#     right = not b[0] and not b[1] and not b[2]
#     result = left == right
#     return result

# statment = inputNumbers(3)

# if predicatCheck(statment) == True:
#     print(f"истина")
# else:
#     print(f"ложь")



# 2.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input('введите число x: '))
# y = int(input('введите число y: '))

# if x > 0 and y > 0:
#     print(f'кординаты x = {x} и y = {y} точка находится в 1-й плоскости.')
# elif x < 0 and y > 0:
#     print(f'кординаты x = {x} и y = {y} точка находится во 2-й плоскости.')
# elif x < 0 and y < 0:
#     print(f'кординаты x = {x} и y = {y} точка находится в 3-й плоскотси. ')
# elif x > 0 and y < 0:
#     print(f'кординаты x = {x} and y = {y} точка находится в 4-ой плоскости.')






# 1.Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# a = int(input('введите номер четверти:  '))
# if a < 1 or a > 4:
#     print('введен неверный номер четверти')
# elif a == 1: print('x > 0 and y > 0')
# elif a == 2: print('x < 0 and y < 0')
# elif a == 3: print('x < 0 and y > 0')
# elif a == 4: print('x > 0 and y < 0')





# 2.Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


# import math                           а что за импорт math и numbers, это необходимая часть или можно уберать ?
# import numbers


# a1 = float(input('введите число a по оси x: '))
# a = float(input('введите число a по оси y: '))
# b1 = float(input('введите число b по оси x: '))
# b = float(input('введите число b по оси y: '))

# numbers = round(math.sqrt((b - a)**2 + (b1 - a1)**2), 3)
# print(numbers)


