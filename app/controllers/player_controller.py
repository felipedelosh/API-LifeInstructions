# app/controllers/player_controller.py
# from flask import request
from app.use_cases.create_player import CreatePlayer
from app.services.person_service import PersonService
from app.repositories.person_repository import PersonRepository
from app.helpers.response import create_response

# Inyections
repository = PersonRepository()
service = PersonService(repository)
use_case = CreatePlayer(service)

def register_player():
    try:
        # data = request.get_json()
        player = use_case.execute("ES")
        print(player.get_json())
        return create_response(True, player.get_json(), 200)
    except:
        return create_response(False, "", 500)
