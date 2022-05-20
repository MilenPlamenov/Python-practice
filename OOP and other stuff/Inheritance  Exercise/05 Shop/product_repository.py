class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        product = [p for p in self.products if p.name == product_name]

        if product:
            return product[0]

    def remove(self, product_name):
        product = [p for p in self.products if p.name == product_name]

        if product:
            self.products.remove(product[0])

    def __repr__(self):
        data = ''
        data += '\n'.join([f"{p.name}: {p.quantity}" for p in self.products])
        return data
