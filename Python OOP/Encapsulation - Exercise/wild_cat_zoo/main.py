from wild_cat_zoo.animal import Animal
from wild_cat_zoo.caretaker import Caretaker
from wild_cat_zoo.cheetah import Cheetah
from wild_cat_zoo.keeper import Keeper
from wild_cat_zoo.lion import Lion
from wild_cat_zoo.tiger import Tiger
from wild_cat_zoo.vet import Vet
from wild_cat_zoo.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []
