#!flask/bin/python
from flask import Flask, request, jsonify
from thermostat import currentTemp
import atexit
import datetime
import requests

app = Flask(__name__)

@app.route('/app/')
def index():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {'time': timestamp, 'temperature': currentTemp().record_temp()}
    return jsonify(data)

@app.route('/record/')
def temp():
    django_url = "http://54.154.99.221:8000/temps/"
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {'time': timestamp, 'temperature': currentTemp().record_temp()}
    json_response = jsonify(data)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(django_url, data=json_response, headers=headers)
    if r.raise_for_status() is None:
        return '<em>Status 200:</em> ' + r
    return 'An error has occurred'

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
