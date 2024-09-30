from flask import Flask, render_template, request
from flask_socketio import SocketIO
import logging
import json

# Initialize Flask and SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Configure logging
logging.basicConfig(filename='webrtc_logs.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('log_webrtc_data')
def handle_log(data):
    logging.info(json.dumps(data))  # Log the entire data object
    print(f"Received data: {data}")

@socketio.on('connection_event')
def handle_connection_event(data):
    logging.info(f"Connection event: {data['event']} - Peer: {data['peer_ip']}")
    print(f"Connection event: {data['event']} - Peer: {data['peer_ip']}")

if __name__ == '__main__':
    socketio.run(app, debug=True)
