from flask import Flask, render_template, jsonify
import json
import os
import threading

app = Flask(__name__, template_folder='templates', static_folder='static')
COUNTER_FILE = 'counters.json'
lock = threading.Lock()

def read_counters():
    with lock:
        if not os.path.exists(COUNTER_FILE):
            return {'started': 0, 'finished': 0}
        with open(COUNTER_FILE, 'r') as f:
            return json.load(f)

def write_counters(counters):
    with lock:
        with open(COUNTER_FILE, 'w') as f:
            json.dump(counters, f, indent=4)

@app.route('/')
def index():
    counters = read_counters()
    counters['started'] += 1
    write_counters(counters)
    return render_template('index.html')

@app.route('/scenes')
def get_scenes():
    # This is a read-only operation, so no lock needed here.
    with open('scenes.json') as f:
        scenes = json.load(f)
    return jsonify(scenes)

@app.route('/thanks')
def thanks():
    counters = read_counters()
    counters['finished'] += 1
    write_counters(counters)
    return render_template('thanks.html', started=counters['started'], finished=counters['finished'])

if __name__ == '__main__':
    # Debug mode should be off for production.
    # Use a production-ready WSGI server like Gunicorn instead of app.run().
    # Example: gunicorn --bind 0.0.0.0:5000 app:app
    app.run(debug=False, host='0.0.0.0')