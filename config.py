import os


USE_ROUNDED_COORDS = False
OPENWEATHER_API = os.getenv("OPENWEATHER_API")
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_API + "&lang=ru&"
    "units=metric"
)
