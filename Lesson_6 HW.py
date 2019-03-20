# Создать класс треугольник и реализовать в нем конструктор, методы для вычисления (не печати, нужен return) площади, периметра  и вывод значений сторон треугольника на экран.
# В конструкторе сделать проверку на возможность создания такого треугольника, если нет, то написать, что такой треугольник нельзя создать и сделать exit(1)


class Triangle:
    def __init__(self, a, b, c):
        if max(a, b, c) >= (a + b + c -(max(a, b, c))):
            print("Треугольник нельзя создать")
            exit(1)
        self.a = a
        self.b = b
        self.c = c

    def per(self):
        print('Стороны:', self.a, self.b, self.c)
        return self.a + self.b + self.c

    def square(self):
        print('Стороны:',self.a, self.b, self.c)
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** (1 / 2)

myTriangle = Triangle(3, 4, 5)
print(myTriangle .per())
print(myTriangle.square())

# Задание-2:
#
# Написать класс, который будет удобно использовать для работы с (на выбор что-нибудь одно) комплексными числами \ матрицами \ светофор \ микроволновка

class microwave():
    def __init__(self, power, time):
        self.power = power
        self.time = time

    def cook(self):
        print('Время приготовления:', self.time, 'Мощность:', self.power)

myCook = microwave(700, 7).cook()







