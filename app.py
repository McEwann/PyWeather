import requests
import config
from flask import Flask, request, render_template
weather = "Default"

app = Flask(__name__, static_url_path='/static')
# API key here
api_key = config.api_key

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["city"]
        # Get the current weather information for the city
        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}&units=metric")
        if weather_data.status_code == 404:
            error_message = "City not found, check spelling and try again."
            return render_template("index.html", error_message=error_message)
        else:
            weather = weather_data.json()["weather"][0]["main"]
            temp = weather_data.json()["main"]["temp"]
            return render_template("index.html", city=user_input, weather=weather, temp=temp)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)