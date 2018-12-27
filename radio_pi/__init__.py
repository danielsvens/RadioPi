from flask import Flask
from flask_apscheduler import APScheduler
from flask_sqlalchemy import SQLAlchemy

import config


def is_radio_playing():
    radio.status()


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

from radio_pi.streamer import RadioStream

radio = RadioStream()
radio.play()

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

from radio_pi import routes
