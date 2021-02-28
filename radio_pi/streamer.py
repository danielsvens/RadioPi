import vlc

from radio_pi.models import Radio


class RadioStream:

    def __init__(self):
        self.uri = None
        self.stream = None

        try:
            self.stream = self.start_radio()
        except Exception as e:
            print('Något gick fel')
            print(str(e))

    def play(self):
        return self.stream.play()

    def stop(self):
        return self.stream.stop()

    def change_station(self, uri):
        self.stop()
        if not self.is_playing():
            self.stream = self.start_radio(uri)
            self.play()

    def retry(self):
        print('Något gick fel, vi testar igen')
        self.stream = self.start_radio()
        self.play()

    def start_radio(self, *uri):
        if uri:
            self.uri = uri[0]
        else:
            query = Radio.query.filter_by(active_station=1).first()
            self.uri = str(query.endpoint)

        return vlc.MediaPlayer(self.uri)

    def is_playing(self):
        return self.stream.is_playing()

    def status(self):
        if not self.is_playing():
            self.retry()
