"""
Разработка класса TrafficLight, который будет иметь конструктор по умолчанию,
свойство light - возвращающее один из возможных цвет светофора в виде строки ["RED", "YELLOW", "GREEN"],
а так же метод change() изменяющий цвет светофора согласно алгоритму:
RED => YELLOW => GREEN
GREEN => YELLOW => RED

При инициализации класса, светофор находится в режиме красного цвета - RED.

Пример проверки:

trf_light = TrafficLight()
print(trf_light.light) # RED
trf_light.change()
print(trf_light.light) # YELLOW
trf_light.change()
print(trf_light.light) # GREEN
trf_light.change()
print(trf_light.light) # YELLOW
trf_light.change()
print(trf_light.light) # RED
trf_light.change()
print(trf_light.light) # YELLOW
trf_light.change()
print(trf_light.light) # GREEN
"""
from enum import Enum

class Color(Enum):
    RED = 0
    YELLOW = 1
    GREEN = 2

class TrafficLight:
    def __init__(self, light: Color = Color.RED.name):
        self._light = light
        self._i = 0
    @property
    def light(self):
        return self._light

    def change(self):
        if self._light == Color.RED.name:
            self._light = Color.YELLOW.name
            self._i = 1
        elif self._light == Color.YELLOW.name:
            if self._i == 1:
                self._light = Color.GREEN.name
            elif self._i == 2:
                self._light = Color.RED.name
                self._i = 0
        elif self._light == Color.GREEN.name:
            self._light = Color.YELLOW.name
            self._i = 2
trf_light = TrafficLight()
print(trf_light.light) # RED
trf_light.change()
print(trf_light.light) # YELLOW
trf_light.change()
print(trf_light.light) # GREEN
trf_light.change()
print(trf_light.light) # YELLOW
trf_light.change()
print(trf_light.light) # RED
trf_light.change()
print(trf_light.light) # YELLOW
trf_light.change()

print(trf_light.light) # GREEN
