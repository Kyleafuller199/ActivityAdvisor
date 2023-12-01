import json

def lambda_handler(event, context):
    city = event['queryStringParameters'].get('city', '')
    state = event['queryStringParameters'].get('state', '')
    date = event['queryStringParameters'].get('date', '')
    time = event['queryStringParameters'].get('time', '')
    short_weather = event['queryStringParameters'].get('short_weather', '')

    activities = []

    if "Thunderstorms" in short_weather:
        short_weather = "Thunderstorms"
        activities = ["Stay indoors", "Watch a movie", "Read a book"]
    elif "Rain" in short_weather or "Showers" in short_weather:
        short_weather = "Rainy"
        activities = ["Watching movies", "Cooking", "Reading"]
    elif "Snow" in short_weather:
        short_weather = "Snow"
        activities = ["Skiing", "Building a snowman", "Drinking hot chocolate"]
    elif "Cloudy" in short_weather:
        short_weather = "Cloudy"
        activities = ["Walking in the park", "Photography", "Board games"]
    elif "Sunny" in short_weather:
        short_weather = "Sunny"
        activities = ["Hiking", "Picnics", "Outdoor sports"]
    elif "Clear" in short_weather:
        short_weather = "Clear"
        activities = ["Stargazing", "Outdoor activities", "Barbecue"]
    elif "Fog" in short_weather:
        short_weather = "Foggy"
        activities = ["Take a walk", "Enjoy a hot drink", "Relax"]

    if not activities:
        activities = ["No activities found for this weather condition."]

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            "city": city,
            "state": state,
            "date": date,
            "time": time,
            "short_weather": short_weather,
            "activities": activities
        })
    }