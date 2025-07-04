from weather.strategies import WeatherEffect

class WeatherContext():
    def __init__(self):
        self.strategy: WeatherEffect = None

    def setStrat(self, strategy: WeatherEffect):
        self.strategy =  strategy

    def doStrat(self, entities):
        if self.strategy:
            self.strategy.affect(entities)