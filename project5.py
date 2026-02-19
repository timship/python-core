"""
Задание №5
Реализуйте систему управления историей посещений браузера с возможностью отмены (undo) и возврата (redo) действий. История должна вести себя как стек, где каждая новая страница добавляется наверх, а при навигации "назад" (undo) мы возвращаемся к предыдущей странице.

Реализуйте класс BrowserHistory с методами:

visit(url: str) - добавляет URL в историю.
undo() -> str - возвращает предыдущий URL и удаляет текущий из истории (аналог "назад").
redo() -> str - возвращает следующий URL, если после undo не было новых visit (аналог "вперёд").
current() -> str - возвращает текущий URL
Если история пуста, методы должны возвращать None
После вызова visit вся "будущая" история (после undo) должна очищаться
Пример:

history = BrowserHistory()
history.visit("https://google.com")
history.visit("https://youtube.com/watch?v=dQw4w9WgXcQ")
history.visit("https://github.com")

print(history.current())  # https://github.com
print(history.undo())  # https://youtube.com/watch?v=dQw4w9WgXcQ
print(history.undo())  # https://google.com
print(history.redo())  # https://youtube.com/watch?v=dQw4w9WgXcQ
history.visit("stackoverflow.com")
print(history.redo())  # None
"""

class BrowserHistory:
    def __init__(self):
        self.undo_stack = list()
        self.redo_stack = list()


    def visit(self, url: str):
        self.undo_stack.append(url)
        self.redo_stack.clear()

    def undo(self) -> str | None:
        if not self.undo_stack:
            return None
        url = self.undo_stack.pop()
        self.redo_stack.append(url)
        return self.undo_stack[-1] if self.undo_stack else None

    def redo(self) -> str | None:
        if not self.redo_stack:
            return None
        else:
            url = self.redo_stack.pop()
            self.undo_stack.append(url)
            return url

    def current(self) -> str | None:
        if not self.undo_stack:
            return None
        else:
            return self.undo_stack[-1]


history = BrowserHistory()
history.visit("https://google.com")
history.visit("https://youtube.com/watch?v=dQw4w9WgXcQ")
history.visit("https://github.com")

print(history.current())  # https://github.com
print(history.undo())  # https://youtube.com/watch?v=dQw4w9WgXcQ
print(history.undo())  # https://google.com
print(history.redo())  # https://youtube.com/watch?v=dQw4w9WgXcQ
history.visit("stackoverflow.com")
print(history.redo())  # None