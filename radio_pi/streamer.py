import vlc
from radio_pi.models import Radio


class RadioStream:

    def __init__(self):
        try:
            query = Radio.query.filter_by(active_station=1).first()
            self.uri = str(query.endpoint)
            print(query.station)

            self.stream = vlc.MediaPlayer(self.uri)

        except Exception as e:

            print("Uri Verkar inte fungera, Testar default p2 musik")
            self.stream = vlc.MediaPlayer('http://sverigesradio.se/topsy/direkt/srapi/163.mp3')

            print('\nStack Trace\n')
            print(str(e))

    def play(self):
        return self.stream.play()

    def stop(self):
        return self.stream.stop()

    def change_song(self, uri):
        self.stop()
        self.stream = vlc.MediaPlayer(uri)
        self.play()

