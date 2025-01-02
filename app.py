from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def weather():
    city = request.form["city"]
    api_key = "5364fda91d12129e82555923430acf36"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url).json()

        if response.get("cod") != 200:  # Check if there was an error in fetching data
            return render_template("index.html", error=response.get("message", "Unknown error"))

        # Extracting necessary data
        weather_data = {
            "city": city,
            "temperature": response["main"]["temp"],
            "description": response["weather"][0]["description"],
            "icon": response["weather"][0]["icon"],
        }

        return render_template("index.html", weather=weather_data)
    
    except Exception as e:
        # If something goes wrong during the request or parsing, return an error
        return render_template("index.html", error=str(e))

if __name__ == "__main__":
    app.run(debug=True)
