class GsmMobileDevice:
    def __init__(self, quantity, price_per_one, year_of_manufacture, manufacturer, model):
        self.gsms = []
        self.quantity = quantity
        self.price_per_one = price_per_one
        self.year_of_manufacture = year_of_manufacture
        self.manufacturer = manufacturer
        self.model = model

    def add_gsm(self, gsm):
        if gsm not in self.gsms:
            self.gsms.append(gsm)

    def sort_models_by_quantity(self):
        return sorted(self.gsms, key=self.quantity)
