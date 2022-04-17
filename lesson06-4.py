"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'Автомобиль {self.name} едет.'

    def stop(self):
        return f'Автомобиль {self.name} остановился'

    def turn_right(self):
        return f'Автомобиль {self.name} повернул направо'

    def turn_left(self):
        return f'Автомобиль {self.name} повернул налево'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name} составляет {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} составляет {self.speed}')

        if self.speed > 40:
            return f'Скорость автомобиля {self.name} выше, чем допустима для городского типа транспорта'
        else:
            return f'Скорость автомобиля {self.name} разрешена для городского типа транспорта'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочего автомобиля {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'Скорость автомобиля {self.name} выше, чем допустима для рабочего типа транспорта'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из департамента полиции'
        else:
            return f'{self.name} не из департамента полиции'


audi = SportCar(100, 'красный цвет', 'Audi', False)
oka = TownCar(30, 'белый цвет', 'Oka', False)
lada = WorkCar(70, 'розовый цвет', 'Lada', True)
ford = PoliceCar(110, 'синий цвет', 'Ford', True)
print(lada.turn_left())
print(f'{oka.turn_right()}, {audi.stop()}')
print(f'{lada.go()} {lada.show_speed()}')
print(f'{lada.name} {lada.color}')
print(f'Автомобиль {audi.name} машина полиции? {audi.is_police}')
print(f'Автомобиль {lada.name} машина полиции? {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.police())
print(ford.show_speed())
