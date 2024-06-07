from flask import Flask, jsonify
from bot import user_coins

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Coin Clicker Web App!"

@app.route('/coins/<int:user_id>')
def get_coins(user_id):
    coins = user_coins.get(user_id, 0)
    return jsonify({'user_id': user_id, 'coins': coins})

if __name__ == '__main__':
    app.run(debug=True)
