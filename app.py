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
    joke=None
    moods = ["happy", "sad", "excited", "angry", "funny"]
    #mood_list_response = requests.get("https://icanhazdadjoke.com/")
    # if mood_list_response.status_code == 200:
    #     data = mood_list_response.json()
    #     moods = list(data["message"].keys())
    #     moods.sort()
    if request.method == "POST":
        api_url="https://icanhazdadjoke.com/"
        headers={"Accept": "application/json"}
        response = requests.get(api_url, headers=headers )

        if response.status_code == 200:
            joke = response.json().get("joke")
            mood = request.form.get("mood").lower()

    return render_template ("joke.html", joke=joke,moods=moods,mood=mood)
if __name__ == '__main__':
    app.run(debug=True)