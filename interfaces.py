from typing import Any, List
from dataclasses import dataclass


@dataclass
class WeatherCurrent:
    location: str
    region: str
    country: str
    latitude: float
    longitude: float
    timezone: str
    local_time: str
    temp_c: int
    temp_f: float
    feels_like_c: int
    feels_like_f: float
    humidity: int
    cloud: int
    daytime: bool
    condition: str
    icon_url: str
    wind_mph: float
    wind_kph: float
    wind_direction: str
    wind_degree: int

    @staticmethod
    def from_dict(obj: Any) -> 'WeatherCurrent':
        _location = str(obj.get("location"))
        _region = str(obj.get("region"))
        _country = str(obj.get("country"))
        _latitude = float(obj.get("latitude"))
        _longitude = float(obj.get("longitude"))
        _timezone = str(obj.get("timezone"))
        _local_time = str(obj.get("local_time"))
        _temp_c = int(obj.get("temp_c"))
        _temp_f = float(obj.get("temp_f"))
        _feels_like_c = int(obj.get("feels_like_c"))
        _feels_like_f = float(obj.get("feels_like_f"))
        _humidity = int(obj.get("humidity"))
        _cloud = int(obj.get("cloud"))
        _daytime = bool(obj.get('daytime'))
        _condition = str(obj.get("condition"))
        _icon_url = str(obj.get("icon_url"))
        _wind_mph = float(obj.get("wind_mph"))
        _wind_kph = float(obj.get("wind_kph"))
        _wind_direction = str(obj.get("wind_direction"))
        _wind_degree = int(obj.get("wind_degree"))
        return WeatherCurrent(_location, _region, _country, _latitude, _longitude, _timezone, _local_time, _temp_c,
                              _temp_f, _feels_like_c, _feels_like_f, _humidity, _cloud, _daytime, _condition, _icon_url,
                              _wind_mph, _wind_kph, _wind_direction, _wind_degree)


@dataclass
class WeatherForecastItem:
    date: str
    max_temp_c: float
    max_temp_f: float
    min_temp_c: float
    min_temp_f: float
    avg_temp_c: float
    avg_temp_f: float
    will_it_rain: bool
    chance_of_rain: int
    condition: str
    icon_url: str
    sunrise: str
    sunset: str
    max_wind_mph: float
    max_wind_kph: float

    @staticmethod
    def from_dict(obj: Any) -> 'WeatherForecastItem':
        _date = str(obj.get("date"))
        _max_temp_c = float(obj.get("max_temp_c"))
        _max_temp_f = float(obj.get("max_temp_f"))
        _min_temp_c = float(obj.get("min_temp_c"))
        _min_temp_f = float(obj.get("min_temp_f"))
        _avg_temp_c = float(obj.get("avg_temp_c"))
        _avg_temp_f = float(obj.get("avg_temp_f"))
        _will_it_rain = bool(obj.get("will_it_rain"))
        _chance_of_rain = int(obj.get("chance_of_rain"))
        _condition = str(obj.get("condition"))
        _icon_url = str(obj.get("icon_url"))
        _sunrise = str(obj.get("sunrise"))
        _sunset = str(obj.get("sunset"))
        _max_wind_mph = float(obj.get("max_wind_mph"))
        _max_wind_kph = float(obj.get("max_wind_kph"))
        return WeatherForecastItem(_date, _max_temp_c, _max_temp_f, _min_temp_c, _min_temp_f, _avg_temp_c, _avg_temp_f,
                                   _will_it_rain, _chance_of_rain, _condition, _icon_url, _sunrise, _sunset,
                                   _max_wind_mph, _max_wind_kph)


@dataclass
class WeatherForecast:
    location: str
    region: str
    country: str
    latitude: float
    longitude: float
    timezone: str
    local_time: str
    forecast: List[WeatherForecastItem]

    @staticmethod
    def from_dict(obj: Any) -> 'WeatherForecast':
        _location = str(obj.get("location"))
        _region = str(obj.get("region"))
        _country = str(obj.get("country"))
        _latitude = float(obj.get("latitude"))
        _longitude = float(obj.get("longitude"))
        _timezone = str(obj.get("timezone"))
        _local_time = str(obj.get("local_time"))
        _forecast = [WeatherForecastItem.from_dict(y) for y in obj.get("forecast")]
        return WeatherForecast(_location, _region, _country, _latitude, _longitude, _timezone, _local_time, _forecast)
