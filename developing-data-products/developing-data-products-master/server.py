from flask import Flask
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/roll-dice')
def roll_dice():
    return str(np.random.choice([1, 2, 3, 4, 5, 6], 1))