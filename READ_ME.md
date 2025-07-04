## Padrões

### Factory
- /atack/factory.py: criação de Atacks, tendo múltiplas classes de ataques diferentes

### Template method
- /atack/model.py: ataques podem implementar seus próprios métodos de cálculo de dano, ou utilizar a base

### Singleton
- /game/model.py: cria a única instância de jogo que será utilizada

### Mediator
- /battle.model.py: gerencia o acesso dos objetos envolvidos

### Strategy
- /weather_effect.strategies.py: estratégias de efeito de clima diferentes que podem ser usadas durante a batalha
- /weather_effect.context.py: contexto que segura uma estratégia até ser mudada