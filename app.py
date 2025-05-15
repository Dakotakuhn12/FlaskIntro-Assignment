import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/joke", methods=["GET", "POST"])
def joke():
    error = None
    mood = ""
    moods = []
    mood_list_response = requests.get("https://icanhazdadjoke.com/")
if __name__ == '__main__':
    app.run(debug=True)