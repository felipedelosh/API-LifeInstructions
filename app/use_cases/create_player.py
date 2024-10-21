# app/use_cases/create_player.py
from app.services.person_service import PersonService
from app.helpers.person_to_player_mapper import map_person_to_player
from app.helpers.rnd_person_genrator import rnd_person_genrator

class CreatePlayer:
    def __init__(self, person_service: PersonService):
        self.person_service = person_service

    def execute(self, lang):
        _newPId = self.person_service.generate_new_id()
        father = rnd_person_genrator(_newPId, sex="MALE", isParent=True).id
        _newPId = self.person_service.generate_new_id()
        mother = rnd_person_genrator(_newPId, sex="FEMALE", isParent=True).id

        _newPId = self.person_service.generate_new_id()
        player = map_person_to_player(rnd_person_genrator(_newPId, age=0))
        player.father = father
        player.mother = mother

        return self.person_service.register_person(player)
