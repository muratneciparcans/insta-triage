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


## For Testing purposes
class Message(Resource):
    def get(self, id, direction):
        send_message(direction, id)

class Video(Resource):
    def get(self, path):
        send_video(path)

api.add_resource(Message, '/message/<string:id>/<string:direction>')
api.add_resource(Video, '/video/<string:path>')


def start():
    socketio.run(app, "0.0.0.0", port=5000)
    
if __name__ == '__main__':
    start()