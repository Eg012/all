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
        books_name = ['Meтро 2033', 'Голос', 'Рыцари сорока островов']
        author = ['Д.М.Глуховский', 'Д.Д.Сергеевна', 'С.В.Лукьяненко']
        number = [1, 2, 3]
        publishing = ['2005', '28 ноября 2016 г.', '2006']
        return Book(name=books_name,
                    author=author,
                    number=number,
                    year=publishing)


books = []
for i in range(3):
    books.append(Book.random())

for book in sorted(books):
    print(book)


class Home_library:
    def __init__(self, books):
        self.books = books

    def add(self, book):
        self.book = book

    @staticmethod
    def random():
        pass

    def remove(self, number):
        self.number = number

    # {"year": 2008, }
    def get(self, filters):
        self.filters = filters
        filters = h

h = Home_library([])

h.get({
    "year": 2008,
    "author": 'Д.М.Глуховский',
}, )

h.get({
    "year": "28 ноября 2016 г",
    "author": 'Д.Д.Сергеевна'
}, )

h.get({
    "year": 2006,
    "author": 'С.В.Лукьяненко'
})
