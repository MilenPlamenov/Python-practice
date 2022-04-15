
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def total(self):
        print(sum([item.price for item in self.items]))

    def __len__(self):
        print(len(self.items))


item1 = Item("bike", 1000)
item2 = Item("headphones", 100)

sc = ShoppingCart()
sc.total()
sc.add(item1)
sc.len()
sc.total()
sc.add(item2)
sc.add(item2)
sc.len()
sc.total()


# 2 →  n = 2 (number of item types)
# bike 1000  →  name = 'bike' price = 1000
# headphones 100 → name = 'headphones' price = 100
# 8  → q = 8    (number of method calls)
# total  → each line represents a method call on the ShoppingCart
# add bike
# len
# total
# add headphones
# add headphones
# len
# total



