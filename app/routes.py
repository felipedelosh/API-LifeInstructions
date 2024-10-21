# app/routes.py
from flask import Flask
from app.controllers.health_controller import health_check
from app.controllers.player_controller import register_player
from app.controllers.get_random_person_controller import get_random_person

app = Flask(__name__)

def configure_routes(app):
    app.route('/health', methods=['GET'])(health_check)
    app.route('/register_player', methods=['POST'])(register_player)
    app.route('/get_random_person', methods=['GET'])(get_random_person)
    

configure_routes(app)
