# app/use_cases/generate_random_person.py
from app.helpers.rnd_person_genrator import RandomPersonGenerator

class GenerateRandomPerson:
    def __init__(self):
        pass

    def execute(self):
        rndP = RandomPersonGenerator()
        return rndP
