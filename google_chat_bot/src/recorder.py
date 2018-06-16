#Instead of adding silence at start and end of recording (values=0) I add the original audio . This makes audio sound more natural as volume is >0. See trim()
#I also fixed issue with the previous code - accumulated silence counter needs to be cleared once recording is resumed.

from array import array
from struct import pack
from sys import byteorder
import copy
import pyaudio
import wave
import io
import tempfile
import readchar
import time

# @Note Silence Detection to difficult
THRESHOLD = 2000  # audio levels not normalised.

CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
FRAME_MAX_VALUE = 2 ** 15 - 1
NORMALIZE_MINUS_ONE_dB = 10 ** (-1.0 / 20)
RATE = 44100
SECONDS_TO_WAIT = 3 # How many seconds of leeway after input
SILENT_CHUNKS = SECONDS_TO_WAIT * RATE / CHUNK_SIZE  # [seconds of silence trimmed]
CHANNELS = 1
TRIM_APPEND = RATE / 4

def record():
    """Record a word or words from the microphone and 
    return the data as an array of signed shorts."""

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, 
            rate=RATE, input=True, output=True, frames_per_buffer=CHUNK_SIZE)

    data_all = array('h')
    record_while_loud(stream, data_all) # Too risky
    # record_with_space(stream, data_all)

    sample_width = audio.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save temporary file
    wave_file = tempfile.NamedTemporaryFile().name

    wf = wave.open(wave_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data_all)
    wf.close()

    # @TODO: Check if this is actually necessary
    with io.open(wave_file, 'rb') as audio_file:
        return audio_file.read()

def record_with_space(stream, data_all):
    recording = False

    while True:
        key = readchar.readchar()
        if key == ' ':
            break;
        else:
            time.sleep(0.01)

    time.sleep(0.01)

    while True:
        # little endian, signed short$
        print 'I got here'
        print CHUNK_SIZE
        data_chunk = array('h', stream.read(CHUNK_SIZE))


        if byteorder == 'big':
            data_chunk.byteswap()
        data_all.extend(data_chunk)

        key = readchar.readchar()
        if key == ' ':
            break;
        else:
            time.sleep(0.01)

def record_while_loud(stream, data_all):
    silent_chunks = 0
    audio_started = False

    while True:
        # little endian, signed short
        data_chunk = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            data_chunk.byteswap()
        data_all.extend(data_chunk)

        silent = is_silent(data_chunk)

        if audio_started:
            if silent:
                #print 'Its silent right?'
                silent_chunks += 1
                if silent_chunks > SILENT_CHUNKS:
                    break
            else: 
                silent_chunks = 0
        elif not silent:
            print "I started"
            audio_started = True

    print 'Detected silence'

def is_silent(data_chunk):
    """Returns 'True' if below the 'silent' threshold"""
    return max(data_chunk) < THRESHOLD