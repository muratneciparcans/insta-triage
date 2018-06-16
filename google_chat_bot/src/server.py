import os
import json
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

    def send_data(self, payload):
        print '{}: {}'.format('payload', payload)
        self.socketio.emit('data', payload)

    def send_reset(self):
        print 'reset'
        self.socketio.emit('reset', {})

    def start(self):
        self.socketio.run(self.app, "0.0.0.0", port=5000)
        
class TestStuff:
    ## For Testing purposes
    class Message(Resource):
        def get(self, id, direction):
            server.send_message(direction, id)

    class Video(Resource):
        def get(self, path):
            server.send_video('http://nickdesaulniers.github.io/netfix/demo/frag_bunny.mp4')

    class Data(Resource):
        def get(self, question):
            server.send_data(question)

    def __init__(self, server):
        server.api.add_resource(TestStuff.Message, '/message/<string:id>/<string:direction>')
        server.api.add_resource(TestStuff.Video, '/video/<string:path>')
        server.api.add_resource(TestStuff.Data, '/data/<string:question>')

if __name__ == '__main__':
    server = Server()
    test = TestStuff(server)
    server.start()
