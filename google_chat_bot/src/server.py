from flask import Flask, render_template, request
from flask_socketio import SocketIO
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
socketio = SocketIO(app)


def send_video(file_path):
	msg = {}
	msg['file'] = file_path
	print msg
	socketio.emit('video', msg)

def send_message(incoming, message):
	msg = {}
	msg['incoming'] = incoming
	msg['message'] = message
	print msg
	socketio.emit('message', msg)

class Message(Resource):
    def get(self, id):
        send_message(False, id)

class Video(Resource):
	def get(self, path):
		send_video('/usr/local/bin')
        
api.add_resource(Message, '/message/<string:id>')
api.add_resource(Video, '/video/<string:path>')

if __name__ == '__main__':
	socketio.run(app, "0.0.0.0", port=5000)
