class Main:

    def __init__ (self, data):
        self.temp = data["temp"]
        self.feelsLike = data["feels_like"]
        self.tempMin = data["temp_min"]
        self.tempMax = data["temp_max"]
        self.pressure = data["pressure"]
        self.humidity = data["humidity"]

