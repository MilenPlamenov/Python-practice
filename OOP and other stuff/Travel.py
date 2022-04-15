class Travel:
    def __init__(self, travel_id, destination, flight, price):
        self.travel_id = travel_id
        self.destination = destination
        self.flight = flight
        self.price = price

    def reduce(self):
        if self.price > 200:
            self.price -= self.price * 0.1

    def print(self):
        print(f"ID: {self.travel_id}, Destination: {self.destination}, Flight: {self.flight}, Price: {self.price}")


travel_num_one = Travel(1, "Hawaii", "early", 1000)  # making the object
print(travel_num_one.price)
travel_num_one.reduce()
print(travel_num_one.price)
travel_num_one.print()