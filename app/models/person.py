# app/models/person.py
class Person:
    def __init__(self, id):
        self.id = id
        self.firt_name = ""
        self.middle_name = ""
        self.last_name = ""
        self.second_last_name = ""
        self.sex = ""
        self.age = 0
        self.location = ""

    def get_json(self):
        return self.__dict__

    def __repr__(self):
        attributes = ', '.join(f'{key}={value}' for key, value in self.__dict__.items())
        return f'Player({attributes})'
