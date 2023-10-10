from structure_and_functionality_4.client import Client
from structure_and_functionality_4.meals.meal import Meal


class FoodOrdersApp:
    VALID_MEALS = ["Starter", "MainDish", "Dessert"]
    CURRENT_ID = 1

    def __init__(self):
        self.menu = []
        self.clients_list = []

    @property
    def is_ready(self):
        return len(self.menu) >= 5

    def get_next_id(self):
        current_id = self.CURRENT_ID
        self.CURRENT_ID += 1
        return current_id

    def register_client(self, client_phone_number: str):
        existing_client = self.__find_client_by_number(client_phone_number)

        if existing_client:
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)

        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.type() in self.VALID_MEALS:
                self.menu.append(meal)

    def show_menu(self):
        if not self.is_ready:
            raise Exception("The menu is not ready!")

        result = []

        for meal in self.menu:
            result.append(meal.details())

        return '\n'.join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if not self.is_ready:
            raise Exception("The menu is not ready!")

        existing_client = self.__find_client_by_number(client_phone_number)

        if not existing_client:
            # TODO: could be registered without this method
            self.register_client(client_phone_number)

        meals_to_be_added = {}

        for meal_name, quantity in meal_names_and_quantities.items():
            existing_meal = self.__find_meal(meal_name)
            if not existing_meal:
                raise Exception(f"{meal_name} is not on the menu!")
            if existing_meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {existing_meal.type()}: {meal_name}!")
            meals_to_be_added[existing_meal] = quantity

        for meal, meal_quantity in meals_to_be_added.items():
            existing_client.bill += meal.price * meal_quantity
            existing_client.shopping_cart.append((meal, meal_quantity))
            for meal_in_menu in self.menu:
                if meal_in_menu.name == meal.name:
                    meal_in_menu.quantity -= meal_quantity

        meal_names = [x[0].name for x in existing_client.shopping_cart]
        return f"Client {client_phone_number} successfully ordered " \
               f"{', '.join(meal_names)} for {existing_client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        existing_client = self.__find_client_by_number(client_phone_number)

        if not existing_client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal in existing_client.shopping_cart:
            self.__returning_quantity_to_meal(meal)

        existing_client.shopping_cart.clear()
        existing_client.bill = 0.0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        existing_client = self.__find_client_by_number(client_phone_number)

        if not existing_client.shopping_cart:
            raise Exception("There are no ordered meals!")

        receipt_id = self.get_next_id()
        existing_client.shopping_cart.clear()
        total_paid_money = existing_client.bill
        existing_client.bill = 0.0
        return f"Receipt #{receipt_id} with total amount of " \
               f"{total_paid_money:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    def __find_client_by_number(self, client_phone_number) -> Client:
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                return client

    def __find_meal(self, meal_name) -> Meal:
        for meal in self.menu:
            if meal.name == meal_name:
                return meal

    def __returning_quantity_to_meal(self, meal):
        meal_name, quantity = meal[0], meal[1]
        for current_meal in self.menu:
            if meal_name == current_meal.name:
                current_meal.quantity += quantity
