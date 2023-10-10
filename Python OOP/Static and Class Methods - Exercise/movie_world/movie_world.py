from movie_world.customer import Customer
from movie_world.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) == self.customer_capacity():
            return
        self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) == self.dvd_capacity():
            return
        self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        current_customer = self.__find_id(self.customers, customer_id)
        current_dvd = self.__find_id(self.dvds, dvd_id)

        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"
        elif current_dvd.is_rented:
            return "DVD is already rented"
        elif not current_dvd.is_allowed_to_watch(current_customer.age):
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"

        current_dvd.is_rented = True
        current_customer.rented_dvds.append(current_dvd)
        return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        current_customer = self.__find_id(self.customers, customer_id)
        current_dvd = self.__find_id(self.dvds, dvd_id)

        if current_dvd not in current_customer.rented_dvds:
            return f"{current_customer.name} does not have that DVD"

        current_customer.rented_dvds.remove(current_dvd)
        current_dvd.is_rented = False
        return f"{current_customer.name} has successfully returned {current_dvd.name}"

    def __repr__(self):
        result = '\n'.join([repr(customer) for customer in self.customers]) + '\n'
        result += '\n'.join([repr(dvd) for dvd in self.dvds]) + '\n'

        return result.strip()

    def __find_id(self, object_list, needed_id):
        for current_object in object_list:
            if current_object.id == needed_id:
                return current_object
