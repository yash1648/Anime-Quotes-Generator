import flask
from .routes import route

app=flask.Flask(__name__)

app.register_blueprint(route)

