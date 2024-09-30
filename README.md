# WebRTC Logger Using Flask and SocketIO

![WebRTC Logger](https://cdn.discordapp.com/attachments/1225420924623257611/1290458180152852502/image.png?ex=66fc8855&is=66fb36d5&hm=2d3c378002de5bde82fbdad70965d3d484237d4b938a632907f8f1b04d892280&)

# Overview
This application is a comprehensive WebRTC logger built with Flask and SocketIO. It captures detailed information about WebRTC connections, including ICE candidates, connection states, and various statistics. The logger helps in analyzing WebRTC interactions and troubleshooting issues.

# Features
Logs incoming and outgoing WebRTC connections.
Captures and logs ICE candidates, including IP addresses and ports.
Tracks connection state changes.
Collects detailed statistics every second for all active WebRTC connections.
Easy to integrate with existing WebRTC applications.

# Requirements
Python 3.6 or higher
```bash
pip install Flask
pip install Flask-SocketIO
```
# Installation
Clone the repository
```bash
git clone https://github.com/SleepTheGod/WebRTC-logger-using-Flask-and-SocketIO.git
```

# Navigate to the project directory
```bash
cd WebRTC-logger-using-Flask-and-SocketIO
```

# Install the required packages
```bash
pip install flask flask-socketio
```

# Usage
Run the application

```bash
python app.py
```

Once you do this then you will need to navigate to the following
```
Open your web browser and navigate to
```
# Now you need to do the following
Click the "Start Logging" button to begin capturing WebRTC statistics. Click "Stop Logging" to finish logging.

# Log File
The logs are saved in a file named webrtc_logs.txt in the same directory as app.py. This file contains detailed logs of WebRTC statistics, connections, and candidates.

# Contributing
If you would like to contribute to this project, please feel free to submit a pull request or open an issue for discussion.
