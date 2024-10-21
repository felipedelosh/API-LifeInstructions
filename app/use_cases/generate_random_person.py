# app/use_cases/generate_random_person.py
from app.helpers.rnd_person_genrator import rnd_person_genrator

class GenerateRandomPerson:
    def execute(self):
        rndP = rnd_person_genrator()
        return rndP
