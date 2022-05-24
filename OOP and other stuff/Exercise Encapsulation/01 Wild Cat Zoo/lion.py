from project.animal import Animal


class Lion(Animal):
    LION_MONEY_FOR_CARE = 50

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.money_for_care = Lion.LION_MONEY_FOR_CARE
