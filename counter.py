class Counter:
    def __init__(self, counter=0):
        self.__counter = counter

    def plus(self):
        self.__counter += 1

    def minus(self):
        self.__counter -= 1

    def __str__(self):
        return f'{self.__counter}'


c = Counter()
c1 = Counter(10)

c1.plus()
c1.plus()
c1.minus()

print(c1._Counter__counter)
