# app/use_cases/make_activity.py
from app.models.time_manager import TimeManager
from app.helpers.get_activities import get_activities

time_manager = TimeManager()


class MakeActivity:
    def execute(self, actions):
        life_activities = get_activities()

        if actions not in life_activities.keys():
            return f"The action {actions} not avaiable"

        return time_manager.make_activities(life_activities, actions)