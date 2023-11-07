from flask import Flask, render_template, request, jsonify
import random
import json

app = Flask(__name__)

with open('weather_data.json') as json_file:
    activities = json.load(json_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    input_date = request.form['date']
    input_time = request.form['time']

    input_zip_code = request.form['zip_code']

    weather_conditions = list(activities['conditions'].keys())
    weather_condition = random.choice(weather_conditions)
    temperature = str(random.randint(60, 100))

    recommended_activities = activities['conditions'].get(weather_condition, [])

    response = {
        "date": input_date,
        "time": input_time,
        "weather": weather_condition,
        "temperature": temperature,
        "activities": recommended_activities
    }

    return render_template('display.html', data=response)

if __name__ == '__main__':
    app.run(debug=True)
