# app/use_cases/get_all_persons.py
from app.services.person_service import PersonService
from app.models.person import Person

class GetAllPersons:
    def __init__(self, person_service: PersonService):
        self.person_service = person_service

    def execute(self):
        data = self.person_service.get_all()

        if data:
            _persons = []
            for i in data:
                print(i)


        return data
