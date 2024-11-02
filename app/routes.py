# app/routes.py
from flask import Flask
from app.controllers.health_controller import health_check
from app.controllers.player_controller import register_player
from app.controllers.person_controller import get_all_persons
from app.controllers.get_random_person_controller import get_random_person
from app.controllers.time_manager_controller import takeOptionActivity

app = Flask(__name__)

def configure_routes(app):
    app.route('/health', methods=['GET'])(health_check)
    app.route('/register_player', methods=['POST'])(register_player)
    app.route('/get_all_persons', methods=['GET'])(get_all_persons)
    app.route('/get_random_person', methods=['GET'])(get_random_person)
    app.route('/take_option_activity', methods=['POST'])(takeOptionActivity)
    

configure_routes(app)
