from fitness_gym.customer import Customer
from fitness_gym.equipment import Equipment
from fitness_gym.exercise_plan import ExercisePlan
from fitness_gym.subscription import Subscription
from fitness_gym.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription_plan = self.__find_id(self.subscriptions, subscription_id)
        customer = self.__find_id(self.customers, subscription_plan.customer_id)
        trainer = self.__find_id(self.trainers, subscription_plan.trainer_id)
        plan = self.__find_id(self.plans, subscription_plan.exercise_id)
        equipment = self.__find_id(self.equipment, plan.equipment_id)

        result = f"{subscription_plan}\n"
        result += f"{customer}\n"
        result += f"{trainer}\n"
        result += f"{equipment}\n"
        result += f"{plan}\n"

        return result.strip()

    def __find_id(self, object_list, needed_id):
        for current_object in object_list:
            if current_object.id == needed_id:
                return current_object
