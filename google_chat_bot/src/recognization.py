
import sys

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from google.cloud.speech_v1.types import SpeechContext


# @TODO: Check again what the audio type actually is, make this simpler and try
def recognize(content, rate):
    speech_client = speech.SpeechClient()
    speech_config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=rate,
        language_code="en-US"
    )

    print ('Trying to recognize')
    audio = types.cloud_speech_pb2.RecognitionAudio(content=content)
    response = speech_client.recognize(speech_config, audio)

    # @TODO: Do something with the response
    return response

