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

    def init_table(self, schema):
        if self.content.get(schema.get('_table')) is None:
            self.content[schema.get('_table')] = []

    def create(self, schema, data):
        table_name = schema.get('_table')
        cls = dict(schema)
        del cls['_table']
        cls.update(data)
        print(cls)
        self.content[table_name].append(cls)

    def save(self):
        with open("Data_Base.json", "w") as db_file:
            json.dump(self.content, db_file)

    def get(self, schema, filters=None):
        table_name = schema.get('_table')
        with open("Data_Base.json", "w") as db_file:
            json.dump(self.content, db_file)
        # self.content[table]
        if filters is None:
            return self.content[table_name]

        contents = []
        for item in self.content[table_name]:
            for key in filters.keys():
                if type(filters[key]) == list and item[key] in filters[key]:
                    contents.append(item)
                elif item[key] == filters[key]:
                    contents.append(item)

        return contents

    def remove(self, schema, filters):
        table_name = schema.get('_table')
        with open('Data_Base.json', 'w') as db_file:
            json.dump(self.content, db_file)

        for item in self.content[table_name]:
            for key in filters.keys():
                if type(filters[key]) == list and item[key] in filters[key]:
                    self.content[table_name].remove(item)
                elif item[key] == filters[key]:
                    self.content[table_name].remove(item)

User = {
    "_table": "users",
    "name": "",
    "password": ''
}

Token = {
    "_table": "tokens",
    "id": "2",
}

db = Base()
db.connect()
db.init_table(User)
db.init_table(Token)
db.create(User, {
    "name": "Ivan",
    "password": "123"
})
db.create(User, {
    "name": "Ivan1",
    "password": "1232"
})

db.create(Token, {
    "id": "10"
})

db.save()
db.remove(User, {
                "name": "Ivan1",
})
db.save()