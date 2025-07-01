from flask import Flask
from flask_cors import CORS
from app.data import carregar_usuarios

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})
carregar_usuarios()
from app import routes
