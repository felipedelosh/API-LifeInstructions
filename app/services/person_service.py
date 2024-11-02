# app/services/person_service.py
from app.repositories.person.iperson_repository import IPersonRepository

class PersonService:
    def __init__(self, repository: IPersonRepository):
        self.repository = repository

    def generate_new_id(self):
        return self.repository.get_next_id()

    def register_person(self, person):
        self.repository.add(person)
        return person

    def get_all(self):
        return self.repository.get_all()
