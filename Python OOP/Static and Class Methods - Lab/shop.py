class Shop:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = dict()

    @classmethod
    def small_shop(cls, name, type):
        default_capacity = 10
        return cls(name, type, default_capacity)

    def add_item(self, item_name):
        total_items_quantity = sum(self.items.values())
        if self.capacity == total_items_quantity:
            return "Not enough capacity in the shop"

        if item_name not in self.items.keys():
            self.items[item_name] = 0
        self.items[item_name] += 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name, amount):
        if item_name in self.items.keys() and amount <= self.items[item_name]:
            self.items[item_name] -= amount
            if self.items[item_name] == 0:
                del self.items[item_name]
            return f"{amount} {item_name} removed from the shop"

        return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)