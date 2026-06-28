from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.get("/games")

def get_games():
    with open("games.json") as f:
        games = json.load(f)
    return jsonify(games)

if __name__ == "__main__":
    app.run(debug=True) 