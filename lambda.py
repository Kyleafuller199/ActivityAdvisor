import json

def lambda_handler(event, context):
    city = event.get('city', '')
    state = event.get('state', '')
    date = event.get('date', '')
    time = event.get('time', '')

    weather = event.get('weather', '').lower()
    activities = []

    if "thunderstorms" in weather:
        activities = ["Stay indoors", "Watch a movie", "Read a book"]
    elif "rain" in weather or "showers" in weather:
        activities = ["Watching movies", "Cooking", "Reading"]
    elif "snow" in weather:
        activities = ["Skiing", "Building a snowman", "Drinking hot chocolate"]
    elif "cloudy" in weather:
        activities = ["Walking in the park", "Photography", "Board games"]
    elif "sunny" in weather:
        activities = ["Hiking", "Picnics", "Outdoor sports"]
    elif "clear" in weather:
        activities = ["Stargazing", "Outdoor activities", "Barbecue"]
    elif "fog" in weather:
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