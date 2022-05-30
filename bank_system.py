class Bank:
    def __init__(self, name: str, age: int, address: str, balance_user: int):
        self.balance_bank = 100000000
        self.users = ["Егор", "Алексей", "Павел", "Дмитрий", "Илья"]
        self.name = name
        self.age = age
        self.address = address
        self.balance_user = balance_user

    def add_user(self, name, age, address, balance_user):
        self.users.append(
            Bank(name, age, address, balance_user)
        )

    def remove_user(self, users, name):
        for user in users:
            if user.name == name:
                self.users.remove(user)

    def find_mosgennik(self, users):
        #  _flag = True
        # if users.send() > 4:
        #    _flagd = False
        #    return _flag
        pass


class User:
    def __init__(self):
        self.balance = ["10.000", "120.000", "500.000", "120.000"]
        self.operations = [Operation]
        self.users = ["Егор", "Алексей", "Павел", "Дмитрий", "Илья"]


class Operation:
    def __init__(self, count, froms, to):
        self.froms = User
        self.to = User
        self.count = count

    def send(self, froms, to, count):
        f = []
        # operations = [*self.froms, *self.to, *self.count]
        command = Operation(froms, to, count)
        f.operations.append(command)


g = Bank([
    Bank(name="Андрей", age=18, address="Улица Пушкина Дом Колотушкина", balance_user=1800)
])
