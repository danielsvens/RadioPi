import vlc
from radio_pi.models import Radio
import time


class RadioStream:

    def __init__(self):
        self.uri = None
        self.stream = None

        try:
            self.stream = self.start_radio()
        except Exception as e:

            print("Uri Verkar inte fungera, Testar default p2 musik")
            self.stream = vlc.MediaPlayer('http://sverigesradio.se/topsy/direkt/srapi/163.mp3')

            print('\nStack Trace\n')
            print(str(e))

    def play(self):
        return self.stream.play()

    def stop(self):
        return self.stream.stop()

    def change_station(self, uri):
        self.stop()
        self.stream = vlc.MediaPlayer(uri)
        self.play()

    def retry(self):
        time.sleep(5)
        self.stream = self.start_radio()
        self.play()

    def start_radio(self):
        query = Radio.query.filter_by(active_station=1).first()
        self.uri = str(query.endpoint)
        print(query.station)

        return vlc.MediaPlayer(self.uri)


