import random


class Animal:
    def __init__(self, animal_weight):
        self.animal_weight = animal_weight

    def __int__(self):
        return random.randint(self.animal_weight) * 0.1  # animal_weight * 0.1


class Сarnivorous(Animal):  # плотоядный
    def __init__(self, animal_weight, food_count):
        super().__init__(animal_weight)
        self.food__count = food_count
        self.food__type = "meat"


class Omnivores(Animal):  # всеядный
    def __init__(self, animal_weight):
        super().__init__(self, animal_weight)
        self.food__type = "grass"


class Predator(Animal):  # хищник
    def __init__(self, animal_weight):
        super().__init__(self, animal_weight)
        self.food_type = "meat"

    # def __int__(self):

    @staticmethod
    def start():
        animal_example = ['тигр', 'панда', 'шимпанзе ']
        food_type = ['meat', 'grass', 'all']
