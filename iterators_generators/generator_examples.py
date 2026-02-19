"""
Реализуем функцию-генератор generate_values(f, start_x, end_x, step),
которая будет создавать генератор значений функции f(x) на заданном промежутке [start_x, end_x] с шагом step.

При реализации для точности сравнений чисел выполняйте округления до 2-ого знака после запятой.

"""

def generate_values(f, start_x, end_x, step):
    x = start_x
    while round(x, 2) <= end_x:
        yield f(x)
        x += step

f1 = lambda x: 2*x + 1

gen1 = generate_values(f1, 0, 1, 0.1)
values1 = []
for y in gen1:
    values1.append(round(y,2))
print(values1) # result = [1, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0]

gen2 = generate_values(f1, 0, 2, 0.1)
values2 = []
for y in gen2:
    values2.append(round(y,2))
print(values2) # result = [1, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0]






