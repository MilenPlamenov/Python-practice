class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > 0:
            self.animals.append(animal)
            self.__budget -= price
            self.__animal_capacity -= 1
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > 0:
            self.__workers_capacity -= 1
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        worker = [w for w in self.workers if w.name == worker_name]

        if worker:
            self.workers.remove(worker[0])
            self.__workers_capacity += 1
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total = sum([s.salary for s in self.workers])
        if self.__budget >= total:
            self.__budget -= total
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total = sum([t.money_for_care for t in self.animals])
        if self.__budget >= total:
            self.__budget -= total
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [l for l in self.animals if l.__class__.__name__ == "Lion"]
        tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]
        cheetahs = [ch for ch in self.animals if ch.__class__.__name__ == "Cheetah"]
        result = ""
        result += f"You have {len(self.animals)} animals\n----- {len(lions)} Lions:\n"
        result += '\n'.join([l.__repr__() for l in lions]) + '\n'
        result += f"----- {len(tigers)} Tigers:\n"
        result += '\n'.join([t.__repr__() for t in tigers]) + '\n'
        result += f"----- {len(tigers)} Cheetahs:\n"
        result += '\n'.join([ch.__repr__() for ch in cheetahs])
        return result

    def workers_status(self):
        keepers = [keep for keep in self.workers if keep.__class__.__name__ == "Keeper"]
        caretakers = [care for care in self.workers if care.__class__.__name__ == "Caretaker"]
        vets = [vet for vet in self.workers if vet.__class__.__name__ == "Vet"]
        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        result += '\n'.join([k.__repr__() for k in keepers]) + '\n'
        result += f"----- {len(caretakers)} Caretakers:\n"
        result += '\n'.join([c.__repr__() for c in caretakers]) + '\n'
        result += f"----- {len(vets)} Vets:\n"
        result += '\n'.join([v.__repr__() for v in vets])
        return result
