# app/services/player_service.py
from app.models.player import Player
from app.repositories.player_repository import PlayerRepository

class PlayerService:
    def __init__(self, repository: PlayerRepository):
        self.repository = repository

    def register_player(self, name, age):
        new_player = Player(id=len(self.repository.get_all()) + 1, name=name, age=age)
        self.repository.add(new_player)
        return new_player
