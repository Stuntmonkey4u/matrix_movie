from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scenes')
def get_scenes():
    with open('scenes.json') as f:
        scenes = json.load(f)
    return jsonify(scenes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')