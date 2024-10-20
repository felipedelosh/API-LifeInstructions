# app/repositories/player_repository.py
class PlayerRepository:
    def __init__(self):
        self.players = []  # Simulates DB
    
    def add(self, player):
        self.players.append(player)
    
    def get_all(self):
        return self.players
