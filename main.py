from flask import Flask, render_template, request, jsonify
import random
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    input_date = request.form['date']
    input_time = request.form['time']
    input_zip_code = request.form['zip_code']

    # Simulate fetching weather conditions randomly (replace this with actual weather data retrieval)
    weather_conditions = ['Sunny', 'Rain', 'Snow', 'Cloudy']
    weather_condition = random.choice(weather_conditions)
    temperature = str(random.randint(60, 100))

    # Make a request to the Lambda function
    lambda_endpoint = "https://1ha9lsdel6.execute-api.us-east-2.amazonaws.com/Test/activity_advisor"
    lambda_response = requests.get(lambda_endpoint, params={'condition': weather_condition})

    if lambda_response.status_code == 200:
        lambda_data = lambda_response.json()
        recommended_activities = lambda_data.get('activities', [])
    else:
        recommended_activities = []

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
