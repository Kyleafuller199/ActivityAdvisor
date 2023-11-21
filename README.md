# Weather Activity Recommender Service

## Overview
This application is designed to provide activity recommendations based on the forecasted weather conditions for a specified location. It utilizes Flask, a web framework in Python, to create a web interface where users can input their date, time, and zip code to receive suggested activities suitable for the weather conditions at that time and location.

## Usage

### Setup and Dependencies
- **Flask Framework:** Utilized for the web application.
- **Requests Module:** Used for making HTTP requests.
- **Random Module:** Simulates fetching weather conditions randomly for demonstration purposes.

### Running the Application
1. **Installation:** Ensure you have Python installed. Install the necessary dependencies by running: `pip install flask requests`.
2. **Run the Application:** Execute the `main.py` file to start the Flask server. The server runs locally and can be accessed via a web browser.

### Endpoint and Inputs
- **Endpoint:** The web interface is accessible at the root URL (`/`) where users can input date, time, and zip code.
- **POST Request to `/get_weather`:** Submits the user inputs to retrieve suggested activities. The inputs include date, time, and zip code.
  
## Workflow

### Fetching Weather Conditions
- **Random Weather Generation:** Simulates weather conditions randomly by selecting from predefined weather types such as 'Sunny', 'Rain', 'Snow', or 'Cloudy'.
- **Lambda Function Integration:** Utilizes the `requests` module to send a GET request to an AWS Lambda Function endpoint (`https://1ha9lsdel6.execute-api.us-east-2.amazonaws.com/Test/activity_advisor`) passing the generated weather condition as a parameter.

### Display
- **Response Parsing:** Upon receiving a successful response (HTTP status code 200) from the Lambda function, the application processes the returned JSON data to extract recommended activities.
- **Render Display:** Renders the weather conditions, temperature, user inputs, and suggested activities on the `display.html` template, providing users with the suggested activities for the specified weather conditions.

## Notes
- This application currently simulates weather conditions and uses a placeholder Lambda function URL for demonstration purposes. Adjustments will be needed to integrate with a live weather API and a functional Lambda service for accurate data.
- Ensure to handle error scenarios gracefully, considering situations where the Lambda function may not return expected data or in case of network failures.


Version 1.1
