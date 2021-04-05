import requests, json 

from entity.WeatherDTO import WeatherDTO
from service.WeatherService import WeatherService

city = "Minsk"
units = "metric"
lang = "ru"

weatherService = WeatherService()

data = weatherService.getData(city, units, lang)

weather = WeatherDTO(data)

print(f'{weather.weather.description} {weather.main.temp} ({weather.main.feelsLike})')
