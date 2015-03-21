#!flask/bin/python
from flask import Flask, request, jsonify
from thermostat import currentTemp
import atexit
import datetime

app = Flask(__name__)

@app.route('/app/')
def index():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {'time': timestamp, 'temperature': currentTemp().record_temp()}
    return jsonify(data)

@app.route('/record/')
def temp():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {'time': timestamp, 'temperature': currentTemp().record_temp()}
    return jsonify(data)

def shutdown():
    currentTemp().keyboard_interupt()
    shutdown_server()
    return 'Server shutting down...'


if __name__ == '__main__':
    app.run(debug=True)

atexit.register(shutdown)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not Running...')
    func()

    
