import configparser

from entity.WeatherDTO import WeatherDTO
from service.WeatherService import WeatherService

city = "Minsk"
units = "metric"
lang = "en"



def setParamsFromConfig():
    config = configparser.ConfigParser()
    config.read('config')
    global city
    city = config["Global"]["city"]
    global units
    units = config["Global"]["units"]
    global lang
    lang = config["Global"]["lang"]

setParamsFromConfig()

weatherService = WeatherService()

data = weatherService.getData(city, units, lang)

weather = WeatherDTO(data)

print(f'{weather.weather.description} {weather.main.temp} ({weather.main.feelsLike})')
