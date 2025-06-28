## Padrões

### Factory
- /npc/factory.py: criação de NPCs, sendo Enemie ou Friend
- /atack/factory.py: criação de Atacks, tendo múltiplas classes de ataques diferentes

### Template pattern
- /atack/model.py: ataques podem implementar seus próprios métodos de cálculo de dano, ou utilizar a base

### Singleton
- /game/model.py: cria a única instância de jogo que será utilizada

### Mediator
- (planejado) /battle

### Strategy
- (planejado) /weather_effect