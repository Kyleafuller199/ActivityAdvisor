from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_weather', methods=['POST'])
def get_weather():
    input_location = request.form['location']

    # Make a request to your Lambda function to get weather data using GET
    lambda_endpoint = "https://1ha9lsdel6.execute-api.us-east-2.amazonaws.com/Test/activity_advisor"
    lambda_response = requests.get(lambda_endpoint, params={'location': input_location})

    if lambda_response.status_code == 200:
        weather_data = lambda_response.json()
        return render_template('display.html', data=weather_data)
    else:
        error_response = "Failed to retrieve weather data from Lambda function."
        return render_template('error.html', error=error_response)


if __name__ == '__main__':
    app.run(debug=True)
