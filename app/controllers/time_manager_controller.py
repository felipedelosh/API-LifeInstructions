# app/controllers/time_manager_controller.py
from flask import request
from app.repositories.player.sqlite_player_repository import SQLitePlayerRepository
from app.services.player_service import PlayerService
from app.use_cases.get_player import GetPlayer
from app.use_cases.make_activity import MakeActivity
from app.helpers.response import create_response

# GET PLAYER
player_repository = SQLitePlayerRepository('DB/lifeInstructions.db')
player_service = PlayerService(player_repository)
use_case_get_player = GetPlayer(player_service)
# Make action
use_case_make_activity = MakeActivity(player_service)


def takeOptionActivity():
    try:
        data = request.get_json()
        
        player_id = data.get("player_id")

        if not player_id:
            return create_response(False, "'player_id' must be a non-empty or invalid user", 400)

        actions = data.get("action")
        if not isinstance(actions, str) or len(actions) == 0:
            return create_response(False, "'action' must be a non-empty string", 400)
        
        player = use_case_get_player.execute(player_id)

        player_make_actions = use_case_make_activity.execute(player, actions)

        if isinstance(player_make_actions, str):
            return create_response(False, f"{player_make_actions}", 200)

        return create_response(True, player_make_actions.get_json(), 200)
    except:
        return create_response(False, "", 500)
