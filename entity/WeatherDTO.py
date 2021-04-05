from entity.Weather import Weather
from entity.Main import Main

class WeatherDTO:

    def __init__ (self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.cod = data["cod"]

        self.weather = Weather(data["weather"][0])
        self.main = Main(data["main"])
