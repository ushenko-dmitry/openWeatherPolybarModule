import requests

class WeatherService:
    __url = "http://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&lang={lang}&appid=API_KEY"

    def getData (self, city, units, lang):
        url = self.__url.replace("{city}", city).replace("{units}", units).replace("{lang}", lang)
        try:
            return requests.get(url).json()
        except requests.exceptions.ConnectionError:
            print('Error: no internet connection')
