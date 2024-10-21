# app/controllers/get_random_person_controller.py
from app.helpers.response import create_response
from app.use_cases.generate_random_person import GenerateRandomPerson
from app.services.person_service import PersonService
from app.repositories.person_repository import PersonRepository

# Inyections
repository = PersonRepository()
service = PersonService(repository)
use_case = GenerateRandomPerson(service)

def get_random_person():
    try:
        rnd_person = use_case.execute()
        return create_response(True, rnd_person.get_json(), 200)
    except:
        return create_response(False, "", 500)