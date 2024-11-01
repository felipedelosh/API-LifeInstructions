# app/herlers/person_to_player_mapper.py
from app.models.person import Person
from app.models.player import Player

def map_person_to_player(person: Person) -> Player:
    player = Player(person.id)
    player.first_name = person.first_name
    player.middle_name = person.middle_name
    player.last_name = person.last_name
    player.second_last_name = person.second_last_name
    player.sex = person.sex
    player.age = person.age
    player.location = person.location
    player.plausible_death = person.plausible_death
    return player
