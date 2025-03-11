from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "ESP Lock Server is Running!"

@app.route('/unlock', methods=['POST'])
def unlock():
    return "Unlocking the Bike!", 200

@app.route('/lock', methods=['POST'])
def lock():
    return "Locking the Bike!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
