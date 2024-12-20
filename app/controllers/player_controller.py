# app/controllers/player_controller.py
from flask import request
from app.use_cases.create_player import CreatePlayer
from app.use_cases.get_player import GetPlayer
from app.services.person_service import PersonService
from app.services.player_service import PlayerService
from app.repositories.person_repository import PersonRepository # Search if use  >> Need delete
from app.repositories.person.sqlite_person_repository import SQLitePersonRepository
from app.repositories.player.sqlite_player_repository import SQLitePlayerRepository
from app.helpers.response import create_response

# Inyections
person_repository = SQLitePersonRepository('DB/lifeInstructions.db')
player_repository = SQLitePlayerRepository('DB/lifeInstructions.db')
person_service = PersonService(person_repository)
player_service = PlayerService(player_repository)
use_case_create_player = CreatePlayer(person_service, player_repository)
use_case_get_player = GetPlayer(player_service)

def register_player():
    try:
        user_preferencies = request.get_json()
        player = use_case_create_player.execute("ES", user_preferencies)
        return create_response(True, player.get_json(), 200)
    except:
        return create_response(False, "", 500)
    
def get_player(player_id):
    try:
        player = use_case_get_player.execute(player_id)
        return create_response(True, player.get_json(), 200)
    except Exception as e:
        # Log the exception for debugging purposes
        # print(f"Error: {e}")
        return create_response(False, "", 500)
