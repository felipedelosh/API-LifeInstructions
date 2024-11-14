# app/services/player_service.py
from app.repositories.player.iplayer_repository import IPlayerRepository
from app.models.player import Player

class PlayerService:
    def __init__(self, repository: IPlayerRepository):
        self.repository = repository

    def add(self, person):
        self.repository.add(person)
        return person

    def get_all(self):
        data =  self.repository.get_all()

        return []
    

    def _convert_to_player(self, row):
        person = Player(row[0])

        return person
