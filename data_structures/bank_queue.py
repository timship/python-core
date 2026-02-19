"""
Реализуем систему обработки очереди в банковском отделении. 
Клиенты приходят в случайном порядке, но система должна обрабатывать их в порядке поступления (FIFO), 
однако среди клиентов есть со статусом VIP, которые имеют более высокий приоритет в обслуживании чем приоритетные.

Реализуем класс ClientsQueue, который:

Добавляет новых клиентов в очередь. (push)
Добавляет новых VIP клиентов в очередь приоритетных клиентов. (push_vip)
Позволяет забрать клиента из очереди (next), None если клиенты закончились.
Проверить что очередь пустая. (is_empty)
Узнать количество клиентов в ожидании. (get_queue_size)
Пример:

queue = ClientsQueue()
queue.push("Иванов Иван Иванович")
queue.push("Петров Петр Петрович")
queue.push_vip("Сергеев Сергей Сергеевич")

print(queue.get_queue_size()) # 3
print(queue.next()) # Сергеев Сергей Сергеевич
print(queue.next()) # Иванов Иван Иванович
print(queue.next()) # Петров Петр Петрович
print(queue.is_empty()) # True
"""
import queue
from itertools import count

class ClientsQueue:
    def __init__(self):
        self.queue = queue.PriorityQueue()
        self.counter = count()

    def push(self, client: str):
        self.queue.put((2, next(self.counter), client))

    def push_vip(self, client: str):
        self.queue.put((1, next(self.counter), client))

    def get_queue_size(self) -> int:
        self.queue.qsize()
        return self.queue.qsize()

    def next(self) -> str:
        if self.queue.empty():
            return None
        else:
            return self.queue.get()[2]

    def is_empty(self) -> bool:
        return self.queue.empty()

queue = ClientsQueue()
queue.push("Иванов Иван Иванович")
queue.push("Петров Петр Петрович")
queue.push_vip("Сергеев Сергей Сергеевич")

print(queue.get_queue_size()) # 3
print(queue.next()) # Сергеев Сергей Сергеевич
print(queue.next()) # Иванов Иван Иванович
print(queue.next()) # Петров Петр Петрович

print(queue.is_empty()) # True
