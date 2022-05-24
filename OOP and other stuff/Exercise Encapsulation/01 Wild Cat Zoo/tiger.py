from project.animal import Animal


class Tiger(Animal):
    TIGER_MONEY_FOR_CARE = 45

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.money_for_care = Tiger.TIGER_MONEY_FOR_CARE

