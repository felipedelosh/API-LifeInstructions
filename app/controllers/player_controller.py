# app/controllers/player_controller.py
# from flask import request
from app.use_cases.create_player import CreatePlayer
from app.services.person_service import PersonService
from app.repositories.person_repository import PersonRepository
from app.repositories.person.sqlite_person_repository import SQLitePersonRepository
from app.helpers.response import create_response

# Inyections
repository = SQLitePersonRepository('DB/lifeInstructions.db')
service = PersonService(repository)
use_case = CreatePlayer(service)

def register_player():
    try:
        # data = request.get_json()
        try:
            player = use_case.execute("ES")
        except:
            print("Hay un error")
        
        return create_response(True, player.get_json(), 200)
    except:
        return create_response(False, "", 500)
