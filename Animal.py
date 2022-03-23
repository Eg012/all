import random


class Animal:
    def __init__(self, animal_weight, eat_norma):
        self.animal_weight = animal_weight
        self.eat_norma = eat_norma

    def __int__(self):
        return int(self.animal_weight * self.eat_norma)

    @staticmethod
    def random(class_name, random_pool):
        return class_name(**random.choice(random_pool))


class Carnivorous(Animal):  # Сarnivorous
    def __init__(self, animal_weight, eat_norma, nickname, food_type=None):
        super().__init__(animal_weight, eat_norma)
        self.food_type = "meat" if food_type is None else food_type
        self.name = ['гепард', 'медведь', 'морж']
        self.nickname = nickname

    def __str__(self):
        return f'класс животного:{self.__class__.__name__}, имя животного:{random.choice(self.name)}, кличка:{self.nickname}, тип еды:{self.food_type}, количество еды:{self.eat_norma}'


    @staticmethod
    def random():
        pool = [
            {
                "animal_weight": random.randint(60, 120),
                "eat_norma": 1.5,
                "name": "гепард",
                "nickname": "Александр"
            },
            {
                "animal_weight": random.randint(100, 400),
                "eat_norma": 5.6,
                "name": "медведь",
                "nickname": "Миша"
            },
            {
                "animal_weight": random.randint(150, 400),
                "eat_norma": 7.0,
                "name": "морж",
                "nickname": "Анатолий"
            }
        ]
        return Animal.random(Carnivorous, pool)

    def __gt__(self, other):
        return self.eat_norma > other.eat_norma


class Omnivorous(Animal):
    def __init__(self, animal_weight, eat_norma, nickname, name, food_type=None):
        super().__init__(animal_weight, eat_norma)
        self.food_type = "food" if food_type is None else food_type
        # self.name = ['барсук', 'утка', 'кабан'] random.choice(self.name)
        self.eat_norma = eat_norma
        self.nickname = nickname
        self.name = name

    def __str__(self):
        return f'класс животного:{self.__class__.__name__}, имя животного:{self.name}, кличка:{self.nickname}, тип еды:{self.food_type}, количество еды:{self.eat_norma}'

    @staticmethod
    def random():
        pool = [
            {
                "animal_weight": random.randint(4, 15),
                "eat_norma": 1.5,
                "name": "барсук",
                "nickname": "Олег"
            },
            {
                "animal_weight": random.randint(3, 8),
                "eat_norma": 1.0,
                "name": "утка",
                "nickname": "Настя"
            },
            {
                "animal_weight": random.randint(50, 150),
                "eat_norma": 7.0,
                "name": "кабан",
                "nickname": "Петя"
            }
        ]
        return Animal.random(Omnivorous, pool)

    def __gt__(self, other):
        return self.eat_norma > other.eat_norma


class Herbivorous(Animal):
    def __init__(self, animal_weight, eat_norma, nickname, name, food_type=None):
        super().__init__(animal_weight, eat_norma)
        self.food_type = "grass" if food_type is None else food_type
        self.eat_norma = eat_norma
        # self.name = ['Жираф', 'пандa', 'зебра'] random.choice(self.name)
        self.nickname = nickname
        self.name = name

    def __str__(self):
        return f'класс животного:{self.__class__.__name__}, имя животного:{self.name}, кличка:{self.nickname}, тип еды:{self.food_type}, количество еды:{self.eat_norma}'

    @staticmethod
    def random():
        pool = [
            {
                "animal_weight": random.randint(10, 100),
                "eat_norma": 2.0,
                "name": "жираф",
                "nickname": "Вася"
            },
            {
                "animal_weight": random.randint(100, 220),
                "eat_norma": 5.6,
                "name": "панда",
                "nickname": "Гена"
            },
            {
                "animal_weight": random.randint(50, 150),
                "eat_norma": 7.0,
                "name": "зебра",
                "nickname": "Лёня"
            }
        ]
        return Animal.random(Herbivorous, pool)

    def __gt__(self, other):
        return self.eat_norma > other.eat_norma


print(int(Carnivorous.random()))
print(int(Herbivorous.random()))
print(int(Omnivorous.random()))
#alfavit = []
# animal_carnivorous = ['гепард', 'медведь', 'морж']
#         animal_herbivorous = ['Жираф', 'пандa , 'зебра']
#         animal_omnivorous = ['барсук', 'утка', 'кабан']
#         animal_type = ['carnivorous', 'omnivorous', 'herbivorous']
#         animal_weight = [random.randint(1,100)]
