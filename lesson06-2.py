"""
Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    length = None
    width = None
    weigth = 25
    tickness = 0.05

    def __init__(self, length, width):
        self.length = length
        self.width = width
        print(f'Создание объекта')

    def intake(self):
        self.length = 20
        self.width = 5000
        intake = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'Необходимо {intake} тонн асфальта')


road_to_village = Road(20, 5000)
road_to_village.intake()
