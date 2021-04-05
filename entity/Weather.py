class Weather:

    def __init__ (self, data):
        self.id = data["id"]
        self.main = data["main"]
        self.description = data["description"]
        self.icon = data["icon"]

    def toString (self):
        print ("Weather: " + self.description)
