# app/use_cases/make_activity.py
from app.models.time_manager import TimeManager
from app.services.player_service import PlayerService
from app.helpers.get_activities import get_activities

time_manager = TimeManager()


class MakeActivity:
    def __init__(self, player_service: PlayerService):
        self.player_service = player_service

    def execute(self, player, actions):
        life_activities = get_activities()

        if actions not in life_activities.keys():
            return f"The action '{actions}' not avaiable"

        new_instance_player = time_manager.make_activities(player, life_activities, actions)
        self.player_service.update_player_statistics(new_instance_player)

        return new_instance_player
    