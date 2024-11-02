# app/use_cases/create_player.py
from app.services.person_service import PersonService
from app.helpers.person_to_player_mapper import map_person_to_player
from app.helpers.rnd_person_genrator import rnd_person_genrator
import random 

class CreatePlayer:
    def __init__(self, person_service: PersonService):
        self.person_service = person_service

    def execute(self, lang):
        # the woman in world hav 15% of posibilities to BE single mother
        _isSingleMother = True if random.randint(0, 100) <= 15 else False
        if not _isSingleMother:
            print("Hay padre")
            _newPId = self.person_service.generate_new_id()
            print("ID del padre")
            father = rnd_person_genrator(_newPId, sex="MALE", isParent=True).id
        _newPId = self.person_service.generate_new_id()
        mother = rnd_person_genrator(_newPId, sex="FEMALE", isParent=True).id


        _newPId = self.person_service.generate_new_id()
        player = map_person_to_player(rnd_person_genrator(_newPId, age=0))
        player._father = father if not _isSingleMother else None
        player._mother = mother

        return self.person_service.register_person(player)
