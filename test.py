from Animals import Carnivorous
from Animals import Omnivorous
from Animals import Herbivorous

a1 = Carnivorous.random()
a2 = Carnivorous.random()


b1 = Omnivorous.random()
b2 = Omnivorous.random()

c1 = Herbivorous.random()
c2 = Herbivorous.random()
# print(a1)
# print(a2)
#
# print(a1 > a2)
# print(a1 < a2)
animals = [a1, a2]
animals1 = [b1, b2]
animals2 = [c1, c2]
# animals.extend(animals1, animals2)
animals3 = [*animals, *animals1, *animals2]
# print(str(sorted(animals1, reverse=True)))
# print(str(sorted(animals, reverse=True)))
# print(str(sorted(animals2, reverse=True)))

for i in sorted(animals3, reverse=True):
    print(i)


