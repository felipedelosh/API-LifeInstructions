# app/__init__.py
from flask import Flask
from app.routes import configure_routes

app = Flask(__name__)
configure_routes(app)
