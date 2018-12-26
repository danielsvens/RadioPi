from radio_pi import db
from datetime import datetime


class Radio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    endpoint = db.Column(db.String(250), nullable=False)
    station = db.Column(db.String(80), nullable=False)
    short = db.Column(db.String(80), nullable=True)
    active_station = db.Column(db.Integer, default=0, nullable=False)
    image = db.Column(db.String(250), nullable=True)
    last_modified = db.Column(db.DateTime, nullable=False, onupdate=datetime.now)

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.station)

