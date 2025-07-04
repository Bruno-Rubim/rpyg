from weather.strategies import WeatherEffect
from interface import UI

# contexto das estratégias
# segura uma única estratégia e pode performar sua função
# as estratégias podem ser trocadas livremente durante o 
# funcionamento do programa

class WeatherContext():
    def __init__(self):
        self.strategy: WeatherEffect = None

    def set_strat(self, strategy: WeatherEffect):
        UI.print_text('\n' + strategy.event_desc)
        self.strategy =  strategy

    def do_strat(self, entities):
        if self.strategy:
            UI.print_text('\n' + self.strategy.efect_desc)
            self.strategy.affect(entities)