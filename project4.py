"""
Задание №4
Реализуйте функцию error_process(f, code) которая вызывает функцию f от аргумента code.
При вызове функции f возможны исключения.
Функция error_process должна возвращать следующие значения:

Строку Ошибка значения переменной - при исключении ValueError
Строку Ошибка типа данных - при исключении TypeError
Строку Ошибка вычислений - при исключении ZeroDivisionError
Строку Общая ошибка - при любых других исключениях
True - если никаких ошибок не произошло

Пример:
def internal_f(code):
    if code == 0:
        raise ValueError()
    if code == 1:
        raise TypeError()
    if code == 2:
        raise ZeroDivisionError()
    if code == 3:
        raise FileNotFoundError()

print(error_process(internal_f, 0)) # Ошибка значения переменной
print(error_process(internal_f, 1)) # Ошибка типа данных
print(error_process(internal_f, 2)) # Ошибка вычислений
print(error_process(internal_f, 3)) # Общая ошибка
print(error_process(internal_f, 5)) # True
"""

def error_process(f, code):
    try:
        f(code)
        return True
    except ValueError:
        return "Ошибка значения переменной"
    except TypeError:
        return "Ошибка типа данных"
    except ZeroDivisionError:
        return "Ошибка вычислений"
    except Exception:
        return "Общая ошибка"




def internal_f(code):
    if code == 0:
        raise ValueError()
    if code == 1:
        raise TypeError()
    if code == 2:
        raise ZeroDivisionError()
    if code == 3:
        raise FileNotFoundError()

print(error_process(internal_f, 0)) # Ошибка значения переменной
print(error_process(internal_f, 1)) # Ошибка типа данных
print(error_process(internal_f, 2)) # Ошибка вычислений
print(error_process(internal_f, 3)) # Общая ошибка
print(error_process(internal_f, 5)) # True