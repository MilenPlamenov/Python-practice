class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        self.customers.append(customer) if customer not in self.customers else None

    def add_trainer(self, trainer):
        self.trainers.append(trainer) if trainer not in self.trainers else None

    def add_equipment(self, equipment):
        self.equipment.append(equipment) if equipment not in self.equipment else None

    def add_plan(self, plan):
        self.plans.append(plan) if plan not in self.plans else None

    def add_subscription(self, subscription):
        self.subscriptions.append(subscription) if subscription not in self.subscriptions else None

    def subscription_info(self, subscription_id):
        subscription = [s for s in self.subscriptions if s.id == subscription_id][0]
        customer = [c for c in self.customers if c.id == subscription.customer_id][0]
        trainer = [t for t in self.trainers if t.id == subscription.trainer_id][0]
        plan = [p for p in self.plans if p.id == subscription.exercise_id][0]
        equipment = [e for e in self.equipment if e.id == plan.equipment_id][0]
        info = [subscription, customer, trainer, equipment, plan]
        return ''.join([f"{x.__repr__()}\n" for x in info])




