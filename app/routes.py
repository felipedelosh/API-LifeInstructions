# app/routes.py
from flask import Flask
from app.controllers.player_controller import register_player
from app.controllers.health_controller import health_check

app = Flask(__name__)

def configure_routes(app):
    app.route('/register_player', methods=['POST'])(register_player)
    app.route('/health', methods=['GET'])(health_check)

configure_routes(app)
