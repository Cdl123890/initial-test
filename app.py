from flask import Flask, jsonify, render_template
import random
from ideas import lifestyle_ideas

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/ideas", methods=["GET"])
def get_ideas():
    return jsonify(lifestyle_ideas)

@app.route("/api/ideas/random", methods=["GET"])
def get_random_idea():
    idea = random.choice(lifestyle_ideas)
    return jsonify(idea)

if __name__ == "__main__":
    app.run(debug=True)
