from flask import render_template, request, redirect, url_for, make_response

from radio_pi import app, db
from radio_pi import radio
from radio_pi.models import Radio


@app.route('/')
def index():
    data = dict()
    station_list = db.session.query(Radio.station, Radio.short).all()
    for k, v in station_list:
        data.update({k: v})
    current_station = Radio.query.filter_by(active_station=1).first()
    return render_template('index.html', current_station=current_station, data=data)


@app.route('/', methods=['POST'])
def change_channel():
    id = request.form.get('stations')
    station = [s for s in db.session.query(Radio.endpoint).filter(Radio.short == id).first()]
    db.session.query(Radio).filter(Radio.active_station == 1).update({Radio.active_station: 0})
    db.session.query(Radio).filter(Radio.short == id).update({Radio.active_station: 1})
    db.session.commit()
    radio.change_station(station[0])
    return redirect(url_for('index'))


@app.route('/volume', methods=['POST'])
def volume_slider():
    volume = request.form.get('volume')
    radio.set_volume(volume)
    return make_response('', 200)
