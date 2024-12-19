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
    
    def get_player_by_id(self, player_id):
        data = self.repository.get_player_by_id(player_id)

        if data:
            data = self._convert_to_player(data)

        return data
    
    def _convert_to_player(self, row):
        player = Player(row['id'])
        player.first_name=row['first_name']
        player.middle_name = row['middle_name']
        player.last_name = row['last_name']
        player.second_last_name = row['second_last_name']
        player.sex = row['sex']
        player.age = row['age']
        player.location = row['location']
        player.plausible_death = row['plausible_death']
        player.father = row['father']
        player.mother = row['mother']

        player.statistics.time = row['statistics']['time']
        player.statistics.energy = row['statistics']['energy']
        player.statistics.hunger = row['statistics']['hunger']
        player.statistics.intelligence = row['statistics']['intelligence']
        player.statistics.strength = row['statistics']['strength']
        player.statistics.mental_health = row['statistics']['mental_health']
        player.statistics.physical_health = row['statistics']['physical_health']
        player.statistics.social_skills = row['statistics']['social_skills']
        player.statistics.job_performance = row['statistics']['job_performance']

        return player
