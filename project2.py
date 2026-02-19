"""
Задание №2
Реализуйте класс SubscriptionManager для управления подписками пользователей на различные категории контента. Каждый пользователь может подписываться или отписываться от категорий, а система должна быстро отвечать на вопросы о подписках.

Требования к классу:

1.	subscribe(user_id: str, category: str) – добавляет подписку на категорию для пользователя
2.	unsubscribe(user_id: str, category: str) – удаляет подписку (если она была)
3.	get_user_subscriptions(user_id: str) -> set – возвращает все подписки пользователя
4.	get_category_subscribers(category: str) -> set – возвращает всех подписчиков категории
5.	is_subscribed(user_id: str, category: str) -> bool – проверяет, есть ли подписка

Пример:

manager = SubscriptionManager()

manager.subscribe("user1", "sports")
manager.subscribe("user1", "music")
manager.subscribe("user2", "sports")

print(manager.get_user_subscriptions("user1"))  # {"sports", "music"}
print(manager.get_category_subscribers("sports"))  # {"user1", "user2"}
print(manager.is_subscribed("user2", "music"))  # False

manager.unsubscribe("user1", "music")
print(manager.get_user_subscriptions("user1"))  # {"sports"}

"""

class SubscriptionManager:
    def __init__(self):
        self.graph = {}

    def subscribe(self, user_id: str, category: str):
        if category not in self.graph:
            new_list = []
            new_list.append(user_id)
            self.graph[category] = new_list
        else:
            self.graph[category].append(user_id)
        print(self.graph)

    def unsubscribe(self, user_id: str, category: str):
        if category not in self.graph:
            pass
        else:
            self.graph[category].remove(user_id)

    def get_user_subscriptions(self, user_id: str) -> set:
        user_subscriptions = set()
        for category, new_list in self.graph.items():
            if user_id in new_list:
                user_subscriptions.add(category)
        return user_subscriptions

    def get_category_subscribers(self, category: str) -> set:
        category_subscriptions = set()
        for key, new_list in self.graph.items():
            if category in self.graph:
                category_subscriptions = set(self.graph[category])
        return category_subscriptions


    def is_subscribed(self, user_id: str, category: str):
        return user_id in self.get_category_subscribers(category)


manager = SubscriptionManager()

manager.subscribe("user1", "sports")
manager.subscribe("user1", "music")
manager.subscribe("user2", "sports")

print(manager.get_user_subscriptions("user1"))  # {"sports", "music"}
print(manager.get_category_subscribers("sports"))  # {"user1", "user2"}
print(manager.is_subscribed("user2", "music"))  # False

manager.unsubscribe("user1", "music")
print(manager.get_user_subscriptions("user1"))  # {"sports"}