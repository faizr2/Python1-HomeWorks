
__author__ = 'Файзрахманова Ирина Сергеевна'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.
print('')
print('Задание 1')
print('')

# Модифицирую программу из "easy"

number = int(input('Пожалуйста, введите произвольное число: '))
i=0 # счетчик по цифрам в числе, раз не знаем заранее длину числа
bMax=0 
lenNumb=len(str(number))
while i < lenNumb:
    b = number // 10**i % 10
    if b>bMax:
       bMax=b
    i=i+1
print('Максимальная цифра в данном числе: ', bMax)
# получился обратный порядок, но раз порядок не важен, то так оставлю.


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

# Про кортежи прочитала в книге, уяснила, что это примочка и гордость Python 

print('')
print('Задание 2')
print('')


print('Меняю числа местами кортежами, хотя ещё смутно их понимаю:')

A = int(input('Пожалуйста, введите число A: '))
B = int(input('Пожалуйста, введите число B: '))
print('Ваши A = ', A, 'B = ', B)
A, B = B, A
print('Меняю местами: A = ', A, 'B = ', B)

# или

print('Меняю числа местами с помощью арифметики:')

A = int(input('Пожалуйста, ещё раз введите число A: '))
B = int(input('Пожалуйста, ещё раз введите число B: '))
print('Ваши A = ', A, 'B = ', B)
A=A+B
B=A-B
A=A-B
print('Меняю местами: A = ', A, 'B = ', B)


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

print('')
print('Задание 3')
print('')

import math
print('Вычисляю корни уравнения ax² + bx + c = 0')
print('Пожалуйста, последовательно введите коэффициенты a, b, c')
a = int(input('Пожалуйста, введите a: '))
b = int(input('Пожалуйста, введите b: '))
c = int(input('Пожалуйста, введите c: '))
D=b**2-4*a*c
x=-b/(2*a)
if D==0:
    print('Уравнение имеет один вещественный корень : x = ', x)
else:
    print('Уравнение имеет два кореня:')
    x1=x+math.sqrt(D)/(2*a)
    print('x1 = ', x1)
    x2=x-math.sqrt(D)/(2*a)
    print('x2 = ', x2)


