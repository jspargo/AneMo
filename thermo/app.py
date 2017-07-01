#!flask/bin/python
from flask import Flask, request, jsonify
from thermostat import currentTemp
import atexit
import datetime
import requests
import json
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.cfg')

app = Flask(__name__)

@app.route('/app/')
def index():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {'time': timestamp, 'temperature': currentTemp().record_temp()}
    return jsonify(data)

@app.route('/record/')
def temp():
    url = config.get('anemoController', 'url')
    django_url = str(url + '/temps/')
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    tdata = {'time': timestamp, 'temperature': currentTemp().record_temp()}
    tbody = json.dumps(tdata)
    headers = {'Content-type': 'application/json', 'Authorization': 'Basic amFjazpzcGFyODdnbw=='}
    try:
        r = requests.post(django_url, data=tbody, headers=headers) 
        if r.raise_for_status() is None:
            return '<em>Status 200:</em> ' + tbody
        return '<em>Server Error</em> - No 200 status received'
    except requests.exceptions.RequestException:
        return '<em>No Connection</em> - Either the server is not running, \
        or this IP is incorrect: <strong>' + django_url + '</strong>' 

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
