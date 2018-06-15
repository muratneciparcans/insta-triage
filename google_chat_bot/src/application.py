import sys
import readchar

from recorder import record
from recorder import RATE
from recognization import recognize


class Application(object):
    RECORDING = False

    def __init__(self, mode):
        self.RECORDING = mode

    # This can be somewhat triggered by video play
    def listen_key(self):
        key = readchar.readchar()
        original_rec = self.RECORDING

        if key == ' ':
            self.RECORDING = not self.RECORDING
        else:
            if self.RECORDING:
                self.RECORDING = False

        if original_rec != self.RECORDING:
            if self.RECORDING:
                self.start_recording()

    def start_recording(self):
        self.message("Started recording", 'green')
        data = record()
        recognize(data, RATE)