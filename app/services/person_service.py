# app/services/person_service.py
from app.repositories.person.iperson_repository import IPersonRepository
from app.models.person import Person

class PersonService:
    def __init__(self, repository: IPersonRepository):
        self.repository = repository

    def generate_new_id(self):
        return self.repository.get_next_id()

    def register_person(self, person):
        self.repository.add(person)
        return person

    def get_all(self):
        data =  self.repository.get_all()
        persons = []

        if data:
            persons = [self._convert_to_person(row) for row in data]

        return persons
    

    def _convert_to_person(self, row):
        person = Person(row[0])
        person.first_name = row[1]
        person.middle_name = row[2]
        person.last_name = row[3]
        person.second_last_name = row[4]
        person.sex = row[5]
        person.age = row[6]
        person.location = row[7]
        person.plausible_death = row[8]

        return person
