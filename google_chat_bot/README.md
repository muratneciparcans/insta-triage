### Voice Control

This application is using the Google Cloud Platform Speech Recognition API, to install a user and [get started](https://cloud.google.com/speech/docs/getting-started) (UniteLabs user will be setup in the future)

The language of choice is python. Pip packages are installed via: `pip install -r requirements.txt` in your favourite environment.

Note: This is a pure "playground project" for now, as the client libraries are currently not recommended for production use by Google.

Starting point is `test.py` - project is halted.
### Installation

#### macOS
On macOS, to install `pyaudio` with pip, you first have to install `brew install portaudio`

External Dependencies:
```
brew install ffmpeg
brew install libevent
```

## Dialogflow
Still unclear: Conversational Logic
This minimal prototype is based on Dialogflow.

All based on this tutorial:
https://codelabs.developers.google.com/codelabs/actions-1/index.html#3

Some examples of fullfillment code:
https://github.com/dialogflow/dialogflow-fulfillment-nodejs