from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_weather', methods=['POST'])
def get_weather():
    input_city = request.form['city']
    input_state = request.form['state']
    input_date = request.form['date']
    input_time = request.form['time']

    # Make a request to your partner's weather service to get the weather condition
    partner_weather_endpoint = "https://qnag8pg924.execute-api.us-east-2.amazonaws.com/v1/IdealConditions"
    partner_weather_response = requests.get(partner_weather_endpoint, params={'location': f"{input_city},{input_state}"})

    if partner_weather_response.status_code == 200:
        partner_weather_data = partner_weather_response.json()
        weather_condition = partner_weather_data.get('short_weather', '')  # Use the weather condition received from partner's Lambda

    if partner_weather_response.status_code == 200:
        partner_weather_data = partner_weather_response.json()
        short_weather = partner_weather_data.get('short_weather', {}).get('short_weather', '')

        # Make a request to your Lambda function
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
            "activities": recommended_activities
        }

        return render_template('display.html', data=response)
    else:
        # Handle error when fetching weather condition from partner's service
        error_response = "Failed to retrieve weather condition from partner's service."
        return render_template('error.html', error=error_response)


if __name__ == '__main__':
    app.run(debug=True)
