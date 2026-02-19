"""
Реализуем класс TaskManager для управления задачами с приоритетами. Каждая задача имеет:

id (уникальный идентификатор)
name (название)
priority (приоритет: 1 - высший, 3 - низший)
Требования к классу:

add_task(id: str, name: str, priority: int) – добавляет задачу
get_next_task() -> dict – возвращает и удаляет задачу с наивысшим приоритетом (если приоритеты равны, выбирается первая добавленная)
remove_task(id: str) – удаляет задачу по id
get_tasks_sorted() – возвращает задачи, отсортированные по приоритету (без удаления)

Пример:

manager = TaskManager()
manager.add_task("T1", "Проверить сервер", 2)
manager.add_task("T2", "Починить базу", 1)
manager.add_task("T3", "Написать код", 2)

print(manager.get_next_task())  # {"id": "T2", "name": "Починить базу", "priority": 1}
print(manager.get_tasks_sorted())  # [{'id': 'T1', 'name': 'Проверить сервер', 'priority': 2}, {'id': 'T3', 'name': 'Написать код', 'priority': 2}]
"""

import queue
from itertools import count
counter = count()
class TaskManager:

    def __init__(self):
        self.tasks = []
        self.queue = queue.PriorityQueue()
        self.id = ""

    def add_task(self, id: str, name: str, priority: int):
        self.queue.put((priority, next(counter), id, name))
        self.tasks.append({'id' : id, 'name' : name, 'priority' : priority})
        #print(self.tasks)

    def get_next_task(self) -> dict:
        while not self.queue.empty():
            task = self.queue.get()
            self.id = task[2]
            task_priority = {"id": task[2], "name": task[3], "priority": task[0]}
            self.remove_task(self.id)
            return task_priority

    def remove_task(self, id: str):
        for task in self.tasks:
            if task['id'] == id:
                self.tasks.pop(self.tasks.index(task))

    def get_tasks_sorted(self):
        self.tasks.sort(key=lambda x: x['priority'])
        return self.tasks



manager = TaskManager()
manager.add_task("T1", "Проверить сервер", 2)
manager.add_task("T2", "Выучить Python", 1)
manager.add_task("T3", "Обновить Windows", 3)
manager.add_task("T4", "Написать код", 2)
manager.add_task("T5", "Помайнить", 3)
manager.add_task("T6", "Решить задачу", 1)

print(manager.get_next_task())  # {'id': 'T2', 'name': 'Выучить Python', 'priority': 1}
print(manager.get_next_task())  # {'id': 'T6', 'name': 'Решить задачу', 'priority': 1}
print(manager.get_next_task())  # {'id': 'T1', 'name': 'Проверить сервер', 'priority': 2}
manager.remove_task("T5")
print(manager.get_tasks_sorted())  # [{'id': 'T4', 'name': 'Написать код', 'priority': 2}, {'id': 'T3', 'name': 'Обновить Windows', 'priority': 3}]



"""
manager = TaskManager()
manager.add_task("T1", "Проверить сервер", 2)
manager.add_task("T2", "Починить базу", 1)
manager.add_task("T3", "Написать код", 2)

print(manager.get_next_task())  # {"id": "T2", "name": "Починить базу", "priority": 1}

print(manager.get_tasks_sorted())  # [{'id': 'T1', 'name': 'Проверить сервер', 'priority': 2}, {'id': 'T3', 'name': 'Написать код', 'priority': 2}]"""
