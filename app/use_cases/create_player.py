# app/use_cases/create_player.py
from app.models.person import Person
from app.services.person_service import PersonService
from app.services.player_service import PlayerService
from app.helpers.person_to_player_mapper import map_person_to_player
from app.helpers.rnd_person_genrator import rnd_person_genrator
import random 

class CreatePlayer:
    def __init__(self, person_service: PersonService, player_service: PlayerService):
        self.person_service = person_service
        self.player_service = player_service

    def execute(self, lang, user_preferencies=None):
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
        if user_preferencies:
            player = self._fillPersonData(_newPId, user_preferencies)
        else:
            player = rnd_person_genrator(_newPId, age=0)

        player = map_person_to_player(player)
        player._father = father.id if not _isSingleMother else None
        player._mother =  mother.id
        # register player
        self.player_service.add(player)
        # Register like a person and return
        return self.person_service.register_person(player)
    
    def _fillPersonData(self, id, user_preferencies):
        player = Person(id)
        _player = player.__dict__
        for key, value in user_preferencies.items():
            try:
                _key = f"_{key}"
                setattr(player, _key, value)
            except:
                # print(f"Err set Player Atr: {_key}:{value}")
                pass


        return player


