"""
Реализуем класс InventoryManager для учета товаров на складе. 
Каждый товар имеет уникальный артикул - item_id, название, цену и количество на складе. 
Система должна поддерживать базовые операции: добавление, продажа, проверка остатков.

Требования к классу:

add_item(item_id: str, name: str, price: float, quantity: int) – добавляет товар на склад (или увеличивает количество, если товар уже есть)
sell_item(item_id: str, quantity: int) – продает указанное количество товара (если есть в достаточном количестве), возвращает результат выполнения операции True/False
get_item_info(item_id: str) -> dict – возвращает информацию о товаре в виде словаря {"name": str, "price": float, "quantity": int}
get_low_stock_items(threshold: int = 5) -> dict – возвращает товары, количество которых меньше порога (по умолчанию 5)
get_total_inventory_value() -> float – вычисляет общую стоимость всех товаров на складе
Используем словарь для хранения товаров, где ключ – item_id, а значение – другой словарь с информацией о товаре

inventory = InventoryManager()

# Добавляем товары
inventory.add_item("A1", "Ноутбук", 50000, 10)
inventory.add_item("A2", "Смартфон", 30000, 15)

# Продаем товар
inventory.sell_item("A1", 3)  # Успешно
inventory.sell_item("A2", 20) # False

# Получаем информацию
print(inventory.get_item_info("A1"))  # {"name": "Ноутбук", "price": 50000, "quantity": 7}
print(inventory.get_low_stock_items(10))  # {"A1": 7} (ноутбуков осталось меньше 10)
print(inventory.get_total_inventory_value())  # 50000*7 + 30000*15 = 800000
"""
class InventoryManager:

    def __init__(self):
        self.items = {}

    def add_item(self, item_id: str, name: str, price: float, quantity: int) -> None:
        if item_id not in self.items:
            self.items[item_id] = {"name": name, "price": price, "quantity": quantity}
        else:
            self.items[item_id]["quantity"] += quantity

    def sell_item(self, item_id: str, quantity: int) -> bool:
        if item_id in self.items:
            if quantity <= self.items[item_id]["quantity"]:
                self.items[item_id]["quantity"] -= quantity
                return True
        else:
            return False


    def get_item_info(self, item_id: str) -> dict:
        if item_id not in self.items:
            return {"name": "", "price": 0, "quantity": 0}
        else:
            return self.items[item_id]

    def get_low_stock_items(self, threshold: int = 5) -> dict:
        low_stock_items = {}
        for item_id, item in self.items.items():
            if self.items[item_id]["quantity"] < threshold:
                low_stock_items[item_id] = self.items[item_id]["quantity"]
        return low_stock_items

    def get_total_inventory_value(self) -> float:
        total_inventory_value = 0
        for item_id in self.items:
            total_inventory_value += self.items[item_id]["price"] * self.items[item_id]["quantity"]
        return total_inventory_value

inventory = InventoryManager()

# Добавляем товары
inventory.add_item("A1", "Ноутбук", 50000, 10)
inventory.add_item("A2", "Смартфон", 30000, 15)
inventory.add_item("A3", "Телевизор", 44000, 21)
inventory.add_item("A4", "Холодильник", 62000, 8)

# Продаем товар
inventory.sell_item("A1", 3)  # True
inventory.sell_item("A2", 20) # False
inventory.sell_item("A3", 6) # True
inventory.sell_item("A4", 9) # False

# Получаем информацию
print(inventory.get_item_info("A1"))  # {"name": "Ноутбук", "price": 50000, "quantity": 7}
print(inventory.get_item_info("A3"))  # {'name': 'Телевизор', 'price': 44000, 'quantity': 15}
print(inventory.get_low_stock_items(10))  # {'A1': 7, 'A4': 8}
print(inventory.get_total_inventory_value())  # 1956000


"""
inventory = InventoryManager()

# Добавляем товары
inventory.add_item("A1", "Ноутбук", 50000, 10)
inventory.add_item("A2", "Смартфон", 30000, 15)

# Продаем товар
inventory.sell_item("A1", 3)  # Успешно
inventory.sell_item("A2", 20) # False

# Получаем информацию
print(inventory.get_item_info("A1"))  # {"name": "Ноутбук", "price": 50000, "quantity": 7}
print(inventory.get_low_stock_items(10))  # {"A1": 7} (ноутбуков осталось меньше 10)
print(inventory.get_total_inventory_value())  # 50000*7 + 30000*15 = 800000

"""
