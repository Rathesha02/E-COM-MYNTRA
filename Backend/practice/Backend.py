from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cardapp"
)

# Welcome route
@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"message": "Welcome to the Card API!"})

# Get all cards
@app.route("/api/cards", methods=["GET"])
def get_cards():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cards")
    cards = cursor.fetchall()
    cursor.close()
    return jsonify(cards)

if __name__ == "__main__":
    app.run(debug=True)
