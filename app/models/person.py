# app/models/person.py
from app.models.statistics import Statistics

class Person:
    def __init__(self, id):
        self._id = id
        self._first_name = ""
        self._middle_name = ""
        self._last_name = ""
        self._second_last_name = ""
        self._sex = ""
        self._age = 0
        self._location = ""
        self._plausible_death = ""
        self.statistics = Statistics()

    @property
    def id(self):
        return self._id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value):
        self._middle_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def second_last_name(self):
        return self._second_last_name

    @second_last_name.setter
    def second_last_name(self, value):
        self._second_last_name = value

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def plausible_death(self):
        return self._plausible_death

    @location.setter
    def plausible_death(self, value):
        self._plausible_death = value

    def get_json(self):
        return self.__dict__

    def __repr__(self):
        attributes = ', '.join(f'{key}={value}' for key, value in self.__dict__.items())
        return f'Person({attributes})'
