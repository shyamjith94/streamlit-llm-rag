import requests


class WatherToolUtils:

    def get_langitude_longitude(self,city:str)->tuple[str,str]:
        """ 
        get latitude and longitude
        use OpenWeatherMap API
        """
        geo_reponse = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
                params={
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json",
            },
            timeout=10,
        )
        geo_reponse.raise_for_status()
        location = geo_reponse.json().get("results", [])[0]
        return location.get("latitude"), location.get("longitude")
    def weather_row_data(self, city:str)->dict:
        """
        Get the current weather raw data information
        """
        latitude, longitude = self.get_langitude_longitude(city)
        weather_response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "temperature_2m,"
                "relative_humidity_2m,"
                "apparent_temperature,"
                "weather_code,"
                "wind_speed_10m"
            ),
            "timezone": "auto",
        },
        timeout=10,
    )
        weather_response.raise_for_status()
        current = weather_response.json().get("current")
        return {
        "city": current.get("name"),
        "country": current.get("country"),
        "temperature": current.get("temperature_2m"),
        "feels_like": current.get("apparent_temperature"),
        "humidity": current.get("relative_humidity_2m"),
        "wind_speed": current.get("wind_speed_10m"),
        "weather_code": current["weather_code"],
        "time": current["time"],
    }
    def weather_formatted(self, city:str)->str:
        """
        Get the current weather formatted data information
        """
        weather_row_data = self.weather_row_data(city)
        return f"""
        Current weather in {city}:
        Temperature: {weather_row_data.get('temperature')}°C
        Relative Humidity: {weather_row_data.get('relative_humidity')}%
        Apparent Temperature: {weather_row_data.get('apparent_temperature')}°C
        Weather Code: {weather_row_data.get('weather_code')}
        Wind Speed: {weather_row_data.get('wind_speed_10m')} km/h
        Time: {weather_row_data.get('time')}
        """