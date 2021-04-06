import configparser

from entity.WeatherDTO import WeatherDTO
from service.WeatherService import WeatherService

weatherService = WeatherService()

parameter = weatherService.getParameterFromConfigFile()
weather = weatherService.getWeatherDTO(parameter)
weatherService.printWeather(weather, parameter)
