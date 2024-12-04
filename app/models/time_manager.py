# app/models/time_manager.py
class TimeManager:
    def make_activities(self, player, life_activities, action):
        try:
            _statitics_updates = life_activities[action]
            _statitics_player = player.statistics.__dict__.items()


            # UPDATE PLAYER STATICTICS
            for key, value in _statitics_updates.items():
                print("IN")
                print(key, value)
                print("Player state", key, _statitics_player[key])

        except:
            return f"I DONT MAKE ACTION {action}"







        #for stat_name, stat_value in player.statistics.__dict__.items():
            #print(stat_name)
            #print(stat_value)
            #new_value = random.randint(0, 100)
            #setattr(player.statistics, stat_name, new_value)
            #print(f"Updated {stat_name.capitalize()}: {getattr(player.statistics, stat_name)}")
        #   pass

        return "Aka estoyyyyy"