from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from radio_pi.streamer import RadioStream

radio = RadioStream()
radio.play()

from radio_pi import routes