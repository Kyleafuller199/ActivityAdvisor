import json
from urllib import request


def lambda_handler(event, context):
    # Extract the 'location' parameter from the query string
    location = event['queryStringParameters'].get('location', '')

    # Make an HTTP GET request to retrieve weather data
    with request.urlopen(
            "https://qnag8pg924.execute-api.us-east-2.amazonaws.com/v1/IdealConditions?location=" + location) as weather_response:
        forecast_content = weather_response.read().decode('utf-8')
        forecast_json = json.loads(forecast_content)

    # Extract necessary information from the received JSON response
    current_weather = forecast_json["forecast"]["0"]["weather"]
    city = forecast_json["information"]["city"]
    state = forecast_json["information"]["state"]
    date = forecast_json["forecast"]["0"]["date"]
    time = forecast_json["forecast"]["0"]["time"]

    activities = []
    if "Thunderstorms" in current_weather:
        activities = ["Stay indoors", "Watch a movie", "Read a book"]
    elif "Rainy" in current_weather or "Showers" in current_weather:
        activities = ["Watching movies", "Cooking", "Reading"]
    elif "Snow" in current_weather:
        activities = ["Skiing", "Building a snowman", "Drinking hot chocolate"]
    elif "Cloudy" in current_weather:
        activities = ["Walking in the park", "Photography", "Board games"]
    elif "Sunny" in current_weather:
        activities = ["Hiking", "Picnics", "Outdoor sports"]
    elif "Clear" in current_weather:
        activities = ["Stargazing", "Outdoor activities", "Barbecue"]
    elif "Fog" in current_weather:
        activities = ["Take a walk", "Enjoy a hot drink", "Relax"]
    else:
        activities = ["No activities found for this weather condition."]

    # Construct the response object
    response = {
        'statusCode': 200,
        'body': json.dumps({
            "city": city,
            "state": state,
            "date": date,
            "time": time,
            "short_weather": current_weather,
            "activities": activities,
        }),
        'headers': {
            'Content-Type': 'application/json'
        }
    }

    return response