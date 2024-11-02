# app/controllers/time_manager_controller.py
from flask import request
from app.services.person_service import PersonService
from app.repositories.person_repository import PersonRepository
from app.use_cases.make_activity import MakeActivity
from app.helpers.response import create_response

use_case = MakeActivity()

def takeOptionActivity():
    try:
        data = request.get_json()
        
        player = data.get("player_id")

        if not player:
            return create_response(False, "'player_id' must be a non-empty or invalid user", 400)

        actions = data.get("actions")
        if not isinstance(actions, str) or len(actions) == 0:
            return create_response(False, "'actions' must be a non-empty string", 400)

        make_actions = use_case.execute(player, actions)
        return create_response(True, make_actions, 200)
    except:
        return create_response(False, "", 500)