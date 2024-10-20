# app/use_cases/create_player.py
from app.services.player_service import PlayerService
import random

class CreatePlayer:
    def __init__(self, player_service: PlayerService):
        self.player_service = player_service

    def rnd_sex():
        _sex = ['MALE', 'FEMALE']
        return _sex[random.randint(0, 1)]
    
    def generate_mother():
        pass

    def generate_fatther():
        pass
    
    def execute(self, lang):
        return self.player_service.register_player()
