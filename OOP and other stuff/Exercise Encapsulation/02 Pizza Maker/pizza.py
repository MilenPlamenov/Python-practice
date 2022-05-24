class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}  # topping_type as a key and topping weight as value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if not value:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = value

    def add_topping(self, topping):
        current_type, current_value = topping.topping_type, topping.weight
        if len(self.toppings) >= self.toppings_capacity:
            raise ValueError("Not enough space for another topping")
        if current_type not in self.toppings:
            self.toppings[current_type] = 0
        self.toppings[current_type] += current_value

    def calculate_total_weight(self):
        return self.dough.weight + sum(self.toppings.values())
