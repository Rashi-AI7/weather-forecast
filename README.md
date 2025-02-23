# weather-forecast
A Python-based weather app that fetches real-time weather data using the WeatherStack API and logs the results.


Features:
Fetches real-time weather details like temperature, humidity, wind speed, and weather conditions.
Uses an API key stored in a .env file for security.
User-friendly CLI to enter a city name and get instant weather updates.

Requirements:
Make sure you have the following installed before running the project-

1. Python 3+
2. requests library
3. python-dotenv library

Create a virtual environment (optional but recommended):
sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

Install required dependencies:
sh
Copy
Edit
pip install -r requirements.txt
Set up your .env file:
Create a file named .env in the project directory.

How to use it?
1. Go to [WeatherStack](https://weatherstack.com/) and sign up for a free API key.
2. Create a new file named `.env` in the project folder.
3. Copy this line and paste it into `.env`:
   WEATHER_API_KEY=your_api_key_here
4. Save the file and run the script!


Example Output:

Enter your city: Kanpur

Fetching Weather data..

Weather in Kanpur
Temperature: 30°C
Humidity: 65%
Condition: Partly Cloudy
Wind Speed: 10 km/h

If the API key is invalid or expires, regenerate it from WeatherStack.
Contributing
Feel free to fork the repo and submit pull requests for improvements!

License:
The project is open source under the MIT License.