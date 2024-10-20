# app/use_cases/create_player.py
from app.services.player_service import PlayerService

class CreatePlayer:
    def __init__(self, player_service: PlayerService):
        self.player_service = player_service
    
    def execute(self):
        return self.player_service.register_player()
