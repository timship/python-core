"""
Класс космического объекта SpaceObject
(данный класс будет являться для нас базовым,
все последующие объекты должны будут наследоваться от него)
который будет иметь следующие свойства:

1. Конструктор объекта, в котором в аргументах передается масса объекта
2. weight - масса, которая будет определяться в момент создания объекта, не подлежит изменению, но доступен для чтения
3. absorbed - свойство возвращающее True/False по умолчанию, и символизирующее признак поглощения объекта кем-то другим,
при создании объекта устанавливается в False
4. mark_absorbed - метод объекта изменяющий его признак absorbed на True и устанавливающий массу в ноль

Класс планеты Planet который будет иметь следующие свойства:

1. Конструктор объекта в котором в аргументах передается масса планеты
2. Планеты могут сталкиваться, друг с другом и создавать новые,
при этом считаем что их массы будут объединены, поэтому для них должна работать операция сложения Planet(100) + Planet(200)
3. Планеты являются космическими объектами


Класс BlackHole который будет иметь следующие свойства:

1. BlackHole это тоже SpaceObject
2. При инициализации BlackHole создается с нулевой массой
3. BlackHole может поглотить любой SpaceObject, при этом масса поглощенного объекта перейдет к BlackHole,
а для него станет равна нулю и он будет отмечен поглощенным.
В коде решения передайте все классы.

Пример проверки:

s_obj = SpaceObject(10)
print(s_obj.weight)   # 10
print(s_obj.absorbed) # False
s_obj.mark_absorbed()
print(s_obj.absorbed) # True
res = Planet(100) + Planet(200)
print(res.weight)     # 300

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
