# app/use_cases/get_player.py
from app.services.player_service import PlayerService

class GetPlayer:
    def __init__(self, player_service: PlayerService):
        self.player_service = player_service

    def execute(self, player_id):
        return self.player_service.get_player_by_id(player_id)
