# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Triangles():
    def __init__(self, Ax, Ay, Bx, By, Cx, Cy):
        self.Ax = Ax
        self.Ay = Ay
        self.Bx = Bx
        self.By = By
        self.Cx = Cx
        self.Cy = Cy
        self.AB = round (math.sqrt(int (math.fabs(((By - Ay)**2) + ((Bx - Ax)**2)))),2)
        self.BC = round(math.sqrt(int(math.fabs(((Cy - By) ** 2) + ((Cx - Bx) ** 2)))), 2)
        self.CA = round(math.sqrt(int(math.fabs(((Ay - Cy) ** 2) + ((Ax - Cx) ** 2)))), 2)

    def perim(self):
        self.perim = (self.AB + self.BC + self.CA)
        return (self.perim)

    def SqTriang(self):
        self.perim /=2
        self.SqTriang =  round(math.sqrt(self.perim*(self.perim - self.AB)*(self.perim - self.BC)* (self.perim - self.CA)),2)
        return (self.SqTriang)

    def hghtTrngl(self):
        self.SqTriang *=2
        self.hghtTrngl =  round((self.SqTriang / self.CA),2)
        return (self.hghtTrngl)


my_tri = Triangles(2,2,5,8,7,4)


print('Длинна строны АВ = {}, ВС = {}, СА = {}'.format(my_tri.AB, my_tri.BC,my_tri.CA))
print('Периметр треугольника АВС равен {}'.format(my_tri.perim()))
print('Площадь треугольника АВС равна {}'.format(my_tri.SqTriang()))
print('Высота треугольника АВС, проведенная из угла В равна {}'.format(my_tri.hghtTrngl()))


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapez():
    def __init__(self, Ax, Ay, Bx, By, Cx, Cy, Dx, Dy):
        self.Ax = Ax
        self.Ay = Ay
        self.Bx = Bx
        self.By = By
        self.Cx = Cx
        self.Cy = Cy
        self.Dx = Dx
        self.Dy = Dy
        self.AB = round(math.sqrt(int(math.fabs(((By - Ay)**2) + ((Bx - Ax)**2)))), 2)
        self.BC = round(math.sqrt(int(math.fabs(((Cy - By)**2) + ((Cx - Bx)**2)))), 2)
        self.CD = round(math.sqrt(int(math.fabs(((Dy - Cy)**2) + ((Dx - Cx)**2)))), 2)
        self.DA = round(math.sqrt(int(math.fabs(((Ay - Dy)**2) + ((Ax - Dx)**2)))), 2)
        self.D1 = round(math.sqrt(int(math.fabs(((Cy - Ay)**2) + ((Cx - Ax)**2)))), 2)
        self.D2 = round(math.sqrt(int(math.fabs(((Dy - By)**2) + ((Dx - Bx)**2)))), 2)

        

    def perimTrapez(self):
        self.perimTrapez = (self.AB + self.BC + self.CD+self.DA)
        return (self.perimTrapez)

#    def hghtTrapez(self):
#        self.hghtTrapez =  .... слишком сложно получается. По идее надо попробовать из разных углов трапеции
#  даны ведь только координаты, а трапеция может оказаться перевернутой 
#       return (self.hghtTrngl)

# Площадь трапеции буду искать только через длины сторон
# кажется была формула получше, но не могу найти, придётся так, громоздко

    def SqTrapez(self):
        self.SqTrapez = round(((self.CD+self.BC)/2)*(math.sqrt((self.AB**2)-((((self.DA-self.CD)**2)+(self.AB**2)-(self.BC**2))/(2*(self.DA-self.CD))))), 2)
        return (self.SqTrapez)

# исхожу, что это всё-таки хоть какая-то трапеция, и где-то уже сделана проверка, входных данных
# что даны координаты именно четырех точек, и среди них нет совпадающих, одна сторона короче другой, есть две параллельные
# и т.д. Может потом доделаю, но пока времени не хватает.
# главное свойство равнобедренной трапеции, это что равны её диагонали.

    def chckTrapez(self):
        if self.D1 == self.D2:
            print("Трапеция равнобокая")
        else:
            print("Трапеция неравнобокая")


my_trapez1 = Trapez(0,0,2,2,4,2,6,0)

my_trapez1.chckTrapez()
print('Длинна строн трапеции АВ = {}, ВС = {}, СD = {}, DA = {}'.format(my_trapez1.AB, my_trapez1.BC,my_trapez1.CD,my_trapez1.DA))
print('Периметр трапеции АВСВ равен {}'.format(my_trapez1.perimTrapez()))
print('Площадь трапеции АВСВ равна {}'.format(my_trapez1.SqTrapez()))

my_trapez2 = Trapez(0,0,3,3,6,3,9,0)

my_trapez2.chckTrapez()
print('Длинна строн трапеции АВ = {}, ВС = {}, СD = {}, DA = {}'.format(my_trapez2.AB, my_trapez2.BC,my_trapez2.CD,my_trapez2.DA))
print('Периметр трапеции АВСВ равен {}'.format(my_trapez2.perimTrapez()))
print('Площадь трапеции АВСВ равна {}'.format(my_trapez2.SqTrapez()))
    
