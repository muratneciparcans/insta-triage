from flask import Flask, render_template, request
from flask_socketio import SocketIO
from flask_restful import Resource, Api

class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.socketio = SocketIO(self.app)

    def send_video(self, file_path):
        msg = {}
        msg['file'] = file_path
        print '{}: {}'.format('file', msg)
        self.socketio.emit('video', msg)

    def send_message(self, direction, message):
        msg = {}
        msg['direction'] = direction
        msg['message'] = message
        print '{}: {}'.format(direction, message)
        self.socketio.emit('message', msg)

    def send_register(self, payload):
        msg = {}
        msg['payload'] = payload
        print '{}: {}'.format('payload', msg)
        self.socketio.emit('registry', msg)

    def start(self):
        self.socketio.run(self.app, "0.0.0.0", port=5000)


class TestStuff:
    ## For Testing purposes
    class Message(Resource):
        def get(self, id, direction):
            send_message(direction, id)

    class Video(Resource):
        def get(self, path):
            send_video('http://nickdesaulniers.github.io/netfix/demo/frag_bunny.mp4')

    class AppRegister(Resource):
        def get(self, payload):
            send_register(payload)

    def __init__(self, api):
        api.add_resource(Message, '/message/<string:id>/<string:direction>')
        api.add_resource(Video, '/video/<string:path>')
        api.add_resource(AppRegister, '/registry/<string:payload>')
