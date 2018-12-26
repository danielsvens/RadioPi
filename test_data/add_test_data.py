from radio_pi import db
from radio_pi.models import Radio
from datetime import datetime

'''
@ Adding some test data to db.
'''

print('Dropping tables')
db.drop_all()
print('Creating tables')
db.create_all()

radio_p1 = Radio(endpoint='http://sverigesradio.se/topsy/direkt/srapi/132.mp3',
                 station='Sveriges Radio p1',
                 short='P1',
                 active_station=0,
                 image='https://static-cdn.sr.se/sida/images/132/2186745_512_512.jpg?preset=api-default-square',
                 last_modified=datetime.now()
                 )

radio_p2 = Radio(endpoint='http://sverigesradio.se/topsy/direkt/srapi/163.mp3',
                 station='Sveriges Radio p2',
                 short='P2',
                 active_station=1,
                 image='https://static-cdn.sr.se/sida/images/2562/3679054_1400_1400.jpg?preset=api-default-square',
                 last_modified=datetime.now()
                 )

radio_p3 = Radio(endpoint='http://sverigesradio.se/topsy/direkt/srapi/164.mp3',
                 station='Sveriges Radio p3',
                 short='P3',
                 active_station=0,
                 image='https://static-cdn.sr.se/sida/images/164/2186756_512_512.jpg?preset=api-default-square',
                 last_modified=datetime.now()
                 )


print('Adding data to tables')
db.session.add(radio_p1)
db.session.add(radio_p2)
db.session.add(radio_p3)
db.session.commit()
db.session.close()
print('Done')
