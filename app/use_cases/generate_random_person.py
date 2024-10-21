# app/use_cases/generate_random_person.py
from app.services.person_service import PersonService
from app.helpers.rnd_person_genrator import rnd_person_genrator

class GenerateRandomPerson:
    def __init__(self, person_service: PersonService):
        self.person_service = person_service

    def execute(self):
        _newPId = self.person_service.generate_new_id()
        rndP = rnd_person_genrator(_newPId)
        return self.person_service.register_person(rndP)
