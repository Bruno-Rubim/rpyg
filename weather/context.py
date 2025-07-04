from weather.strategies import WeatherEffect

class WeatherContext():
    def __init__(self):
        self.strategy: WeatherEffect = None

    def set_strat(self, strategy: WeatherEffect):
        self.strategy =  strategy

    def do_strat(self, entities):
        if self.strategy:
            self.strategy.affect(entities)