# app/use_cases/create_player.py
from app.services.person_service import PersonService
from app.services.player_service import PlayerService
from app.helpers.person_to_player_mapper import map_person_to_player
from app.helpers.rnd_person_genrator import rnd_person_genrator
import random 

class CreatePlayer:
    def __init__(self, person_service: PersonService, player_service: PlayerService):
        self.person_service = person_service
        self.player_service = player_service

    def execute(self, lang):
        # the woman in world hav 15% of posibilities to BE single mother
        _isSingleMother = True if random.randint(0, 100) <= 15 else False

        if not _isSingleMother:
            _newPId = self.person_service.generate_new_id()
            father = rnd_person_genrator(_newPId, sex="MALE", isParent=True)
            self.person_service.register_person(father)

        _newPId = self.person_service.generate_new_id()
        mother = rnd_person_genrator(_newPId, sex="FEMALE", isParent=True)
        self.person_service.register_person(mother)

        _newPId = self.person_service.generate_new_id()
        player = map_person_to_player(rnd_person_genrator(_newPId, age=0))
        
        player._father = father.id if not _isSingleMother else None
        player._mother =  mother.id

        # register player
        self.player_service.add(player)
        # Register likea a person and return
        return self.person_service.register_person(player)
