# app/models/statistics.py
class Statistics:
    def __init__(self):
        self.energy = 100  # 100 is full, 0 is exhausted
        self.hunger = 100  # 100 is full, 0 is starving
        self.intelligence = 50
        self.strength = 50
        self.mental_health = 70  # 100 is optimal, 0 is critical
        self.physical_health = 70  # 100 is optimal, 0 is critical
        self.social_skills = 50
        self.job_performance = 50

    def update_stat(self, stat_name, value):
        if hasattr(self, stat_name):
            new_value = getattr(self, stat_name) + value
            setattr(self, stat_name, max(0, min(new_value, 100)))  # Keeps stats within 0 to 100 range
        else:
            raise ValueError(f"Statistic '{stat_name}' does not exist.")

    def __repr__(self):
        return (f"Energy: {self.energy}, Hunger: {self.hunger}, Intelligence: {self.intelligence}, "
                f"Strength: {self.strength}, Mental Health: {self.mental_health}, Physical Health: {self.physical_health}, "
                f"Social Skills: {self.social_skills}, Job Performance: {self.job_performance}")
