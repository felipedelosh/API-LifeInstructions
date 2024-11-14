# app/controllers/player_controller.py
# from flask import request
from app.use_cases.create_player import CreatePlayer
from app.services.person_service import PersonService
from app.services.player_service import PlayerService
from app.repositories.person_repository import PersonRepository # Serach if use to delette
from app.repositories.person.sqlite_person_repository import SQLitePersonRepository
from app.repositories.player.sqlite_player_repository import SQLitePlayerRepository
from app.helpers.response import create_response

# Inyections
person_repository = SQLitePersonRepository('DB/lifeInstructions.db')
player_repository = SQLitePlayerRepository('DB/lifeInstructions.db')
person_service = PersonService(person_repository)
player_servide = PlayerService(player_repository)
use_case = CreatePlayer(person_service, player_repository)

def register_player():
    try:
        player = use_case.execute("ES")
        return create_response(True, player.get_json(), 200)
    except:
        return create_response(False, "", 500)
