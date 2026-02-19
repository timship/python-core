"""
Используя и не изменяя классы из предыдущего шага, добавьте класс BlackHole со следующими свойствами:

1. BlackHole это тоже SpaceObject
2. При инициализации BlackHole создается с нулевой массой
3. BlackHole может поглотить любой SpaceObject, при этом масса поглощенного объекта перейдет к BlackHole,
а для него станет равна нулю и он будет отмечен поглощенным.
В коде решения передайте все классы.

Пример проверки:


black_hole = BlackHole()

print(black_hole.weight) # 0
p1 = Planet(100)
p2 = Planet(200) + Planet(300)
black_hole.absorb(p1)
print(black_hole.weight) # 100
black_hole.absorb(p2)
print(black_hole.weight) # 600

print(p1.absorbed) # True
print(p2.absorbed) # True
print(p1.weight)   # 0
print(p2.weight)   # 0
"""


class SpaceObject:
    def __init__(self, weight: int):
        self.__weight = weight
        self.__absorbed = False

    @property
    def weight(self):
        return self.__weight

    @property
    def absorbed(self):
        return self.__absorbed

    def mark_absorbed(self):
        self.__absorbed = True
        self.__weight = 0

class Planet(SpaceObject):
    def __init__(self, weight: int):
        super().__init__(weight)

    def __add__(self, other: 'Planet'):
        planet1 = self.weight
        planet2 = other.weight
        return Planet(planet1 + planet2)

class BlackHole(SpaceObject):
    def __init__(self):
        super().__init__(0)

    def absorb(self, other: SpaceObject):
        if not other.absorbed:
            self._SpaceObject__weight += other.weight
            other.mark_absorbed()

black_hole = BlackHole()

print(black_hole.weight) # 0
p1 = Planet(100)
p2 = Planet(200) + Planet(300)
black_hole.absorb(p1)
print(black_hole.weight) # 100
black_hole.absorb(p2)
print(black_hole.weight) # 600

print(p1.absorbed) # True
print(p2.absorbed) # True
print(p1.weight)   # 0
print(p2.weight)   # 0


"""
class SpaceObject:
    def __init__(self, weight):
        self.__weight = weight
        self.__absorbed = False
    
    @property
    def weight(self):
        return self.__weight
    
    @property
    def absorbed(self):
        return self.__absorbed
    
    def mark_absorbed(self):
        self.__absorbed = True
        self.__weight = 0


class Planet(SpaceObject):
    def __init__(self, weight):
        super().__init__(weight)
    
    def __add__(self, other):
        return Planet(self.weight + other.weight)


class BlackHole(SpaceObject):
    def __init__(self):
        super().__init__(0)

    def absorb(self, object: SpaceObject):
        super().__init__(self.weight + object.weight)
        object.mark_absorbed()
"""