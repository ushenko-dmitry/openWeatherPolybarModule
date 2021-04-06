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
        parameter.output = config["Global"]["output"]
        return parameter

    def printWeather (self, weather, parameter):
        keySet = {}
        keySet["D"] = weather.weather.description
        if parameter.round > 0:
            keySet["T"] = round(weather.main.temp, parameter.round)
            keySet["F"] = round(weather.main.feelsLike, parameter.round)
            keySet["n"] = round(weather.main.tempMin, parameter.round)
            keySet["x"] = round(weather.main.tempMax, parameter.round)
        else:
            keySet["T"] = round(weather.main.temp)
            keySet["F"] = round(weather.main.feelsLike)
            keySet["n"] = round(weather.main.tempMin)
            keySet["x"] = round(weather.main.tempMax)
        keySet["P"] = weather.main.pressure
        keySet["H"] = weather.main.humidity
        keySet["C"] = weather.name

        for ch in parameter.output:
            if keySet.get(ch) is not None:
                print (keySet.get(ch), end='')
            else:
                print (ch, end='')
        print ()
    
