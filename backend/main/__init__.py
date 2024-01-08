from flask import Blueprint



main = Blueprint('main',__name__)

from backend.main import routes