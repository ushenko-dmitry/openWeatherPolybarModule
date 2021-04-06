import requests
import configparser

from entity.Parameter import Parameter
from entity.WeatherDTO import WeatherDTO

class WeatherService:
    __url = "http://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&lang={lang}&appid=API_KEY"

    def getWeatherDTO(self, parameter):
        data = self.getData(parameter.city, parameter.units, parameter.lang)
        return WeatherDTO(data)

    def getData (self, city, units, lang):
        url = self.__url.replace("{city}", city).replace("{units}", units).replace("{lang}", lang)
        try:
            return requests.get(url).json()
        except requests.exceptions.ConnectionError:
            print('Error: no internet connection')

    def getParameterFromConfigFile (self):
        config = configparser.ConfigParser()
        config.read('config')

        parameter = Parameter()
        parameter.lang = config["Global"]["lang"]
        parameter.units = config["Global"]["units"]
        parameter.city = config["Global"]["city"]
        parameter.round = int(config["Global"]["round"])
        return parameter

    def printWeather (self, weather, parameter):
        print (weather.weather.description, end=' ')
        if parameter.round > 0:
            print (round(weather.main.temp, parameter.round), end=' ')
            print ("(" + str(round(weather.main.feelsLike, parameter.round)) + ")", end=' ')
        else:
            print (round(weather.main.temp), end=' ')
            print ("(" + str(round(weather.main.feelsLike)) + ")", end=' ')
        print ()
