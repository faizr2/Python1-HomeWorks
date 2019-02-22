# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

#number = float(input("numerical request: "))

num=float(input("Введите число, которое необходимо округлить: "))
dig=int(input("Введите количествознаков, до которых необходимо округлить: "))

def my_round(number, digits):
  multipl = 10.0**digits
  return int (number*multipl + 0.5) / multipl

print('округленное число = ', my_round(num,dig))

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

#def lucky_ticket(ticket_number):
#    pass


#print(lucky_ticket(123006))
#print(lucky_ticket(12321))
#print(lucky_ticket(436751))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    tick_list=str(ticket_number)
    if len(tick_list) != 6: return False
    first=0
    last=0
    for i in range(3):
        first+=int(tick_list[i])
        last+=int(tick_list[-i-1])
    return first==last

def test(got, expected):
    prefix = "OK" if got == expected else "X"
    print("{0} - Получено: {1} | Ожидалось: {2}".format(prefix, repr(got), repr(expected)))

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
