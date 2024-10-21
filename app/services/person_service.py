# app/services/person_service.py
from app.repositories.person_repository import PersonRepository

class PersonService:
    def __init__(self, repository: PersonRepository):
        self.repository = repository

    def generate_new_id(self):
        return self.repository.get_next_id()

    def register_person(self, person):
        self.repository.add(person)
        return person
