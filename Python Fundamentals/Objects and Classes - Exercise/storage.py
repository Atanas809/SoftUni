# Задача 1:

class Storage:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = list()

    def add_product(self, product: str):

        if len(self.storage) < self.capacity:
            self.storage.append(product)

    def get_products(self):

        return self.storage

storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())
