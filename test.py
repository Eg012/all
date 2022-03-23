from Animals import Carnivorous


a1 = Carnivorous.random()
a2 = Carnivorous.random()

# print(a1)
# print(a2)
#
# print(a1 > a2)
# print(a1 < a2)
animals = [a1, a2, Carnivorous.random(), Carnivorous.random()]
print(str(sorted(a1, a2, lambda a1, a2: a2 > a1)))





