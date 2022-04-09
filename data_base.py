import json
from os import path


class Base:
    def __init__(self):
        self.content = {}

    def connect(self):
        if path.exists('Data_Base.json'):
            with open('Data_Base.json', 'r') as db_file:
                self.content = json.load(db_file)
        else:
            with open("Data_Base.json", "w") as db_file:
                json.dump({}, db_file)

    def init_table(self, name):
        if self.content.get(name) is None:
            self.content[name] = []

    def create(self, table_name, cls, data):
        all_data = cls
        all_data.update(data)
        print(all_data)
        self.content[table_name].append(all_data)

    def save(self):
        with open("Data_Base.json", "w") as db_file:
            json.dump(self.content, db_file)

    def remove(self):
        # with open('Data_Base.json', 'r') as db_file:
        #  self.content = json.read(db_file)
        #
        #  if db_file in db_file:
        #      db_file.id == id
        pass


User = {
    "name": "",
    "password": ''
}

Token = {
    "id": "2",
}


db = Base()
db.connect()
db.init_table('users')
db.init_table('tokens')
db.create('users', User, {
    "name": "Ivan",
    "password": "123"
})
db.create('users', User, {
    "name": "Ivan1",
    "password": "1232"
})

db.create('tokens', Token, {
    "id": "10"
})

db.save()