# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# может можно и поизящнее, но с имеющимися знаниями не сообразила как

fruits=["яблоко", "банан", "киви", "арбуз"]
i=0  # мне же номер всё равно надо выводить, так что я ввожу индекс, только для нумерации
for fruit in fruits:  # переменной fruit при каждой итерации(полном обороте) цикла присваиваются элементы поочереди
    i+=1
    print(i,'.', '{:>7}'.format(fruit))

# Подсказка: воспользоваться методом .format()


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

# смогла сделать только путем создания нового списка, так как если напрямую удалять в цикле for in,
# то пропускаются элементы из-за сдвига индекса от удаления

L1=["яблоко", "банан", "киви", "арбуз", "груша", "манго"]
L2=["яблоко", "банан", "киви", "арбуз"]
new_L1=[]     # создаю пустой список, чтоб складывать туда неповторяющиеся элементы
print("L1=", L1)
print("L2=", L2)

for item1 in L1:
    if item1 not in L2:
        new_L1.append(item1)
print("new_L1=", new_L1)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

from random import randint
L = [randint(1, 100) for i in range(5)]  # создаю произвольный список из 5 целых чисел.
NL=[]
print(L)
for num in L:
    if num % 2 == 0:
        NL.append(num/4)
    else:
        NL.append(num*2)
print(NL)

# более короткая запись 
NL2 = [num / 4 if num % 2 == 0 else num * 2 for num in L]
print(NL2)
