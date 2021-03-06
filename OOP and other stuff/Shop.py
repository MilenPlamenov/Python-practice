# from collections import defaultdict
#
#
# class Shop:
#     def __init__(self, name, type, capacity):
#         self.name = name
#         self.type = type
#         self.capacity = capacity
#         self.items = defaultdict(lambda: 0)
#
#     @classmethod
#     def small_shop(cls, name, type):
#         return cls(name, type, 10)
#
#     def add_item(self, item_name):
#         if self.capacity > 0:
#             if item_name not in self.items:
#                 self.items[item_name] += 1
#             return f"{item_name} added to the shop"
#         return "Not enough capacity in the shop"
#
#     def remove_item(self, item_name, amount):
#         if item_name in self.items:
#             self.items[item_name] -= amount
#             self.capacity -= amount
#             return f"{amount} {item_name} removed from the shop"
#         return f"Cannot remove {amount} {item_name}"
#
#     def __repr__(self):
#         return f"{self.name} of type {self.type} with capacity {self.capacity}"
#
#
# fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
# small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
# print(fresh_shop)
# print(small_shop)
#
# print(fresh_shop.add_item("Bananas"))
# print(fresh_shop.remove_item("Tomatoes", 2))
#
# print(small_shop.add_item("Jeans"))
# print(small_shop.add_item("Jeans"))
# print(small_shop.remove_item("Jeans", 2))


class Shop:
    def __init__(self, name: str, shop_type: str, capacity: int):
        self.name = name
        self.type = shop_type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name: str, shop_type: str):
        return cls(name, shop_type, 10)

    def add_item(self, item_name: str):
        total_amount = 0
        for item_amount in self.items.values():
            total_amount += item_amount
        if total_amount >= self.capacity:
            return "Not enough capacity in the shop"
        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name:str, amount:int):
        if item_name not in self.items or self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"
        self.items[item_name] -= amount
        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))