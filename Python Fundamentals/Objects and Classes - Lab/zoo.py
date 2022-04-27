# Задача 4:

class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = list()
        self.fishes = list()
        self.birds = list()

    def add_animal(self, species,  type_of_animal):

        if species == "mammal":
            self.mammals.append(type_of_animal)
        elif species == "fish":
            self.fishes.append(type_of_animal)
        elif species == "bird":
            self.birds.append(type_of_animal)

        Zoo.__animals += 1

    def get_info(self, species):

        if species == "mammal":
            return f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            return f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            return f"Birds in {self.zoo_name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"

zoo = Zoo(input())

number = int(input())

for x in range(number):
    info = input().split()

    species = info[0]
    animal = info[1]

    zoo.add_animal(species, animal)

needed_animal = input()

print(zoo.get_info(needed_animal))


