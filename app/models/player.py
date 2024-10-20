# app/models/player.py
class Player:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        self.location = ""

    def get_json(self):
        return self.__dict__

    def __repr__(self):
        attributes = ', '.join(f'{key}={value}' for key, value in self.__dict__.items())
        return f'Player({attributes})'
