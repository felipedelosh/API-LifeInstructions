# app/controllers/get_random_person_controller.py
from app.helpers.response import create_response
from app.use_cases.generate_random_person import GenerateRandomPerson

# Inyections
use_case = GenerateRandomPerson()

def get_random_person():
    try:
        rnd_person = use_case.execute()
        return create_response(True, rnd_person, 200)
    except:
        return create_response(False, "", 500)