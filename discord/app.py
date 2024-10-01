from flask import Flask, request, jsonify, render_template
import os
import datetime

app = Flask(__name__)

# Directory to store the logs
LOG_DIR = 'logs'

# Ensure the logs directory exists
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def save_log(log_type, log_data):
    """
    Save the log to a file. Logs are stored in a directory structure based on log type.
    :param log_type: Type of the log (webrtc or ringrtc)
    :param log_data: The log content
    """
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'{log_type}_log_{timestamp}.txt'
    file_path = os.path.join(LOG_DIR, log_type, filename)

    # Ensure subdirectory for log type exists
    log_type_dir = os.path.join(LOG_DIR, log_type)
    if not os.path.exists(log_type_dir):
        os.makedirs(log_type_dir)

    with open(file_path, 'w') as log_file:
        log_file.write(log_data)

@app.route('/')
def index():
    """
    Serve the main HTML page.
    """
    return render_template('index.html')

@app.route('/log/<log_type>', methods=['POST'])
def log_call(log_type):
    """
    Endpoint to receive WebRTC and RingRTC logs from the form or external requests.
    :param log_type: The type of log ('webrtc' or 'ringrtc')
    """
    if log_type not in ['webrtc', 'ringrtc']:
        return jsonify({'error': 'Invalid log type'}), 400

    # Get the log data from the form or request
    log_data = request.form.get('log_data') or request.get_data(as_text=True)

    if not log_data:
        return jsonify({'error': 'No log data received'}), 400

    # Save the log
    save_log(log_type, log_data)

    return jsonify({'message': f'{log_type} log received and stored.'}), 200

if __name__ == '__main__':
    app.run(debug=True)
