class Book:
    def __init__(self, number, name, year, author):
        self.number = number
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f'название книги:{self.name},год издания:{self.year}, номер книги: {self.number},'

    @staticmethod
    def random():
        books = ['Meтро 2033', 'Голос', 'Рыцари сорока островов']
        author = ['Д.М.Глуховский', 'Д.Д.Сергеевна', 'С.В.Лукьяненко']
        number = [1, 2, 3]
        publishing = ['2005', '28 ноября 2016 г.']
        return Book(name=books,
                    author=author,
                    number=number,
                    year=publishing)


books = []
for i in range(3):
    books.append(Book.random())

for i in sorted(books):
    print(i)


class Home_library:
    def __init__(self, books):
        self.books = books

    def add(self, book):
        pass

    def remove(self, number):
        pass

    # {"year": 2008, }
    def get(self, filters):
        pass


h = Home_library([])

h.get({
    "year": 2008,
    "author": 'Д.М.Глуховский',
    'name': 'Meтро 2033'
})
