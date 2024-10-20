# app/controllers/player_controller.py
# from flask import request
from app.use_cases.create_player import CreatePlayer
from app.services.player_service import PlayerService
from app.repositories.player_repository import PlayerRepository
from app.helpers.response import create_response

# Inyections
repository = PlayerRepository()
service = PlayerService(repository)
use_case = CreatePlayer(service)

def register_player():
    try:
        # data = request.get_json()
        player = use_case.execute()
        return create_response(True, player.get_json(), 200)
    except:
        return create_response(False, "", 500)
