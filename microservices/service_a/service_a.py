from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "Service A is running!"

@app.route('/fail')
def fail():
    if random.random() > 0.7:
        return "Service A failed!", 500
    return "Service A is healthy."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

