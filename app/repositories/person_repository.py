# app/repositories/person_repository.py
class PersonRepository:
    def __init__(self):
        self.persons = []  # Simulates DB

    def get_next_id(self):
        if not self.persons:
            return 1
        else:
            return max(person.id for person in self.persons)
    
    def add(self, person):
        self.persons.append(person)
    
    def get_all(self):
        return self.persons
