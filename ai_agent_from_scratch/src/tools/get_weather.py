
SAMPLE_WEATHER = {
    "tokyo": {"celcius": 25, "condition": "sunny"},
    "new york": {"celcius": 15, "condition": "partially cloudy"},
    "london": {"celcius": 10, "condition": "rainy"},
    "delhi": {"celcius": 35, "condition": "hot"},
}

def get_weather(city: str) -> str:
    city = city.lower()
    if city in SAMPLE_WEATHER:
        weather = SAMPLE_WEATHER[city]
        return f"The weather in {city.title()} is {weather['condition']} with a temperature of {weather['celcius']}°C."
    else:
        return f"Sorry, I don't have weather information for {city.title()}."