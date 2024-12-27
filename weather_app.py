import requests  # Import the requests library for making HTTP requests.

# Function to fetch and display the weather for a given city.
def get_weather(city):
    api_key = '406331ad91ddbe5c22ec2c91fb2cf63e'  # OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    response = requests.get(url)  # Make a GET request to the API.
    data = response.json()  # Parse the JSON response.
    
    if data['cod'] == 200:  # Check if the API returned a successful response.
        weather = data['weather'][0]['description']  # Extract weather description.
        temp = data['main']['temp']  # Extract temperature.
        print(f'Weather in {city}: {weather}, {temp}°C')  # Display weather info.
    else:
        print(f'City {city} not found.')  # Handle the case where the city is invalid.

get_weather('Pangasinan')  # Example call to the function.

