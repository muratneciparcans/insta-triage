import os
import json
from flask import Flask, render_template, request
from flask_socketio import SocketIO
from flask_restful import Resource, Api

import utils
app = Flask(__name__)
api = Api(app)
socketio = SocketIO(app)

@socketio.on('connect')
def test_connect():
    socketio.emit('video', {'file': '/assets/videos/remain_standing.mp4'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('started')
def test_connect2():
    socketio.emit('video', {'file': '/assets/videos/remain_standing.mp4'})


class Server(object):
    def __init__(self):
        socketio.on(self, 'started')
        self.app = app;

    def send_video(self, file_path):
        msg = {}
        msg['file'] = file_path
        print '{}: {}'.format('file', msg)
        socketio.emit('video', msg)

    def send_message(self, direction, message):
        msg = {}
        msg['direction'] = direction
        msg['message'] = message
        print '{}: {}'.format(direction, message)
        socketio.emit('message', msg)

    def send_data(self, payload):
        print '{}: {}'.format('payload', payload)
        socketio.emit('data', payload)

    def send_reset(self):
        print 'reset'
        socketio.emit('reset', {})

    def start(self):
        socketio.run(self.app, "0.0.0.0", port=5000)


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
            script = utils.load_script()
            for d in script[question]['data']:
                server.send_data()

    class AllData(Resource):
        def get(self):
            script = utils.load_script()
            """ send all question data for testing
            """
            for k, v in script.iteritems():
                if 'data' in v.keys():
                    for d in v['data']:
                        server.send_data(d)

    def __init__(self, server):
        server.api.add_resource(TestStuff.Message, '/message/<string:id>/<string:direction>')
        server.api.add_resource(TestStuff.Video, '/video/<string:path>')
        server.api.add_resource(TestStuff.Data, '/data/<string:question>')
        server.api.add_resource(TestStuff.AllData, '/all_data')

if __name__ == '__main__':
    server = Server()
    test = TestStuff(server)
    server.start()
