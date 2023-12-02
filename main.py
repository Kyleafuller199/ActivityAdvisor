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

    # Make a request to your partner's weather service
    partner_weather_endpoint = "https://qnag8pg924.execute-api.us-east-2.amazonaws.com/v1/IdealConditions"
    partner_weather_response = requests.get(partner_weather_endpoint,
                                            params={'location': f"{input_city},{input_state}"})

    if partner_weather_response.status_code == 200:
        partner_weather_data = partner_weather_response.json()

        # Print the partner_weather_data to verify its structure
        print(partner_weather_data)

        # Ensure 'city' and 'state' keys exist in partner_weather_data
        if 'city' in partner_weather_data and 'state' in partner_weather_data:
            # Make a request to your Lambda function
            lambda_endpoint = "https://1ha9lsdel6.execute-api.us-east-2.amazonaws.com/Test/activity_advisor"
            lambda_payload = {
                "city": partner_weather_data['city'],
                "state": partner_weather_data['state'],
                "date": input_date,
                "time": input_time
            }
            lambda_response = requests.post(lambda_endpoint, json=lambda_payload)

            if lambda_response.status_code == 200:
                lambda_data = lambda_response.json()
                response = {
                    "date": lambda_data.get('date', ''),
                    "time": lambda_data.get('time', ''),
                    "weather": lambda_data.get('short_weather', ''),
                    "activities": lambda_data.get('activities', [])
                }
                return render_template('display.html', data=response)
            else:
                error_response = "Failed to retrieve weather data from Lambda function."
                return render_template('error.html', error=error_response)
        else:
            error_response = "City or state data not found in partner's service response."
            return render_template('error.html', error=error_response)
    else:
        error_response = "Failed to retrieve weather data from partner's service."
        return render_template('error.html', error=error_response)


if __name__ == '__main__':
    app.run(debug=True)
