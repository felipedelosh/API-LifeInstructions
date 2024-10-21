# app/models/player.py
from .person import Person

class Player(Person):
    def __init__(self, id):
        super().__init__(id)
        self.father = None
        self.mother = None

    def get_json(self):
        return self.__dict__

    def __repr__(self):
        attributes = ', '.join(f'{key}={value}' for key, value in self.__dict__.items())
        return f'Player({attributes})'
