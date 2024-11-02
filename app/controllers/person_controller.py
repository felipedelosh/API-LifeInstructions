# app/controllers/person_controller.py
from app.use_cases.get_all_persons import GetAllPersons
from app.services.person_service import PersonService
from app.repositories.person.sqlite_person_repository import SQLitePersonRepository
from app.helpers.response import create_response


# Inyections
repository = SQLitePersonRepository('DB/lifeInstructions.db')
service = PersonService(repository)
use_case = GetAllPersons(service)


def get_all_persons():
    try:
        persons = use_case.execute()
        return create_response(True, [person.get_json() for person in persons], 200)
    except:
        return create_response(False, "", 500)
