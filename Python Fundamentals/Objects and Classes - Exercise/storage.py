class Storage:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_products = list()

    def add_product(self, product: str):

        if len(self.current_products) < self.capacity:
            self.current_products.append(product)

    def get_products(self):

        return self.current_products

storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())
