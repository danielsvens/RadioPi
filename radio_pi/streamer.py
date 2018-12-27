import vlc

from radio_pi.models import Radio


class RadioStream:

    def __init__(self):
        self.uri = None
        self.stream = self.setup_radio()

    def play(self):
        return self.stream.play()

    def stop(self):
        return self.stream.stop()

    def change_station(self, uri):
        self.stop()
        if not self.is_playing():
            self.stream = self.setup_radio(uri)
            self.play()

    def retry(self):
        print('Something went wrong, lets try again.')
        self.stream = self.setup_radio()
        self.play()

    def setup_radio(self, *uri):
        if uri:
            self.uri = uri[0]
        else:
            query = Radio.query.filter_by(active_station=1).first()
            self.uri = str(query.endpoint)

            if self.uri is None:
                return None

        return vlc.MediaPlayer(self.uri)

    def is_playing(self):
        return self.stream.is_playing()

    def status(self):
        if not self.is_playing():
            self.retry()
