from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)
COUNTER_FILE = 'counters.json'

def read_counters():
    if not os.path.exists(COUNTER_FILE):
        return {'started': 0, 'finished': 0}
    with open(COUNTER_FILE, 'r') as f:
        return json.load(f)

def write_counters(counters):
    with open(COUNTER_FILE, 'w') as f:
        json.dump(counters, f)

@app.route('/')
def index():
    counters = read_counters()
    counters['started'] += 1
    write_counters(counters)
    return render_template('index.html')

@app.route('/scenes')
def get_scenes():
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
    app.run(debug=True, host='0.0.0.0')