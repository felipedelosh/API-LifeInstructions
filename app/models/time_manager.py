# app/models/time_manager.py
class TimeManager:
    def make_activities(self, player, life_activities, action):
        _statitics_updates = life_activities[action]
        _statitics_player = player.statistics.__dict__

        # UPDATE PLAYER STATICTICS
        for key, value in _statitics_updates.items():
            new_value = _statitics_player[key] + value
            setattr(player.statistics, key, new_value)

        return player