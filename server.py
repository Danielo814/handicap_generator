from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def say_hello():
    return "Hello"

@app.route('/api')
def hello_api():
    return jsonify({'player': 45})

@app.route('/api/player')
def player():
    return jsonify({
    'name': 'Daniel Ojeda',
    'index': 5.2, 
    'rounds':
        [{'course': "Harding Park", 'par': 72, 'date': '5/7/19', 'score': 70}, 
        {'course': "Harding Park", 'par': 72, 'date': '5/7/19', 'score': 70}]
    })