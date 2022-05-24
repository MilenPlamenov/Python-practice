from project.animal import Animal


class Cheetah(Animal):
    CHEETAH_MONEY_FOR_CARE = 60

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.money_for_care = Cheetah.CHEETAH_MONEY_FOR_CARE

