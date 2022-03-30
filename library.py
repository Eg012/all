class Book:
    def __init__(self, number, name, year, author):
        self.number = number
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f'название книги:{self.name},год издания:{self.year}, номер книги: {self.number}, автор книги:{self.author}'


class HomeLibrary:
    def __init__(self, books):
        self.books = books

    def remove(self, number):
        for book in self.books:
            if book.number == number:
                self.books.remove(book)

    # {"year": 2008, }
    def get(self, filters=None):
        if filters is None:
            return self.books

        books = []
        for book in self.books:
            for key in filters.keys():
                if type(filters[key]) == list:
                    if book.__dict__[key] in filters[key]:
                        books.append(book)
                        break
                elif book.__dict__[key] == filters[key]:
                    books.append(books)
                    break
        return books

    def push(self, number, name, year, author):
        self.books.append(
            Book(number, name, year, author)
        )


h = HomeLibrary([
    Book(name='Meтро 2033', author='Д.М.Глуховский', year=2005, number=1),
    Book(name='Голос', author='Д.Д.Сергеевна', year=2016, number=2),
    Book(name='С.В.Лукьяненко', author='Рыцари сорока островов', year=2006, number=3)
])
h.remove(3)
a = h.get()

c = h.get({
    "year": [2016],
    "author": 'Д.Д.Сергеевна'
})

b = h.get({
    "year": [2006],
    "author": 'С.В.Лукьяненко'
})


def print_book(books):
    for book in books:
        print(book)

h.push(name='Meтро 2033', author='Д.М.Глуховский', year=2005, number=10)

print_book(a)
print_book(b)
print_book(c)
