from radio_pi import db
from radio_pi.models import Radio


class RadioRepository:

    @staticmethod
    def get_station_by_short(short):
        return db.session.query(Radio.endpoint).filter(Radio.short == short).first()

    @staticmethod
    def update_active_station(short):
        db.session.query(Radio).filter(Radio.active_station == 1).update({Radio.active_station: 0})
        db.session.query(Radio).filter(Radio.short == short).update({Radio.active_station: 1})
        db.session.commit()
