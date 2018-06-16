import os
import json
from flask import Flask, render_template, request
from flask_socketio import SocketIO
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
socketio = SocketIO(app)


def send_video(file_path):
    msg = {}
    msg['file'] = file_path
    print '{}: {}'.format('file', msg)
    socketio.emit('video', msg)

def send_message(direction, message):
    msg = {}
    msg['direction'] = direction
    msg['message'] = message
    print '{}: {}'.format(direction, message)
    socketio.emit('message', msg)

def send_data(payload):
    print '{}: {}'.format('payload', payload)
    socketio.emit('data', payload)

def send_reset():
    print 'reset'
    socketio.emit('reset', {})

## For Testing purposes
class Message(Resource):
    def get(self, id, direction):
        send_message(direction, id)

class Video(Resource):
    def get(self, path):
        send_video('http://nickdesaulniers.github.io/netfix/demo/frag_bunny.mp4')

class AppRegister(Resource):
    def get(self, payload):
        send_data(payload)

class Data(Resource):
    def get(self, question):
        file_directory = os.path.dirname(os.path.realpath(__file__))
        script_path = os.path.join(file_directory, 'resources/triage_script.json')

        with open(script_path) as f:
            script = json.load(f)
            for d in script[question]['data']:
                send_data(d)
                

api.add_resource(Message, '/message/<string:id>/<string:direction>')
api.add_resource(Video, '/video/<string:path>')
api.add_resource(Data, '/data/<string:question>')

def start():
    socketio.run(app, "0.0.0.0", port=5000)
    
if __name__ == '__main__':
    start()