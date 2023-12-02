import json

def lambda_handler(event, context):
    city = event.get('city', '')
    state = event.get('state', '')
    date = event.get('date', '')
    time = event.get('time', '')

    weather = event.get('weather', '').lower()
    activities = []

    if "Thunderstorms" in weather:
        activities = ["Stay indoors", "Watch a movie", "Read a book"]
    elif "Rainy" in weather or "Showers" in weather:
        activities = ["Watching movies", "Cooking", "Reading"]
    elif "Snow" in weather:
        activities = ["Skiing", "Building a snowman", "Drinking hot chocolate"]
    elif "Cloudy" in weather:
        activities = ["Walking in the park", "Photography", "Board games"]
    elif "Sunny" in weather:
        activities = ["Hiking", "Picnics", "Outdoor sports"]
    elif "Clear" in weather:
        activities = ["Stargazing", "Outdoor activities", "Barbecue"]
    elif "Fog" in weather:
        activities = ["Take a walk", "Enjoy a hot drink", "Relax"]

    if not activities:
        activities = ["No activities found for this weather condition."]

    return {
        'statusCode': 200,
        'body': json.dumps({
            "city": city,
            "state": state,
            "date": date,
            "time": time,
            "short_weather": event.get('weather', ''),
            "activities": activities
        }),
        'headers': {
            'Content-Type': 'application/json'
        }
    }